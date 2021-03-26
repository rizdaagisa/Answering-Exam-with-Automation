import requests
import shutil,os,sys
import pandas as pd
import csv
import hashlib
import secrets
import pypyodbc
import time
import glob
# os.chdir("/directory")

path = os.path.dirname(__file__)
path = path.replace("\\","/")
conf = path+"/DB"
# dbq = "Dbq="+path+"/configuration/" + file + ".mdb;"
# print(os.listdir(conf))

# df['Name']='abc' will add the new column and set all rows to that value:

def convert(file,folder):
    
    driver = r"Driver={MICROSOFT ACCESS DRIVER (*.mdb)};"
    dbq = "Dbq="+path+"/DB/"+folder+"/" + file + ".mdb;"
    con = pypyodbc.connect(driver+dbq)
    res = pd.read_sql(f"SELECT soal,A,B,C,D,kunci,bobot FROM {file}", con,columns=['soal','A','B','C','D','kunci','bobot'])
    cur = con.cursor()
    # run a query and get the results 
    SQL = f'SELECT * FROM {file}' # your query goes here
    rows = cur.execute(SQL).fetchall()
    
    df=pd.DataFrame(res)
    df['matkul']= folder
    df['kode_matkul'] = file
    df.to_csv(f'csv/{file}.csv',header=True, index=False)
    cur.close()
    con.close()

def addfile(nama,kode,token,password):
    with open(r'DB_matkul.csv', 'a') as csvfile:
        fieldnames = ["nama_matkul","KD_matkul","token_matkul","file"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'nama_matkul': nama,
                        'token_matkul': token,
                        'KD_matkul': kode,
                        'file' : password,
                    })
    
    with open(r'daftar matkul.csv', 'a', newline='') as csvfile2:
        fieldnames = ["nama_matkul","token_matkul"]
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writerow({'nama_matkul': nama,
                        'token_matkul': token
                    })

def copyfile():
    i = 1
    for folder in os.listdir(conf):
        for filename in os.listdir(conf+'/'+folder):
            if filename.endswith(".MDB") or filename.endswith(".mdb"):
                print(i,folder,filename)
                n = filename.split(".")
                try:
                    convert(n[0],folder)
                except:
                    pass
                # addfile(folder,n[0],token,password)
                # print(os.path.join(path+"\set", filename))
                shutil.copy2(conf+'/'+folder+"/"+filename,path+'/'+"mdb"+"/"+filename)
                time.sleep(1.5)
        i+=1

def merge():
    combined_csv_data = pd.concat([pd.read_csv(path+"/csv/"+f) for f in os.listdir(path+"/csv")])
    combined_csv_data.to_csv('DB_matkul.csv')

# copyfile()
merge()

# convert("KU000206","Agama islam")
# params = {
#     'outputFormat' : 'csv',
#     'errorResponse': 'zip',
# }

# files = {
#     'files[]': ('database.mdb', open('KD021216.mdb', 'rb')),
# }

# response = requests.post('https://www.rebasedata.com/api/v1/convert?outputFormat=csv&errorResponse=zip', files=files)
# open('output.csv', 'wb').write(response.content)