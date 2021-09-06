cores = ['amarelo','roxo','vermelho','cinza'] #add lista
n = input('Digite uma cor: ')
if(n in cores):
    print('A cor {} está na posição {} da lista'.format(n,cores.index(n)))
else:
    print('A cor {} não está na lista'.format(n))