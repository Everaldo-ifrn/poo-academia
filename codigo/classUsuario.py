path = 'C:\\Users\\joao felipe\\OneDrive\\Documents\\IFRN CURSO PROGRAMAÇA\\ACADEMIA\\dados pessoais(academia)\\'
class Usuario:
    def __init__(self, cpf):          #Verificar se existe cadastro
        self.cpf = cpf
        try:
            with open(path+self.cpf+'.txt', 'r') as arquivo:
                lista = arquivo.readlines()
                r = ''                             #r é a resposta se tá ou não cadastrado
                for linhas in lista:
                    linha = linhas.split(': ')      #linha é do tipo string, #felipe: tive que mudar o delimitador porque tava sendo escrito assim no arqv, CPF: XXXXX
                    if linha[1] == self.cpf+'\n':
                        r = 'sim'
                        break
                    else:
                        r == 'nao'
                if r == 'sim':
                     print('Usuário já cadastrado no sistema!')
                if r == 'nao':
                     print('Nao há cadastro com os dados informados!')
                    
        except: 
            print('Nao há cadastro com os dados informados!')
            
    def fazerCadastro(self, nome, telefone, endereco, altura, peso, medicoes, plano, mensalidade):
        self.nome = nome
        self.telefone = str(telefone)
        self.endereco = endereco
        self.altura = str(altura)
        self.peso = str(peso)
        self.medicoes = str(medicoes)
        self.plano = plano
        self.mensalidade = mensalidade

        with open(path+self.cpf+'.txt', 'a') as arquivo:
            arquivo.write('Nome: ' + self.nome + '\n')
            arquivo.write('CPF: ' + str(self.cpf) + '\n')
            arquivo.write('Telefone: ' + self.telefone + '\n')
            arquivo.write('Endereço: ' + self.endereco + '\n')
            arquivo.write('Altura: ' + self.altura + '\n')
            arquivo.write('Peso: ' + self.peso + '\n')
            arquivo.write('Medições: ' + self.medicoes + '\n')
            #Aqui sera colocado no arquivo aquele plano que foi escolhido
            if self.plano == 1:
                     arquivo.write('PLANO:MENSAL''\n')
                     for i in range(1, 13):
                          arquivo.write(f'Més{i}: R${self.mensalidade}\n')
            if self.plano == 2:
                     arquivo.write('PLANO:MENSAL''\n')
                     for i in range(1, 13):
                         arquivo.write(f'Més{i}: R${self.mensalidade}\n')
            

    def alterarDados(self, cpf):
        pass

    def relatorio(self,cpf):
        self.cpf = cpf
        try:
            with open(path+self.cpf+'.txt', 'r') as arquivo: 
                lista = arquivo.readlines()
                r = ''
                for linhas in lista:
                    linha = linhas.split(': ')
                    if linha[1] == self.cpf+'\n':
                        r = 'sim'
                        break
                if r == 'sim': #se o cpf informado existir no arquivo ira mostrar o relatorio
                    for i in lista: 
                        print(i)
                else:
                    print('Dados nao encontrados!')
        except:
             print('Nao há cadastro com os dados informados!') #Se os dados forem errados entao nao irá abrir nenhum arquivo
    
    def cancelarCadastro(self, cpf): #Precisamos rever a ideia de apagar 
         self.cpf = cpf 
         try:
             with open(path+self.cpf+'.txt', 'r') as arquivo:
                 lista = arquivo.readlines()
                 r = ''
                 for linhas in lista:
                     linha = linhas.split(':')
                     if linha[1] == 'MENSAL\n':
                         r = 'mensal'
                         break
                     if linha[1] == 'ANUAL\n':
                         r = 'anual'
                         break 
                 if r == 'mensal':
                     import os #utilizamos essa funçao que trabalha com arquivos, e uma das suas funçoes é excluir/ acredito que o erro seja aqui
                     os.remove(self.cpf+'.txt')
                     print('CADASTRO CANCELADO COM SUCESSO...')
                 if r == 'anual':
                     pass
         except:
             print('Nao há cadastro com esses dados!')



while True:
     cpf = input('Seja bem vindo ao sistema, por favor digite o CPF do cliente>')
     cliente = Usuario(cpf)
     sistema = int(input('O que deseja fazer...\n[1] para fazer cadastro:\n[2] para alterar dados de cadastro\n[3] para ver relatorio de cadastro\n[4] para cancelar cadastro\n[5] para finalizar sistema\n>'))
     if sistema == 1:
         nm = input('Digite o nome>')
         tel = input('Digite o teelefone>')
         end = input('Informe o endereço[Cidade, bairro, rua e numero]>')
         alt = input('Informe a altura>')
         ps = input('Informe o peso>')
         mdcs = input('Informe as mediçoes(Braço, perna e cintura)>')
         plano = int(input('informe qual o plano: ANUAL[1]/MENSAL[2]>'))
         mnsldd = float(input('Informe a mensalidade correspondente ao plano>'))
         cliente.fazerCadastro(nm, tel, end, alt, ps, mdcs, plano, mnsldd)
     if sistema == 3:
         cpf = input('Informe o CPF novamente por favor...>')
         cliente.relatorio(cpf)
     if sistema  == 4:
         cpf = input('Informe o CPF novamente por favor...>')
         cliente.cancelarCadastro(cpf)
     if sistema == 5:
         print('Ate mais...')
         break



