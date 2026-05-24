import random
chances = 5
num_secreto = (random.randint(1, 10))
while chances > 0: 
    num = int(input(f"Qual o número secreto? Você tem {chances} chances:"))
    chances -= 1
    if num == num_secreto:
        print("Você acertou o número secreto, parabéns 🔥🎱")
        break
