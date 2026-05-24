
conta = 0
while True:
    print('1-Bebidas\n2-Comidas\n3-Fechar a conta')
    tipo = int(input('Qual item você deseja acessar?\n'))
    if tipo == 1:
        print('Cardápio de bebidas:\n1.Suco natural - R$4.50\n2.Bloxy cola - R$5.00\n3.Água - R$2.00\n4.Fechar a conta')
        bebida = int(input('Qual item você deseja escolher?\n'))
        if bebida == 1:
            conta += 4.50
        elif bebida ==2:
            conta += 5.00
        elif bebida ==3:
            conta += 2.00
        elif bebida ==4:
            print(f'sua conta deu um total de R${conta}')
            break
    elif tipo == 2:
        print('Cardápio de comidas:\n1.Pizza - R$40.00\n2.Hamburguer - R$18.00\n3.Fritas - R$12.00\n4.Fechar a conta')
        comida = int(input('Qual item você deseja escolher?\n'))
        if comida == 1:
            conta += 40.00
        elif comida ==2:
            conta += 18.00
        elif comida ==3:
            conta += 12.00
        elif comida ==4:
            print(f'sua conta deu um total de R${conta}')
            break
    elif tipo == 3:
        print(f'sua conta deu um total de R${conta}')
        break


