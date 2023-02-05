from classUsuario import Usuario
import path 


class TabelaExercicios:
    def __init__(self, codigo, cpf):
        self.codigo = codigo
        self.cpf = cpf
        self.c = 1  #nº de cada semana de treino criada

        try:
            with open(path.pathT + str(self.codigo) + '.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                linhas = linhas.split('\n')

                for linha in linhas:
                    if cpf == linha[0]:
                        print('Tabela já cadastrada!')
                    else:
                        print('Tabela não cadastrada!')
        except:
            print('Opá, tabela não cadastrada!')  
    
    def fazerTabela(self, semanaTreino, objetivo, c):
        self.semanaTreino = semanaTreino
        self.objetivo = objetivo
        self.c = c

        try:
            with open(path.pathT + str(self.codigo) + '.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            
            with open(path.pathT + str(self.codigo) + '.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha)
                arquivo.write(self.objetivo + '\n')
                arquivo.write('Semana ' + str(self.c) + '\n')
                for dia in semanaTreino:
                    arquivo.write(dia + '\n')
                


        except:                      #Quando for a 1ª lista criada
            with open(path.pathT + str(self.codigo) + '.txt', 'w') as arquivo:
                arquivo.write(self.cpf + '\n')
                arquivo.write(self.objetivo + '\n')
                arquivo.write('Semana ' + str(self.c) + '\n')
                for dia in semanaTreino:
                    arquivo.write(dia + '\n')
        self.c = self.c + 1     #nº das semanas
#Resolva o problema do self.c está sendo = 1 em todas as semanas!!!