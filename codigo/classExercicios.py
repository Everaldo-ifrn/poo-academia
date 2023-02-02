from classUsuario import Usuario
path = 'C:\\Users\\Everaldo Junior\\Desktop\\'

#Usuario.cpf
class TabelaExercicios:
    def __init__(self, codigo, cpf):
        self.codigo = codigo
        self.cpf = cpf

        try:
            with open(path, 'r') as arquivo:
                linhas = arquivo.readlines()
                linhas = linhas.split('\n')

                for linha in linhas:
                    if cpf == linha[0]:
                        print('Tabela já cadastrada!')
                    else:
                        print('Tabela não cadastrada!')
        except:
            print('Opá, tabela não cadastra!')
    
    def fazerTabela(self, codigo):
        exercicios = []      #Decidir usar duas pra aquele negocio de matriz dar certo
        repeticoes = []
        self.codigo = codigo
        c = 1                 #Número do dia par evitar várias condições(tipo contagem dos dias, para saber o índice)

        
        
        for dia in range(1, 6):
            if dia == c:                
                dia = int(input('Escolha o dia pra treinar: \n|1| Segunda-Feira \n|2| Terça-Feira \n|3| Quarta-Feira \n|4| Quinta-Feira \n|5| Sexta-Feira \n|6| Nenhum \n'))
                if dia == 6:           #Quando ele chegar no dia 6, irá para o código
                    break

                exercicio = input('Qual exercicio? ')
                repeticao = input('Quantas repetições? ')
                exercicios.insert(c, exercicio)
                repeticoes.insert(c, repeticao)
                print(exercicios) #####
                print(repeticoes) #####
                    
            

            c = c + 1
        exercicios.append(repeticoes)
        print(exercicios)

        

        
# [[]]

#lista = [[1],[],[2]]
#for i in lista:
#    if i != []:
#        print(i[0])