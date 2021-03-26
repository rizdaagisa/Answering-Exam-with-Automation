import pandas as pd
from flask import Flask, jsonify, request , send_file
import os,sys

app = Flask(__name__)
path = os.path.dirname(__file__)
path = path.replace("\\","/")
df = pd.read_csv("DB_matkul.csv",low_memory=False,error_bad_lines=False,index_col=0,dtype={"soal": "string", "a": "string", "b": "string", "c": "string", "d": "string", "kunci": "string", "bobot": "string"})
# df.drop(columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],axis=1, inplace=True)
# df['d'] = df['d'].str.strip()

def main(so):
    soal = df.loc[df["soal"]  == str(so)]['soal'][0]
    matkul = df.loc[df["soal"]  == str(so)]['matkul'][0]
    kunci = df.loc[df["soal"]  == str(so)]['kunci'][0]
    jawaban = df.loc[df["soal"]  == str(so)][kunci.lower()][0]
    print(soal,matkul,kunci,jawaban)

def search(data):
    kunci = df.loc[df['soal'].str.contains(data, na=False,case=False,regex=True) | (df['soal'] == data)]['kunci'].values[0]
    jawaban = df.loc[df['soal'].str.contains(data, na=False,case=False,regex=True) | (df['soal'] == data)][kunci.lower()].values[0]
    return jawaban

@app.route('/',methods=['GET'])
def index():
    return 'Upss mau iseng ya? Silakan hubungi admin untuk membeli program bot UM'

@app.route('/kunci',methods=['POST'])
def kunci():
    result = request.get_json()
    soal = result['soal']
    jawaban  = search(soal)
    return {'jawaban' : jawaban, 'status':'ok'}


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    # app.run(debug=True)