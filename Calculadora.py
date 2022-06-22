
#Exercicios Aula 1
#Calculadora Básica


escolha = int(input("Digite:\n 1 para soma\n 2 para subtração \n 3 para divisao \n 4 para multiplicação:\n"))


if escolha==1:
    print("Voce escolheu soma")

    valorUm = int(input("Digite o primeiro valor:"))
    valorDois = int(input("Digite o segundo valor:"))

    soma = valorUm + valorDois
    print(f'A soma dos valores dados eh de {soma}')

elif escolha==2:
    print("Voce escolheu subtracao")

    valorUm = int(input("Digite o primeiro valor:"))
    valorDois = int(input("Digite o segundo valor:"))

    subtracao = valorUm-valorDois
    print(f'A subtracao dos valores dados eh de {subtracao}')

elif escolha==3:
    print("Voce escolheu divisao")

    valorUm = int(input("Digite o primeiro valor:"))
    valorDois = int(input("Digite o segundo valor:"))

    divisao = valorUm/valorDois
    resto = valorUm%valorDois
    print(f'A divisao dos valores dados eh de {divisao} e tem de resto {resto}')

elif escolha==4:
    print("Voce escolheu multiplicacao")

    valorUm = int(input("Digite o primeiro valor:"))
    valorDois = int(input("Digite o segundo valor:"))

    multiplicacao = valorUm*valorDois
    print(f'A multiplicacao dos valores dados eh de {multiplicacao}')

else:
    print ("Sair")
