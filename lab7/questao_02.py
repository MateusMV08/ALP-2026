#a) Contar quantos números ímpares o usuário digitou. 
N = int(input("Quantos números quer digitar?"))
contador = 1
impares = 0

while contador <= N:
    #coloquei pra variável "contador" somar toda vez que o usuário digitar um número, pois antes o usuário ficava digitando números infinitamente.
    contador += 1
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1

print(f"Quantidade de ímpares: {impares}")

#b) Somar 10 números digitados pelo usuário.
soma = 0
#adicionei uma variável "contador"
contador = 1
#coloquei pro "contador" checar se é "<=10" ao invés da "soma" e coloquei pra variável do "contador" somar a cada número do usuário.
while contador <= 10: 
    contador += 1 
    num = int(input("Digite um número para somar: "))
    soma += num
#por fim, fiz com que a soma dos 10 números fosse mostrada ao usuário.
print(f'A soma dos 10 números digitados é {soma}')

#c) Imprimir o maior número digitado pelo usuário
#troquei o "inf" por "-inf" se não o "inf" sempre seria o maior número.
maior = float('-inf')
#adicionei a variável "contador".
contador = 1
#coloquei pro "contador" checar se é "<=10" ao invés da "soma" e coloquei pra variável do "contador" somar a cada número do usuário.
while contador <= 10: 
    contador += 1 
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num
#formatei o print, e corrigi ele.
print(f'O maior número é, {maior}')





