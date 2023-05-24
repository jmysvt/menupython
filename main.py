print("-" * 54)
print(
  "Seja bem vindo ao nosso menu, One Week At The Python! Com base no seu número inteiro, escolha a opção que desejar!!"
)
print("-" * 54)

numint = (int(input("Digite um número inteiro:")))

print("-" * 54)
print("""Escolha um dos seguintes cálculos:
[1] Conversão de decimal para as bases binário e octadecimal.
[2] Conversão das bases binário e octadecimal para decimal.
[3] Calculadora aritmética de binários, que contemple  as operações de soma e subtração."""
      )
print("-" * 54)

opnum = int(input("Digite a sua escolha:"))

if opnum == 1:
  print("{} Em decimal convertido para binário é: {}".format(
    numint, bin(numint)))

if opnum == 1:
  print("{} Em decimal convertido para octadecimal é: {}".format(
    numint, oct(numint)))