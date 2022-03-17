n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
media=(n1+n2)/2
reprovado=media<5.0
recuperaçao=media<=5.0 or media <= 6.9
aprovado=media<=7.0


if reprovado == True:
    print('Reprovado')
elif recuperaçao == True:
    print('Recuperação')
else:
    print('Aprovado')

print('Sua média foi de {:.1f} pontos.'.format(media))