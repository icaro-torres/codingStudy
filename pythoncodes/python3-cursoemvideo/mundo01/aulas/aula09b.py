frase = """This is a very long string that
spans multiple lines.
It preserves all the line breaks and
indentation as written.""" # se você colocar três aspas, o Python entende que é uma string longa, as aspas podem ser simples ou duplas

print(frase.lower().find('it'))  # converte a string para minúsculas e procura por ela, retornando a posição