#Everaldo: Só criei esse arquivo como teste, não interfere em nenhum dos outros arquivos
from classUsuario import Usuario
from exercicios import Exercicios
from financias import Financias

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
        if sistemaPrincipal == 2: #Nao ta funcionando como eu queria, nao ocorre o codigo do outro arquivo
            print('ola')   
            #from financias import Financias
            cliente = Financias()
            
     except ValueError:
        print('>> Você digitou algo fora da lista dada, tente novamente! <<')