
class Exercicios:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.senha = senha
        self.login = login
        self.path = 'C:\\Users\\joao felipe\\OneDrive\\Documents\\IFRN CURSO PROGRAMAÇA\\ACADEMIA\\'+self.nome+'.txt' #temos que  ver como podemos evitar algum erro caso ele erre o nome, ou bote diferente(mas acho que as condiçoes dao conta disso)

    
    def fzrTabela(self):
        try:    #O TRY ESTAR TRATANDO DO ERRO DE NAO EXISTIR UM ARQUIVO AINDA  E DO ERRO SE CASSO A VARIAVEL ACHEI ESTIVER VAIZA(SEM NADA).
             with open(self.path, 'r') as arquivo:
                 tabelas = arquivo.readlines()
                 for i in tabelas:
                     tabela = i.split('<===>')
                     if tabela[0] == self.login and tabela[1] == self.senha+'\n':
                        achei = 1
                        break
             
             if achei == 1:    #o que pode evitar o erro mencionado a cima(linhas 7) é melhorar essas condiçoes 
                 print('ops! voce ja possui uma tabela de treinos!')
             else:
                 print('<<<<VAMOS COMEÇAR A CRIAR SEU PLANEJAMENTO>>>>')
                 print('ESTES SAO OS TREINOS: OMBRO, BICEBS, TRICiPS, PANTURRILHA, COXA, DORSAL, ABDOMEM, PEITO')
                 segunda = input('Treino da segunda: ')
                 terça = input('Treino da terça: ')
                 quarta = input('Treino da quarta: ')
                 quinta = input('Treino da quinta: ')
                 sexta = input('Treino da sexta: ')
                 with open(self.path, 'a') as arquivo:
                     arquivo.write(f'{self.nome}<===>{self.senha}\nsegunda: {segunda}\nTerça: {terça}\nQuarta: {quarta}\nQuinta: {quinta}\nSexta{sexta}\n')
             
        except: #BOTEI ESSE CODIGO COMO EXEÇAO PORQUE ACHEI PRATICO, JA QUE NAO FAZ SENTIDO MOSTRAR PARA O CLIENTE QUE O ARQUIVO NAO EXISTE 
             print('<<<<VAMOS COMEÇAR A CRIAR SEU PLANEJAMENTO>>>>')
             print('ESTES SAO OS TREINOS: OMBRO, BICEBS, TRICiPS, PANTURRILHA, COXA, DORSAL, ABDOMEM, PEITO')
             segunda = input('Treino da segunda: ')
             terça = input('Treino da terça: ')
             quarta = input('Treino da quarta: ')
             quinta = input('Treino da quinta: ')
             sexta = input('Treino da sexta: ')
             with open(self.path, 'a') as arquivo:
                 arquivo.write(f'{self.login}<===>{self.senha}\nsegunda: {segunda}\nTerça: {terça}\nQuarta: {quarta}\nQuinta: {quinta}\nSexta: {sexta}\n')
             print('TABELA DE TREINOS FINALIZADA')




    def alterarTabela(self):
         try: #aqui estar tratando do erro caso o arquivo nao exista ainda
             with open(self.path, 'r') as arquivo:
                 novo = arquivo.readlines()
                 cont = 0
                 for i in novo:
                     cont = cont + 1
                     tabela = i.split('<===>')
                     if tabela[0] == self.login and tabela[1] == self.senha+'\n':
                         for i in range(6):
                             novo.pop(cont-1)
                             achei = 'sim'
                         break        
                     else:
                         achei = 'nao'  #aqui é para caso o login e senha nao seja encontrado
            
             if achei == 'sim':
                 print('<<<<VAMOS COMEÇAR A CRIAR SEU PLANEJAMENTO>>>>')
                 print('ESTES SAO OS TREINOS: OMBRO, BICEBS, TRICiPS, PANTURRILHA, COXA, DORSAL, ABDOMEM, PEITO')
                 s = input('Treino da segunda: ')
                 t = input('Treino da terça: ')
                 q = input('Treino da quarta: ')
                 qi = input('Treino da quinta: ')
                 se = input('Treino da sexta: ')
                 novo.append(f'{self.login}<===>{self.senha}\n')
                 novo.append(f'segunda: {s}\n')
                 novo.append(f'Terça: {t}\n')
                 novo.append(f'Quarta: {q}\n')
                 novo.append(f'Quinta: {qi}\n')
                 novo.append(f'Sexta: {se}\n')
                 with open(self.path, 'w') as arquivo:     #precisamos modificar da seguinte forma: inves de escrever tudo, escrever apenas a nova tabela
                     ps = 0
                     for i in novo:
                         arquivo.write(i)
                 print('ALTERAÇOES FINALIZADAS')
     
             if achei == 'nao':
                 print('ops! nao existe tabela com esse login ou senha')

         except:
             print('Nao existe dados!')
    


while True:
    sistema = int(input('Olá, que deseja?  \n- fazer uma tabela de execicios(1), alterar a sua tabela de exercicios(2), nada(3): '))
    if sistema == 1:
        y = input('Digite seu nome: ')
        w = input('digite seu login: ')
        x = input('Digite sua senha:')
        pessoa = Exercicios(y, w, x)
        pessoa.fzrTabela()
    elif sistema == 2:
        y = input('Digite seu nome: ') 
        w = input('digite seu login: ')
        x = input('Digite sua senha: ')
        pessoa = Exercicios(y, w, x)
        pessoa.alterarTabela()
    elif sistema == 3:
        print('Até mais!')
        break
