import sys
import subprocess

def calculaDV(chave43):
     #zerando variaveis
     resto = digito_verificador = soma = 0

     #Multiplicador inicia com 4
     multiplicador = 4
     
     #Multiplica os 43 numeros por seu multiplicador caractere da chave
     for indice in chave43:
        #Multiplica cada digito da chave pelo multiplicador correspondente e soma
        soma = soma + int(indice) * multiplicador
 
        #Se multiplicador chegou a 2, volta para 10
        if(multiplicador == 2):
           multiplicador = 10
        #decrementa 1 para iniciar com 9 quando multiplicador chegar a ser igual a 2
        multiplicador = multiplicador -1
     
     #Pega o resto da divisão através da função mod
     resto = soma % 11
    
     #Dígito verificador é o resultado da subtração 11 - resto
     digito_verificador = 11 - resto
    
     #Testa se o DV é maior = 10
     if(digito_verificador >= 10):
        digito_verificador = 0
    
     #Retorna o DV
     return digito_verificador

try:
    arquivo1 = open('lista.txt', 'r')
except FileNotFoundError:
    print('Foi criado o arquivo "lista.txt" na raiz da pasta pois ele não existia!')
    print('Informe apenas os 43 digitos da chave ou as chaves das notas no arquivo "lista.txt" para gerar uma saida com o DV!\n')
    arquivo1 = open('lista.txt', 'w')
    r = subprocess.call("pause", shell=True)
    sys.exit()

lista = []
lista = arquivo1.readlines()
arquivo1.close()

if not lista:
     print('O arquivo "lista.txt" está vazio!')
     print('Informe apenas os 43 digitos da chave ou as chaves das notas no arquivo "lista.txt" para gerar uma saida com o DV!\n')
     r = subprocess.call("pause", shell=True)
     sys.exit()

lista = [lista.replace('\n', '') for lista in lista]

try:
    arquivo2 = open('outlist.txt', 'w')
except FileNotFoundError:
    arquivo2 = open('outlist.txt', 'w')
print('Processando dados:\n')
for chave in lista:
  digito = calculaDV(chave)
  print(chave+str(digito))
  arquivo2.writelines(chave+str(digito)+'\n')
print('\nProcessamento finalizado com sucesso!\n')
r = subprocess.call("pause", shell=True)
arquivo2.close()
