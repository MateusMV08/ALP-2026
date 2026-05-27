O código a seguir gera um número aleatório entre 1 e 10. Complete o código dando 5 chances para o usuário acertar, mas:
Se o usuário digitar um número fora do intervalo 1 a 10, use continue para ignorar essa tentativa (não conta como chance perdida).
Se acertar, dê parabéns e use break para sair do loop.
import random
secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input("Adivinhe o número (1 a 10): "))
    # Complete aqui

