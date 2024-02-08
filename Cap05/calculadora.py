def calculator():
    print('Escola uma opção: ') 
    opcao = int(input('1. (Soma), \n 2. (Multiplição) \n 3. (Subtração) \n 4. (Divisão): '))
    if opcao == 1:
        primeiro_numero = int(input('Digite o primeiro numero: '))
        segundo_numero = int(input('Digite o segundo numero: '))
        print(primeiro_numero + segundo_numero)
    if opcao == 2:
        primeiro_numero = int(input('Digite o primeiro numero: '))
        segundo_numero = int(input('Digite o segundo numero: '))
        print(primeiro_numero * segundo_numero)
    if opcao == 3:
        primeiro_numero = int(input('Digite o primeiro numero: '))
        segundo_numero = int(input('Digite o segundo numero: '))
        print(primeiro_numero - segundo_numero)    
    if opcao == 4:
        primeiro_numero = int(input('Digite o primeiro numero: '))
        segundo_numero = int(input('Digite o segundo numero: '))
        print(primeiro_numero / segundo_numero)

calculator()

# def calculator2():
#     numeros = []

#     while True:
#         try:
#             numero = float(input('Digite um número (ou qualquer letra para encerrar): '))
#             numeros.append(numero)
#         except ValueError:
#             break

#     if not numeros:
#         print('Nenhum número fornecido.')
#         return

#     print('Escolha uma opção: ')
#     opcao = int(input('1. (Soma), \n 2. (Multiplicação) \n 3. (Subtração) \n 4. (Divisão): '))

#     if opcao == 1:
#         soma = sum(numeros)
#         print('O valor da soma é:', soma)
#     elif opcao == 2:
#         multiplicacao = 1
#         for numero in numeros:
#             multiplicacao *= numero
#         print('O valor da multiplicação é:', multiplicacao)
#     elif opcao == 3:
#         subtracao = numeros[0] - sum(numeros[1:])
#         print('O valor da subtração é:', subtracao)
#     elif opcao == 4:
#         try:
#             divisao = numeros[0]
#             for numero in numeros[1:]:
#                 divisao /= numero
#             print('O valor da divisão é:', divisao)
#         except ZeroDivisionError:
#             print('Erro: Divisão por zero.')
#     else:
#         print('Opção inválida')

# # Exemplo de uso
# calculator2()
