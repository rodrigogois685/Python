'''import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime('%Y')'''

atual=int(input('Digite o ano atual: '))
ano=int(input('Informe seu ano de nascimento: '))
idade_atual=atual-ano

futuro=idade_atual<18
presente=idade_atual==18

if futuro==True:
    print('Terá que se alistar quando chegar aos 18 anos')
elif presente==True:
    print('Chegou a hora de se alistar ao Exército Brasileiro!')
else:
    print('Já passou o tempo de se alistar, caso não tenha se alistado.')