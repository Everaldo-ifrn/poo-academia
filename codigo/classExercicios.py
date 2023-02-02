from classUsuario import Usuario
path = 'C:\\Users\\20211174010034\\Desktop\\'

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
        print('teste')
        self.diaSemana = diaSemana
        self.treino = treino
        tabelas = [[],[],[],[],[],[]]
        while True:
            if self.diaSemana == 1:
                tabelas.insert(0, f'SEGUNDA:{self.treino}\n')
                
            elif self.diaSemana == 2:
                tabelas.insert(1, f'TERÇA:{self.treino}\n')
                
            elif self.diaSemana == 3:
                tabelas.insert(2, f'QUARTA:{self.treino}\n')
                
            elif self.diaSemana == 4:
                tabelas.insert(3, f'QUINTA:{self.treino}\n')
            
            elif self.diaSemana == 5:
                tabelas.insert(4, f'SEXTA:{self.treino}\n')
                
            elif self.diaSemana == 6:
                tabelas.insert(5, f'SABADO:{self.treino}\n')
                
            elif self.diaSemana == 0:
                with open(path + str(self.codigo) + '.txt', 'a') as arquivo:
                    for i in tabelas:
                        if i != []:
                            arquivo.write(i)
                break

        print(tabelas)
                                