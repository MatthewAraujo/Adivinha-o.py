from random import randint
palpites = 0
computador = randint(0, 10)
acertou = False
print('Computador ja escolheu o número, tente adivinhar')
while not acertou:
    jogador = int(input('Qual é o seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador< computador:
            print('Um pouqinho mais')
        if jogador > computador:
            print('Um poquinho menos')
print(f'Acertou em {palpites} palpites')
