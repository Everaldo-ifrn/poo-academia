
class Exercicios:
    def __init__(self, nome, login):
        self.nome = nome
        self.login = login
        self.path = 'C:\\Users\\joao felipe\\OneDrive\\Documents\\IFRN CURSO PROGRAMAÇA\\ACADEMIA\\'+self.login+'.txt'
    
    def fzrTabela(self,data):
        self.data = data
        try:    #O TRY ESTAR TRATANDO DO ERRO DE NAO EXISTIR UM ARQUIVO AINDA  E DO ERRO SE CASSO A VARIAVEL ACHEI ESTIVER VAZIA(SEM NADA).
             with open(self.path, 'r') as arquivo:
                 tabelas = arquivo.readlines()
                 for i in tabelas:
                     tabela = i.split('>>>>')
                     if tabela[1] == self.data+'\n':
                        achei = 1
                        break
             
             if achei == 1:   
                 print('ops! voce ja possui uma tabela de treinos nessa data!')
             else:
                 print('<<<<VAMOS COMEÇAR A CRIAR SEU PLANEJAMENTO>>>>')
                 print('ESTES SAO OS TREINOS: OMBRO, BICEBS, TRICiPS, PANTURRILHA, COXA, DORSAL, ABDOMEM, PEITO')
                 segunda = input('Treino da segunda: ')
                 terça = input('Treino da terça: ')
                 quarta = input('Treino da quarta: ')
                 quinta = input('Treino da quinta: ')
                 sexta = input('Treino da sexta: ')
                 with open(self.path, 'a') as arquivo:
                     arquivo.write(f'===={self.nome}====\nData>>>>{self.data}\nsegunda: {segunda}\nTerça: {terça}\nQuarta: {quarta}\nQuinta: {quinta}\nSexta{sexta}\n')
             
        except: #BOTEI ESSE CODIGO COMO EXEÇAO PORQUE ACHEI PRATICO, JA QUE NAO FAZ SENTIDO MOSTRAR PARA O CLIENTE QUE O ARQUIVO NAO EXISTE 
             print('<<<<VAMOS COMEÇAR A CRIAR SEU PLANEJAMENTO>>>>')
             print('ESTES SAO OS TREINOS: OMBRO, BICEBS, TRICiPS, PANTURRILHA, COXA, DORSAL, ABDOMEM, PEITO')
             segunda = input('Treino da segunda: ')
             terça = input('Treino da terça: ')
             quarta = input('Treino da quarta: ')
             quinta = input('Treino da quinta: ')
             sexta = input('Treino da sexta: ')
             with open(self.path, 'a') as arquivo:
                 arquivo.write(f'===={self.nome}====\nData>>>>{self.data}\nsegunda: {segunda}\nTerça: {terça}\nQuarta: {quarta}\nQuinta: {quinta}\nSexta: {sexta}\n')
             print('TABELA DE TREINOS FINALIZADA')

    def verTabelas(self):
        try:
             with open(self.path, 'r') as arquivo:
                 tabelas = arquivo.readlines()
                 for i in tabelas:
                     print(i)
        except:
             print('Nao há nenhuma tabela registrada!')



while True:
    sistema = int(input('Olá, que deseja?\n- fazer uma tabela de execicios(1), ver tabelas(2), nada(3): '))
    if sistema == 1:
        y = input('Digite o nome(COMPLETO): ')
        w = input('digite o login(CPF): ')
        z = input('Digite a data(x/x/x):') #podemos melhorar a forma que pedimos a data para evitar erros
        pessoa = Exercicios(y, w)
        pessoa.fzrTabela(z)
    elif sistema == 2:
        y = input('Digite o nome(COMPLETO): ') 
        w = input('digite o login(CPF): ')
        pessoa = Exercicios(y, w)
        pessoa.verTabelas()

    elif sistema == 3:
        print('Até mais!')
        break
