from classUsuario import Usuario
import path 


class TabelaExercicios:
    def __init__(self, codigo, cpf):
        self.codigo = codigo
        self.cpf = cpf

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
    
    def fazerTabela(self, diaSemana, treino, objetivo):
        self.diaSemana = diaSemana
        self.treino = treino
        self.objetivo = objetivo
        tabelas = [[],[],[],[],[],[],[]]
        while True:               #Coloquie de novo o while para acabar com o erro de escrever codigo e objetivo no final
            if diaSemana == 0:        #a cada dia ele está escrevendo codigo e objetivo e não a cada semana!
                break

            tabelas[0] = (f'CODIGO: {self.codigo}\n')
            tabelas[1] = (f'OBJETIVO: {self.objetivo}\n')
        
                
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


        

            print(tabelas)
            with open(path.pathT + str(self.codigo) + '.txt', 'r') as arquivo:          #lendo o que já existe
                    linhas = arquivo.readlines()
            

            with open(path.pathT + str(self.codigo) + '.txt', 'w') as arquivo:          #reescrevendo o que já existe
                for linha in linhas:
                    arquivo.write(linha)  

                for i in tabelas:                                                 #escrevendo com novo
                    if i != []:
                        arquivo.write(i)
            break