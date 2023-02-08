from classUsuario import Usuario
import path 


class TabelaExercicios:
    def __init__(self, cpf, c):
        #self.codigo = codigo
        self.cpf = cpf
        self.c = c  #nº de cada semana de treino criada

        try:
            with open(path.pathT + str(self.cpf) + '.txt', 'r') as arquivo:
                linhas = arquivo.readlines()

                for linha in linhas:
                    linha = linha.split(': ')
                    if str(self.cpf) + '\n' == linha[1]:
                        achei = 'sim'
                        break
                    else:
                        achei = 'não'

                if achei == 'sim':
                    print('>> Tabela já cadastrada! <<')
                else:
                    print('>> Tabela não cadastrada! <<')

        except:
           print('>> Opá, tabela não cadastrada! <<')  
    
    def fazerTabela(self, semanaTreino, objetivo):
        self.semanaTreino = semanaTreino
        self.objetivo = objetivo

        try:
            with open(path.pathT + str(self.cpf) + '.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            
            with open(path.pathT + str(self.cpf) + '.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha)
                arquivo.write('Semana: ' + str(self.c) + '\n')
                arquivo.write('Objetivo: ' + self.objetivo + '\n')
                for dia in semanaTreino:
                    arquivo.write(dia + '\n')
                

        except:                      #Quando for a 1ª lista criada
            with open(path.pathT + str(self.cpf) + '.txt', 'w') as arquivo:
                arquivo.write('CPF: '+ self.cpf + '\n')
                arquivo.write('Semana: ' + str(self.c) + '\n')
                arquivo.write('Objetivo: ' + self.objetivo + '\n')
                for dia in semanaTreino:
                    arquivo.write(dia + '\n')
        self.c = self.c + 1     #nº das semanas

        print('>> Tabela de exercício criada! << \n')

    def verTabela(self):
        try:
            with open(path.pathT + str(self.cpf) + '.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    print(linha)
        except:
            pass
            # print('>> Não foi possivel ver a Tabela de exercício, pois ela não existe! << \n')


    def alterarTabela(self, tabelaAlterar, semanaTreinoNova, objetivo):
        self.tabelaAlterar = tabelaAlterar  #nº da semana a ser mudada
        self.semanaTreinoNova = semanaTreinoNova     #nova semana 
        self.objetivo = objetivo 
        try:
            with open(path.pathT + str(self.cpf) + '.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                i = 0       #índice da linha da semana que será apagada
                for linha in linhas:
                    linha = linha.split(': ')
                    if linha[1] == str(self.tabelaAlterar) + '\n':
                        break
                    i = i + 1

                
                try:
                    while linhas[i] != ('Semana: ' + str(self.tabelaAlterar + 1) + '\n'):
                        linhas.pop(i)
                except IndexError:
                    pass

                cont = 1
                for dia in semanaTreinoNova:
                    linhas.insert(i, semanaTreinoNova[- cont] + '\n')
                    cont = cont + 1
                linhas.insert(i, 'Objetivo: ' + str(self.objetivo) + '\n')
                linhas.insert(i, 'Semana: ' + str(self.tabelaAlterar) + '\n')
                    
            with open(path.pathT + str(self.cpf) + '.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha)
            print('>> Tabela Alterada com sucesso! <<')

        except:
            print('>> Não foi possivel alterar a Tabela de exercício, pois ela não existe! << \n')