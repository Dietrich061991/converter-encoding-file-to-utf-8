#encoding=utf-8
import codecs
import sys
import chardet
import re
from os import listdir
from os.path import isfile, join

### encontrar o tipo de encodiing olhando para 20 linhas no arquivo
def predict_encoding(file_path, n_lines=20):
    '''Prever a codificação de um arquivo usando chardet'''
    # Abra o arquivo como dados binários
    with open(file_path, 'rb') as f:
        # unir linhas binárias para um número especificado de linhas
        rawdata = b''.join([f.readline() for _ in range(n_lines)])
    return chardet.detect(rawdata)['encoding']

## converte para utf
def converte_utf(nome_entrada, nome_saida):
  BLOCKSIZE = 1048576 # ou algum outro tamanho desejado em bytes
  with codecs.open(nome_entrada, "r", predict_encoding(nome_entrada)) as sourceFile:
    with codecs.open(nome_saida, "w", "utf-8") as targetFile:
          while True:
              contents = sourceFile.read(BLOCKSIZE)
              if not contents:
                  break
              targetFile.write(contents)

inputFile = '/data/stage/connect2/lzarng/OUT/atlys/PARQUE_ATLYS_CONTA_MKTGPGM_20200929125959_00001.txt'
outputFile = '/data/stage/connect2/lzarng/OUT/atlys/PARQUE_ATLYS_CONTA_MKTGPGM_20200929125959_00001.txt.utf8'

#verificar o tipo de encoding de um arquivo especifico
fileEncoding = str(predict_encoding(inputFile))

## pegar aqueles que nao sao utf-8 e ascii(ASCII é um subconjunto de UTF-8. Qualquer arquivo codificado em ASCII também é UTF-8 válido.)
if fileEncoding.lower() != "utf-8":
    converte_utf(inputFile, outputFile)
