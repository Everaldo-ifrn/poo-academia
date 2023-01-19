path = 'C:\\Users\\20211174010034\\Documents\\GitHub\\classUsuario2.txt'
class Usuario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = str(login)
        self.senha = str(senha)

        try:
            with open(path, 'r') as arquivo:
                c = 1
                linhas = arquivo.readlines()
                for linha in linhas:
                    if linha == self.login + '\n' and linhas[c+1] == self.senha + '\n': 
                        print('achei!')
                        c = c + 1
        except:
            print('Arquivo não existe!')                    

u1 = Usuario('everaldo', 2021, 1234)