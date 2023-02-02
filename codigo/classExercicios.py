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
    
    def fazerTabela(self, codigo, diaSemana, treino):
        pass
                        