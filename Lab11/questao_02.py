import time
import random
while True:
    P = input("Quer fazer uma pergunta?\n")
    if P == "S" or P == "Sim" or P == "s" or P == "sim":
        Quest = input("Faça sua pergunta:\n")
        print("Deixe-me pensar.......")
        time.sleep(2)
        print("Estou quase.......")
        time.sleep(2)
        print("Já sei!")
        time.sleep(2)
        prob = random.randint(1, 10)
        if prob <=5:
            resposta='SIM'
        else:
            resposta='NÃO'
        print(resposta)
    else:
        break