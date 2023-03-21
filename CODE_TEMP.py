print("Conversor de Temperatura")

# solicita a temperatura e a unidade de medida
temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade de medida (C ou F): ")

# converte de Celsius para Fahrenheit
if unidade == "C":
    fahrenheit = (temperatura * 9/5) + 32
    print(temperatura, "graus Celsius correspondem a", fahrenheit, "graus Fahrenheit.")
# converte de Fahrenheit para Celsius
elif unidade == "F":
    celsius = (temperatura - 32) * 5/9
    print(temperatura, "graus Fahrenheit correspondem a", celsius, "graus Celsius.")
# exibe uma mensagem de erro se a unidade de medida não for reconhecida
else:
    print("Unidade de medida inválida.")
