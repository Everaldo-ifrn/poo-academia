path = 'C:\\Users\\20211174010034\\Desktop\\classUsuario.txt'
class Usuario:
    def __init__(self, cpf):          #Verificar se existe cadastro
        self.cpf = cpf
        try:
            with open(path, 'r') as arquivo:
                lista = arquivo.readlines()
                r = ''                             #r é a resposta se tá ou não cadastrado
                for linhas in lista:
                    linha = linhas.split('\n')      #linha é do tipo string
                    if linha[0] == str(self.cpf):
                        r = 'sim'
                        break
                if r == 'sim':
                    print('Usuário já tá cadastrado!')
                else:
                    print('Usuário não tá cadastrado')
                    r = 'não'
        except:
            print('Usuario e arquivo não cadastrado!')
            
    
    def fazerCadastro(self, nome, telefone, endereco, altura, peso, medicoes, plano):
        self.nome = nome
        self.telefone = str(telefone)
        self.endereco = endereco
        self.altura = str(altura)
        self.peso = str(peso)
        self.medicoes = str(medicoes)
        self.plano = plano

        with open(path, 'w') as arquivo:
            arquivo.write('Nome: ' + self.nome + '\n')
            arquivo.write('CPF: ' + str(self.cpf) + '\n')
            arquivo.write('Telefone: ' + self.telefone + '\n')
            arquivo.write('Endereço: ' + self.endereco + '\n')
            arquivo.write('Altura: ' + self.altura + '\n')
            arquivo.write('Peso: ' + self.peso + '\n')
            arquivo.write('Medições: ' + self.medicoes + '\n')
            #Condições de ver o plano
            arquivo.write('Plano: ' + self.plano + '\n')


    def alterarDados(self, cpf):
        pass





        

                         


u1 = Usuario(202020)
u1.fazerCadastro('Everaldo', 8491111111, 'Pedro alves, 123', 1.75, 55.0, 20, 'Mensal')
