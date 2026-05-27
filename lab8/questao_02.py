cont = 5
while cont > 0: 
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0: 
        continue
    print(f'{num} é um número ímpar')
#Quando você digita um número ímpar, o código roda o "print" e volta pro "while", porém quando vc digita um número par, ele apenas volta pro While.