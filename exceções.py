# try -> Bloco que executa o codigo que pode conter uma exceção
# except -> Bloco que lida com exceção
# finally -> Bloco que lida com a finalização dos blocos, independente de ocorrer uma exceção ou não 

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Numero sendo dividido por zero!")
finally:
    print("Bloco executado com sucesso!")
