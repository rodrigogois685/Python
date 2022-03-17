###Empréstimo Bancário###

casa=float(input('Digite o valor da casa: '))

salario=float(input('Digite o valor que você recebe mensal: '))

anos_pagar=int(input('Digite o número de anos e que essa compra seria parcelada: '))

trinta_percent=(salario*3)/10

prestação=float(casa/(anos_pagar*12)) #vezes doze porque 'casa' tá em anos

if prestação > trinta_percent:
    print('O empréstimo foi negado')

else:
    print('A solicitação foi aceita!')
    print('O valor da prestação será {:.2f}'.format(prestação))

