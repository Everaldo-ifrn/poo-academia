from classUsuario import Usuario
path = 'C:\\Users\\Everaldo Junior\\Desktop\\'

#Usuario.cpf
class TabelaExercicios:
    def __init__(self, codigo, cpf):
        self.codigo = codigo
        self.cpf = cpf

        try:
            with open(path + str(self.codigo) + '.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                linhas = linhas.split('\n')

                for linha in linhas:
                    if cpf == linha[0]:
                        print('Tabela já cadastrada!')
                    else:
                        print('Tabela não cadastrada!')
        except:
            print('Opá, tabela não cadastrada!')  
    
    def fazerTabela(self, diaSemana, treino):
        self.diaSemana = diaSemana
        self.treino = treino
        tabelas = [[],[],[],[],[],[]]
        while True:
            if self.diaSemana == 1:
                tabelas.insert(0, f'SEGUNDA:{self.treino}\n')
                break
            
            elif self.diaSemana == 2:
                tabelas.insert(1, f'TERÇA:{self.treino}\n')
                break
                
            elif self.diaSemana == 3:
                tabelas.insert(2, f'QUARTA:{self.treino}\n')
                break
                
            elif self.diaSemana == 4:
                tabelas.insert(3, f'QUINTA:{self.treino}\n')
                break
            
            elif self.diaSemana == 5:
                tabelas.insert(4, f'SEXTA:{self.treino}\n')
                break
                
            elif self.diaSemana == 6:
                tabelas.insert(5, f'SABADO:{self.treino}\n')
                break
            elif diaSemana == 0:
                ##############################################
                #with open(path + str(self.codigo) + '.txt', 'r') as arquivo:
                #    linhas = arquivo.readlines()

                #with open(path + str(self.codigo) + '.txt', 'a') as arquivo:
                #    arquivo.write('1234\n')
                #    pass
                
                """with open(path + str(self.codigo) + '.txt', 'w') as arquivo:     #Reescrevendo...
                    arquivo.write(self.cpf + '\n')
                    #arquivo.write(str(self.codigo) + '\n')
                    for linha in linhas:
                        arquivo.write(linha)"""
                ##############################################

                break
#Falta colocar o codigo no começo de cada semana de treino!

        with open(path + str(self.codigo) + '.txt', 'a') as arquivo:
            #arquivo.write('1234\n') ##################
            for i in tabelas:
                if i != []:
                    arquivo.write(i)
            #linhas = arquivo.readlines()
            #print(linhas)