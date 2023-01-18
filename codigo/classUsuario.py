#Um program em que ele vera se uma determidade tem um cadastro na academia, se tiver tem que pagar a mensalidade pendente, se nao tiver ira perguntar
#se o individuo deseja fazer um e qual a categoria de mensalidade ele quer fazer

path = 'C:\\Users\\Everaldo Junior\\Documents\\MeusProjetos\\Teste\\testando_usuario.txt'
class Usuario:
    def __init__(self, nome, usuario, senha):
        self.nome = nome
        self.usuario = usuario
        self.senha = senha

        try:
            with open(path, 'r') as arquivo:
                lista1 = arquivo.readlines()         #r é a resposta se existe ou não cadastro
                r = ''
                c = 0                         
                for i in lista1:
                    if r == 'Sim':
                        break
                    l1 = i.split('---')
                    for senha in l1:
                        if (senha == self.senha) and (self.nome in l1[c-1]):
                            r = 'Sim'            
                            print('<<<Voçê possui um cadastro>>>')
                               
                            break
                        else:
                            r = 'Não'
                        c = c + 1              #índice da senha

                if r == 'Não':
                    print('<<<Nao existe cadastro com os dados digitados>>>')
                        
                            
        except:
            print('Ainda não há nada no sistema')
            with open(path, 'w') as arquivo:
                arquivo.write('')


    def cadastro(self, novonome, novasenha, categoria):
        self.categoria = categoria
        self.novonome = novonome
        self.novasenha = novasenha
        with open(path, 'a') as arquivo:
            if self.categoria == 1:
                arquivo.write((f'{self.novonome}---{self.novasenha}---Anual\nValor a ser pago:{12*115}\n'))
            if self.categoria == 2:
                arquivo.write((f'{self.novonome}---{self.novasenha}---Mensal\nValor a ser pago:{12*150}\n'))
    

#    def pagamento(self, valor):
#        with open(path, 'r') as arquivo:
#            linhas = arquivo.readlines()
#            print(linhas)

nomex = input('Digite seu nome: ')
usuariox = input('Digite seu usuário: ')
senhax = input('Digite sua senha: ')
Pessoa = Usuario(nomex, usuariox, senhax)

while True:
    atendente = int(input(' O que deseja fazer agora? Cadastro = (1), nada = (2), pagar mensalidade = (3)'))

    try:
        if atendente == 1:
            with open(path, 'r') as arquivo:             #vendo se já tem ou não cadastro
                linhas = arquivo.readlines()
                r = ''
                for linha in linhas:
                    if r == 'Sim':
                        break
                    linha = linha.split('---')
                    for palavra in linha:
                        if nomex in palavra:
                            r = 'Sim'
                            print('<<<Ops, você já tem um cadastro!>>>')
                            break

            if r == '':
                atendente2 = int(input('Informe a categoria de mensalidade desejada: Anual por R$1200 = (1) ou mensal por R$150 = (2): '))
                nomeNovo = input('Digite seu nome COMPLETO: ')
                senhaNova = input('Digite uma senha com 4 digitos: ')
                Pessoa.cadastro(nomeNovo, senhaNova, atendente2)

        elif atendente ==  2:
            print('Ate logo mais!')
            break

    #    elif atendente == 3:
    #        valor = int(input('Valor do dinheiro: R$'))
    #        Pessoa.pagamento(valor)

    except ValueError:
        print('Opa, o número digitado está fora da lista. Tente novamente!')

#FELIPE:fiz testes e entendi o que voçe fez