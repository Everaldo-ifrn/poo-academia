from classUsuario import cliente
path = 'C:\\Users\\joao felipe\\OneDrive\Área de Trabalho\\dados pessoais(academia)\\'


class Financias:
  try:
    def __init__(self):
        with open(path+cliente.cpf+'.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                lista = linha.split(': ')
                if lista[1] == classUsuario.cpf+'\n':
                    print('achei')
                else:
                    print('a')
  except:
    print('b')