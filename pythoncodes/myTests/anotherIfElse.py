idade = int(input("Por favor, digite sua idade: "))

print(f"Sua idade é {idade} anos.")

if idade >= 65:
    print("Você é idoso.")
elif idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")