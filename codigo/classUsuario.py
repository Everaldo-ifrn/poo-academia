#LEMBRE-SE: Mude o PATH!

path = 'C:\\Users\\Everaldo Junior\\Desktop\\'
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
                     arquivo.write('PLANO: ANUAL\n')
                     for i in range(1, 13):
                          arquivo.write(f'Més{i}: R${self.mensalidade}\n')
            if self.plano == 2:
                     arquivo.write('PLANO: MENSAL\n')
                     for i in range(1, 13):
                         arquivo.write(f'Més{i}: R${self.mensalidade}\n')
            

    def alterarDados(self, cpf):
        try: 
            with open(path + cpf + '.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                lista = []
                dados = ['Nome', 'CPF', 'Telefone', 'Endereço', 'Altura', 'Peso', 'Medições', 'PLANO'] #criei essa lista pq fica mais facil o código usando for
                c = 0
                re = ''

                for linha in linhas:
                    linha = linha.split(': ')
                    if linha[1] == cpf + '\n':
                        re = 'Sim'
                        break

                if re == 'Sim':
                    r = int(input('O que você quer mudar? \n|1| Nome \n|2| CPF \n|3| Telefone \n|4| Endereço \n|5| Altura \n|6| Peso \n|7| Medições \n|8| Plano \n'))
                    novoDado = input('Qual é o novo dado? \n')
                    for linha in linhas:
                        if r == (c+1):                     #Estou mudando o dado que ele escolheu
                            linha = linha.split(': ')
                            if linha[0] == dados[c]:
                                linha.pop(1)
                                linha.insert(1, novoDado + '\n')
                                lista.append(linha[0] + ': ' + linha[1])
                        else:
                            lista.append(linha)  
                        c = c + 1
                    arquivo.close()
                    with open(path + cpf + '.txt', 'w') as arquivo:           #Estou reescrevendo a todos os dados com o novo dado
                        for l in lista:
                            arquivo.write(l)    
                
                else:
                    print('Não há dados cadastro!') 
        except:
            print('Não há dados cadastro!')


    def relatorio(self, cpf):
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
    

    def cancelarCadastro(self, cpf): 
        self.cpf = cpf
        try:
             with open(path+self.cpf+'.txt', 'r') as arquivo:
                 lista = arquivo.readlines()
                 r = ''
                 for plano in lista:
                     lista2 = plano.split(': ')
                     if lista2[1] == 'MENSAL\n':
                         r = 'MENSAL'
                         arquivo.close()
                         break
                     if lista2[1] == 'ANUAL\n':
                         r = 'ANUAL'
                         break
             if r == 'MENSAL':
                 import os
                 lista_arquivos = os.listdir(path)
                 nome = path + self.cpf + '.txt'
                 for arquivox in lista_arquivos:
                     if arquivox == self.cpf + '.txt':
                        os.remove(nome)  #aqui usamos essa biblioteca para apagar o arquivo do computador(apenas mensais que nao  atribuem taxas)
                        print('CADASTRO CANCELADO')
             elif r == 'ANUAL':          #aqui cancelamos as parcelas e atribuimos a taxa no arquivo, em finacias pode-se dar baixa
                 with open(path+self.cpf+'.txt', 'r') as arquivo:
                     lista = arquivo.readlines()
                     for i in range(12):
                         lista.pop(8)
                     taxa = input('Informe o valor da taxa>>>')
                     lista.append(f'TAXA: R${taxa}\n')
                 with open(path+self.cpf+'.txt', 'w') as arquivo:
                    for i in lista:
                         arquivo.write(i)
                    print('CADASTRO CANCELADO...TAXA PENDENDTE...')        
        except:
            print('NAO HÁ DADOS RELACIONADOS A ESSE CADASTRO!')              
                     

while True:
     cpf = input('Seja bem vindo ao sistema, por favor digite o CPF do cliente> ')
     cliente = Usuario(cpf)
     print(' ')
     try:
        sistema = int(input('O que deseja fazer...\n[1] para fazer cadastro:\n[2] para alterar dados de cadastro\n[3] para ver relatorio de cadastro\n[4] para cancelar cadastro\n[5] para finalizar sistema\n>'))
        print(' ')

        if sistema == 1:
            nm = input('Digite o nome> ')
            tel = input('Digite o telefone> ')
            end = input('Informe o endereço[Cidade, bairro, rua e numero]> ')
            alt = input('Informe a altura> ')
            ps = input('Informe o peso> ')
            mdcs = input('Informe as mediçoes(Braço, perna e cintura)> ')
            plano = int(input('informe qual o plano: ANUAL[1] / MENSAL[2]> '))
            mnsldd = float(input('Informe a mensalidade correspondente ao plano> '))
            cliente.fazerCadastro(nm, tel, end, alt, ps, mdcs, plano, mnsldd)
            print(' ')

        elif sistema == 2:
            cpf = input('Informe o CPF correspondente ao cadastro que deseja mudar os dados...> ')
            cliente.alterarDados(cpf)
            print(' ')

        elif sistema == 3:
            cpf = input('Informe o CPF correspondente ao cadastro que deseja olhar o relatorio...> ')
            cliente.relatorio(cpf)
            print(' ')

        elif sistema  == 4:
            cpf = input('Informe o CPF correspondente ao cadastro que deseja cancelar...> ')
            cliente.cancelarCadastro(cpf)
            print(' ')

        elif sistema == 5:
            print('Ate mais...')
            break
        
     except ValueError:
         print('>> Você digitou algo fora da lista dada, tente novamente! <<')
