from classUsuario import Usuario
path = 'C:\\Users\\20211174010034\\Desktop\\'

#Usuario.cpf
class TabelaExercicios:
    def __init__(self, codigo, cpf):
        self.codigo = codigo
        self.cpf = cpf


        with open(path, 'r') as arquivo:
            linhas = arquivo.readlines()
            linhas = linhas.split('\n')

            for linha in linhas:
                if cpf == linha[0]:
                    print('Tabela já cadastrada!')
                else:
                    print('Tabela não cadastrada!')

    
    def fazerTabela(self, codigo, diaSemana):
        self.diaSemana = diaSemana
        self.codigo = codigo

# [[]]

#lista = [[1],[],[2]]
#for i in lista:
#    if i != []:
#        print(i[0])