#print("Aqui seguirei executando meu Projeto Python para obter uma calculadora. Aguardem!!!")
operacao = input("""Inicie escolhendo a operação que deseja realizar!
Soma [1]
Subtração[2]
Multiplicação[3]
Divisão[4]

Digite sua escolha: """)

if operacao == "1":
    valor1 = input("Digite um valor para somar: ")
    valor2 = input('Digite um segundo valor para somar: ')
    somatotal = int(valor1) + int(valor2)
    print(f'O valor da soma dos valores é: {somatotal}')
elif operacao == "2":
    valor1 = input("Digite um valor para subtrair: ")
    valor2 = input('Digite um segundo valor para subtrair: ')
    subtotal = int(valor1) - int(valor2)
    print(f'O valor da subtracao dos valores é: {subtotal}')
elif operacao == "3":
    valor1 = input("Digite um valor para multiplicar: ")
    valor2 = input('Digite um segundo valor para multiplicar: ')
    multotal = int(valor1) * int(valor2)
    print(f'O valor da multiplicacao dos valores é: {multotal}')
elif operacao == "4":
    valor1 = input("Digite um valor para dividir: ")
    valor2 = input('Digite um segundo valor para dividir: ')
    divtotal = int(valor1) / int(valor2)
    print(f'O valor da subtracao dos valores é: {divtotal}')
else:
    print("Obrigado por utilizar nossa Calculadora Desenvolvida em Python!")