frase = "Curso em Video Python"
print(frase) # printa a string inteira
print(frase[9]) # printa o caractere na posição 9
print(frase[9:21]) # printa os caracteres da posição 9 até a 21
print(frase[9:21:2]) # printa os caracteres da posição 9 até a 21, pulando de 2 em 2
print(frase[:5]) # printa os caracteres do início até a posição 5
print(frase[15:]) # printa os caracteres da posição 15 até o final
print(frase[9::3]) # printa os caracteres da posição 9 até o final, pulando de 3 em 3
print(len(frase)) # printa o tamanho da string
print(frase.count('o')) # conta quantas vezes aparece a letra "o" minúscula
print(frase.count('o', 0, 13)) # conta quantas vezes aparece a letra "o" minúscula do início até a posição 13
print(frase.find('deo')) # encontra a posição da substring "deo"
print(frase.find('Android')) # retorna um valor negativo se a string não for encontrada
print('Curso' in frase) # verifica se a palavra "Curso" está na string e retorna um valor booleano
print(frase.replace('Python', 'Android')) # substitui "Python" por "Android"
print(frase.upper()) # transforma toda a string em maiúsculas
print(frase.lower()) # transforma toda a string em minúsculas
print(frase.capitalize()) # transforma a primeira letra da string em maiúscula
print(frase.title()) # transforma a primeira letra de cada palavra em maiúscula
print(frase.strip()) # remove espaços no início e no final da string
print(frase.rstrip()) # remove espaços no final da string
print(frase.lstrip()) # remove espaços no início da string
print(frase.split()) # divide a string em uma lista de palavras
print('-'.join(frase)) # junta os caracteres da string com um hífen entre eles