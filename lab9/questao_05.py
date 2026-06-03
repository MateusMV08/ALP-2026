soma = 0
cont = 0
vezes = int(input("Quantidade de valores que deseja digitar:"))
while cont < vezes:
    cont += 1 
    num = int(input("Valor:"))
    soma += num
print(f"A soma dos valores é {soma}, {cont} números foram digitados e {soma/cont} é a média dos números digitados")