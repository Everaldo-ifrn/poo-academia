from classUsuario import Usuario
from classExercicios import TabelaExercicios
from classFinancias import Financias


n = 0
while True:
     cpf = input('- Seja bem vindo ao sistema, por favor digite o CPF do cliente> ')
     cliente = Usuario(cpf)
     print(' ')
     try:
        sistemaPrincipal = int(input('\nPara que area do sistema deseja se dirigir: \n|1| CADASTROS \n|2| FINANCIAS \n|3| TABELAS \n|4| NADA\n> ')) 
        if sistemaPrincipal == 1:
            sistema = int(input('\nO que deseja fazer...\n[1] para fazer cadastro:\n[2] para alterar dados de cadastro\n[3] para ver relatorio de cadastro\n[4] para cancelar cadastro\n[5] para finalizar sistema\n>'))
            print(' ')

            if sistema == 1:
                nm = input('\nDigite o nome> ')
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
                cpf = input('\nInforme o CPF correspondente ao cadastro que deseja mudar os dados...> ')
                cliente.alterarDados(cpf)
                print(' ')

            elif sistema == 3:
                cpf = input('\nInforme o CPF correspondente ao cadastro que deseja olhar o relatorio...> ')
                cliente.relatorio(cpf)
                print(' ')

            elif sistema  == 4:
                cpf = input('\nInforme o CPF correspondente ao cadastro que deseja cancelar...> ')
                cliente.cancelarCadastro(cpf)
                print(' ')

            elif sistema == 5:
                print('\nAte mais...')
                break
            else:
                print('\n>> Você digitou algo fora da lista dada, tente novamente! <<')
        elif sistemaPrincipal == 2:
                
            clienteF = Financias(cliente.cpf)
            sistema = int(input('\nO que deseja fazer... \n|1| Dar baixa na fatura\n|2| Dar baixa em uma taxa\n>'))
                
            if sistema == 1:
                mes = int(input('\nDigite o numero do mes 1, 2, 3... \n> '))
                valor = float(input('\nInforme o valor da mensalidade \n> '))
                clienteF.darBaixaFatura(mes, valor)

            elif sistema == 2:
                valorT = float(input('\nInforme o valor da taxa \n> '))
                clienteF.darBaixaTaxa(valorT)
        

        elif sistemaPrincipal == 3: #TABELAS
            sistema = int(input('\nO que deseja fazer... \n|1| Fazer tabela de exercício \n|2| Alterar tabela de exercício \n|3| Ver tabela de exercício \n'))
                     

            if sistema == 1:
                r = int(input('\nQual objetivo do treino? \n|1| Esmagrecer \n|2| Ganhar massa muscular \n|3| Definir os muscuslos \n> '))
                if r == 1:
                    objetivo = 'Esmagrecer'
                elif r == 2:
                    objetivo = 'Ganhar massa muscular'
                elif r == 3:
                    objetivo = 'definiçao de musculos'
                n = n + 1
                clienteE = TabelaExercicios(cliente.cpf, n) 

                semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']    #Dias que a academia "Normal" funciona
                semanaTreino = []               #Lista dos dias que o usuário vai treinar
                for dia in semana:          #criei a lista só com os dias que ele vai treinar
                    re = int(input(f'\nVai treinar na {dia}? \n|1| Sim \n|2| Não \n> '))
                    if re == 1:
                        treino = input('\nDigite o treino e a repetição desse dia, (exemplo: Perna, 15) \n> ')
                        semanaTreino.append(dia +': '+ treino)    #coloco o treino na mesma lista dos dias
                
                clienteE.fazerTabela(semanaTreino, objetivo)
                

            elif sistema == 2:
                tabelaAlterar = int(input('\nQual tabela você quer alterar? (Exemplo: Semana 1, digite (1)) \n> '))
                clienteE = TabelaExercicios(cliente.cpf, n)                
                r = int(input('\nQual objetivo do treino? \n|1| Esmagrecer \n|2| Ganhar massa muscular \n|3| Definir os muscuslos \n> '))
                if r == 1:
                    objetivo = 'Esmagrecer'
                elif r == 2:
                    objetivo = 'Ganhar massa muscular'
                elif r == 3:
                    objetivo = 'definiçao de musculos'

                semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']    #Dias que a academia "Normal" funciona
                semanaTreinoNova = []               #Lista dos dias que o usuário vai treinar
                for dia in semana:          #criei a lista só com os dias que ele vai treinar
                    re = int(input(f'\nVocê vai treinar na {dia}? \n|1| Sim \n|2| Não \n> '))
                    if re == 1:
                        treino = input('\nDigite o treino e a repetição desse dia, (exemplo: Perna, 15) \n> ')
                        semanaTreinoNova.append(dia +': '+ treino)    #coloco o treino na mesma lista dos dias
    
                
                clienteE.alterarTabela(tabelaAlterar, semanaTreinoNova, objetivo)


            elif sistema == 3:
                clienteE = TabelaExercicios(cliente.cpf, n)
                clienteE.verTabela() 

            else:
                print('\n>> Você digitou algo fora da lista dada, tente novamente! <<')
        
        elif sistemaPrincipal == 4:
            print('\nAté mais!')
            break

        else:
            print('\n>> Você digitou algo fora da lista dada, tente novamente! <<')
                
     except ValueError:
         print('\n>> Você digitou algo fora da lista dada, tente novamente! <<\n')
