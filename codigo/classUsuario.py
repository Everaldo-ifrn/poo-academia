path = 'C:\\Users\\joao felipe\\OneDrive\\Documents\\IFRN CURSO PROGRAMAÇA\\ACADEMIA\\dados pessoais(academia)\\'
class Usuario:
    def __init__(self, cpf):          #Verificar se existe cadastro
        self.cpf = cpf
        try:
            with open(path+self.cpf+'.txt', 'r') as arquivo:
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
                     arquivo.write('PLANO>>>MENSAL''\n')
                     for i in range(1, 13):
                          arquivo.write(f'Més{i}: R$80\n')
            if self.plano == 2:
                     arquivo.write('PLANO>>>MENSAL''\n')
                     for i in range(1, 13):
                         arquivo.write(f'Més{i}: R$100\n')
            

    def alterarDados(self, cpf):
        pass



while True:
    sistema = int(input('O que deseja fazer...\n[1] para fazer cadastro:\n[2] para alterar dados de cadastro\n[3] para ver relatorio de cadastro\n[4] para cancelar cadastro\n[5] para finalizar sistema\n>'))
    if sistema == 1:
        cpf = input('Por favor digit o CPF>')
        cliente = Usuario(cpf)
        nm = input('Digite o nome>')
        tel = input('Digite o teelefone>')
        end = input('Informe o endereço[Cidade, bairro, rua e numero]>')
        alt = input('Informe a altura>')
        ps = input('Informe o peso>')
        mdcs = input('Informe as mediçoes(Braço, perna e cintura)>')
        plano = int(input('informe qual o plano: ANUAL[1]/MENSAL[2]>'))
        cliente.fazerCadastro(nm, tel, end, alt, ps, mdcs, plano)
    if sistema == 5:
        print('Ate mais...')
        break



