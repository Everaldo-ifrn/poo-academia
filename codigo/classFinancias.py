path = 'C:\\Users\\joao felipe\\OneDrive\\Área de Trabalho\\dados de poo academia\\CADASTROS\\'
#import classUsuario
#self.cpf = cliente.cpf

class Financias:
    def __init__(self, cpf):
        self.cpf = cpf 
        try:
            with open(path + self.cpf + '.txt', 'r') as arquivo: #aqui estou vendo se existe cadastro
                linhas = arquivo.readlines()
                r = ''
                for dados in linhas:
                    lista = dados.split(': ')
                    if lista[1] == self.cpf + '\n':
                        r = 'tem'
                        break
                    else:
                        r = 'ntem'
            if r == 'tem':
                for i in linhas: #aqui estou informando qual o plano
                    lista2 = i.split(': ')
                    if lista2[1] == 'MENSAL\n':
                        print('Plano mensal...') 
                        break
                    elif lista2[1] == 'ANUAL\n':
                        print('Plano anual...')
            elif r == 'ntem':
                print('Nao há cadastro com os dados informados!')
        except:
            print('Nao há cadastro com os dados informados!')
    

    def darBaixaFatura(self, mes, valorPago):
        self.mes = mes
        self.valorPago = valorPago
        try:
            with open(path + self.cpf + '.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                cont = -1
                mesAnterior = self.mes - 1
                for dados in linhas:
                    cont = cont + 1
                    if dados == (f'Més-{str(mesAnterior)}-R${str(self.valorPago)}\n'):   #Verificando se o mês anterior tem pendência
                        achei = 'pendente'
                        break
                    elif dados == (f'Més-{str(self.mes)}-PAGO\n'): #Verificando se estar pago
                        achei = 'tempago'
                        break
                    elif dados == (f'Més-{str(self.mes)}-R${str(self.valorPago)}\n'): #verificando se nao estar pago
                        achei = 'tem'
                        break
                    elif 'TAXA' in linhas[8]:
                        achei = 'taxaAnual'
                        break
                    else:
                        achei = 'ntem'
            if achei == 'pendente':
                print('Mes anterior com pendencia!')
            elif achei == 'tem': #sobrecrevendo no arquivo com a fatura dada baixa
                linhas.pop(cont)
                linhas.insert(cont, (f'Més-{str(self.mes)}-PAGO\n'))  
                with open(path + self.cpf + '.txt', 'w') as arquivo:
                    for i in linhas:
                        arquivo.write(i)
                    print('mensalidade dada baixa com sucesso!')
            elif achei == 'tempago':
                print('Mesnsalidade já tá paga!')
            elif achei == 'ntem':
                print('Dados informados errados...')
            elif achei == 'taxaAnual':
                print('Há uma taxa de contrato anual!')
        except:
            print('Erro...')
    
    
    def darBaixaTaxa(self, valorPago):
        self.valorPago = valorPago
        with open(path + self.cpf + ".txt", 'r') as arquivo:
            linhas = arquivo.readlines()
            achei = ''
            if linhas[8] == (f'TAXA: R${valorPago}\n'): #aqui achei melhor verificar na pspsiçao que a gente definiu que a taxa estaria
                achei = "taxa"
            else:
               achei = 'n taxa'
        if achei == 'taxa':
            import os
            arquivo.close()
            nome = path + self.cpf + '.txt'
            lista_arquivo = os.listdir(path)
            for arquivoo in lista_arquivo:
                if arquivoo == self.cpf + '.txt':
                    os.remove(nome)
                    print('TAXA QUITADA')
        elif achei == 'n taxa':
            print('Nao há taxa...')
