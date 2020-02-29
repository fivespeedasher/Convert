import pandas as pd
import chardet
def get_encode_info(file):
    with open(file,'rb') as f:
        return chardet.detect(f.read())['encoding']
IO = "anki.xlsx"
df = pd.read_excel(io = IO, header=None)
df.to_csv('anki.txt',header=None, sep="\t", index=False)
encode_info = get_encode_info('anki.txt')
print(encode_info)