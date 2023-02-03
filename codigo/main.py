from classUsuario import Usuario
from classExercicios import TabelaExercicios
from classFinancias import Financias


while True:
     cpf = input('- Seja bem vindo ao sistema, por favor digite o CPF do cliente> ')
     cliente = Usuario(cpf)
     print(' ')
     try:
        sistemaPrincipal = int(input('Para que area do sistema deseja se dirigir...CADASTROS[1], FINANCIAS[2], TABELAS[3]>>>')) 
        if sistemaPrincipal == 1:
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
            else:
                print('>> Você digitou algo fora da lista dada, tente novamente! <<')
        elif sistemaPrincipal == 2: #Nao ta funcionando como eu queria, nao ocorre o codigo do outro arquivo 
                
            clienteF = Financias(cliente.cpf)
            sistema = int(input('O que deseja fazer... \n[1] Dar baixa na fatura\n[2] Dar baixa em uma taxa\n>'))
                
            if sistema == 1:
                mes = int(input('digite o numero do mes 1, 2, 3...>'))
                valor = float(input('Informe o valor da mensalidade>'))
                clienteF.darBaixaFatura(mes, valor)

            elif sistema == 2:
                valorT = float(input('Informe o valor da taxa>'))
                clienteF.darBaixaTaxa(valorT)
        

        elif sistemaPrincipal == 3: ##########################################################################
            sistema = int(input('O que deseja fazer... \n|1| Fazer tabela de exercício \n|2| Alterar tabela de exercício \n|3| Ver tabela de exercício \n'))
            codigo = int(input('Digite código da conta> '))
            clienteE = TabelaExercicios(codigo, cliente.cpf)

                

            if sistema == 1:
                print('OBJETIVO...|Esmagrecer(1)|-|Ganhar massa muscular(2)|-|Definir os muscuslos(3)|')
                objetivo = ''
                r = int(input('>'))
                if r == 1:
                    objetivo = 'Esmagrecer'
                elif r == 2:
                    objetivo = 'Ganhar massa muscular'
                elif r == 3:
                    objetivo = 'definiçao de musculos'

                while True:
                    diaSemana = int(input('Dia da semana do treino: \n|1| Segunda \n|2| Terça \n|3| Quarta \n|4| Quinta \n|5| Sexta\n|0| FINALIZAR\n'))
                    if diaSemana == 0:
                        clienteE.fazerTabela(diaSemana, "NADA", objetivo)
                        break
                    else:
                        treino = input('Treino e repetição do dia: ')
                        clienteE.fazerTabela(diaSemana, treino, objetivo)
     except ValueError:
         print('>> Você digitou algo fora da lista dada, tente novamente! <<')

     