import pandas as pd

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
    # a = df.filter(like=f'{data}')
    # b = df.loc[:, df.columns.str.contains(f'{data}')]
    # c = df.loc[df['soal'].str.contains('{}|{}'.format("Satuan arus", "Ampere"),na=False,case=False,regex=True)]['soal']
    kunci =df.loc[df['soal'].str.contains(data, na=False,case=False,regex=True) | (df['soal'] == data)]['kunci'].values[0]
    jawaban = df.loc[df['soal'].str.contains(data, na=False,case=False,regex=True) | (df['soal'] == data)][kunci.lower()].values[0]
    # e =df[df['soal'].str.contains(r'{}|baz'.format(data))][0]
    # f = df[df['soal'].str.contains(data, case=False)]
    # g = df[df['soal'].str.contains(data)]
    print(jawaban)

search("Sebuah tahanan 2,2")