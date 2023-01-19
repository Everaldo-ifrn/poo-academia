path = 'C:\\Users\\20211174010031\\Downloads\\codigos\\'
class Exercicios:
    def __init__(self, nome, login):
        self.nome = nome
        self.login = login
       
    
    def fzrTabela(self, dia, mes, ano):
        self.dia = str(dia)
        self.mes = str(mes)
        self.ano = str(ano)
        try:    #O TRY ESTAR TRATANDO DO ERRO DE NAO EXISTIR UM ARQUIVO AINDA  E DO ERRO SE CASSO A VARIAVEL ACHEI ESTIVER VAZIA(SEM NADA).
             with open(path+self.login+'.txt', 'r') as arquivo:
                 tabelas = arquivo.readlines()
                 for i in tabelas:
                     tabela = i.split('>>>>')
                     print(tabela)
                     if tabela[1] == self.dia+'/'+self.mes+'/'+self.ano+'\n': #Preciso corrigir um erro presente aqqui que vale para se a data for a mesma de outra tabela
                        achei = 1
                        break
             
             if achei == 1:   
                 print('ops! voce ja possui uma tabela de treinos nessa data!')
             else:
                 print('<<<<VAMOS COMEÇAR A CRIAR SEU PLANEJAMENTO>>>>')
                 segunda = input('Treino da segunda: ')
                 terça = input('Treino da terça: ')
                 quarta = input('Treino da quarta: ')
                 quinta = input('Treino da quinta: ')
                 sexta = input('Treino da sexta: ')
                 with open(path+self.login+'.txt', 'a') as arquivo:
                     arquivo.write(f'===={self.nome}====\nData>>>>{str(self.dia)}/{str(self.mes)}/{str(self.ano)}\nsegunda: {segunda}\nTerça: {terça}\nQuarta: {quarta}\nQuinta: {quinta}\nSexta: {sexta}\n')
             
        except: #BOTEI ESSE CODIGO COMO EXEÇAO PORQUE ACHEI PRATICO, JA QUE NAO FAZ SENTIDO MOSTRAR PARA O CLIENTE QUE O ARQUIVO NAO EXISTE 
             print('<<<<VAMOS COMEÇAR A CRIAR SEU PLANEJAMENTO>>>>')
             segunda = input('Treino da segunda: ')
             terça = input('Treino da terça: ')
             quarta = input('Treino da quarta: ')
             quinta = input('Treino da quinta: ')
             sexta = input('Treino da sexta: ')
             with open(path+self.login+'.txt', 'a') as arquivo:
                 arquivo.write(f'===={self.nome}====\nData>>>>{str(self.dia)}/{str(self.mes)}/{str(self.ano)}\nsegunda: {segunda}\nTerça: {terça}\nQuarta: {quarta}\nQuinta: {quinta}\nSexta: {sexta}\n')
             print('TABELA DE TREINOS FINALIZADA')

    def verTabelas(self):
        try:
             with open(path+self.login+'.txt', 'r') as arquivo:
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
        print('VAMOS ORGANIZAR A DATA...')
        dia = int(input('Digite o dia do més:'))
        mes = int(input('Digite o numero do més:'))
        ano = int(input('Digite o ano:'))
        pessoa = Exercicios(y, w)
        pessoa.fzrTabela(dia, mes, ano)  
    elif sistema == 2:
        y = input('Digite o nome(COMPLETO): ') 
        w = input('digite o login(CPF): ')
        pessoa = Exercicios(y, w)
        pessoa.verTabelas()

    elif sistema == 3:
        print('Até mais!')
        break
