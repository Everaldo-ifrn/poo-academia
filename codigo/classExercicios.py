from classUsuario import Usuario
path = 'C:\\Users\\joao felipe\\OneDrive\\Área de Trabalho\\dados de poo academia\\TABELAS\\'

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
    
    def fazerTabela(self, diaSemana, treino, objetivo):
        self.diaSemana = diaSemana
        self.treino = treino
        self.objetivo = objetivo
        tabelas = [[],[],[],[],[],[],[]]
        tabelas[0] = (f'CODIGO: {self.codigo}\n')
        tabelas[1] = (f'OBJETIVO: {self.objetivo}\n')
        print(tabelas)
    
            
        if self.diaSemana == 1:
            tabelas.insert(2, (f'SEGUNDA:{self.treino}\n'))
              
            
        elif self.diaSemana == 2:
            tabelas.insert(3, (f'TERÇA:{self.treino}\n'))
               
                
        elif self.diaSemana == 3:
            tabelas.insert(4, (f'QUARTA:{self.treino}\n'))
               
                
        elif self.diaSemana == 4:
            tabelas.insert(5, (f'QUINTA:{self.treino}\n'))
                
            
        elif self.diaSemana == 5:
            tabelas.insert(6, (f'SEXTA:{self.treino}\n'))
            
        elif diaSemana == 0:
            with open(path + str(self.codigo) + '.txt', 'a') as arquivo:
                for i in tabelas:
                    if i != []:
                        arquivo.write(i)
        
                        
        #O BuUG QUE ESTAR OCORRENDO NAOOOO TEM LOGICA NENHUMA!!! 1:20 JA E EU N DESENROLEI, VOU DORMIR