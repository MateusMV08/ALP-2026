while True:
    Resp = input("Você quer saber como manter uma pessoa ingênua ocupada por horas? S/N:\n")
    if Resp == "S" or Resp == "Sim" or Resp == "SIM" or Resp == "s" or Resp == "sim":
        continue
    elif Resp == "N" or Resp == "Não" or Resp == "não" or Resp == "NÃO" or Resp == "n":
        break
    else:
        print(f"{Resp} não é uma resposta válida de sim/não.")
        continue
print("Obrigado. Tenha um bom dia!")
