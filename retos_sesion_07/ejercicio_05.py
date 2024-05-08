# Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome la frase o palabra ejemplo "Anita lava la Tina" es verdad

frase = input("Escriba una cadena o frase: ").lower().replace(" ", "")
print(frase)

frase_inv = frase[-1::-1].lower()
print(frase_inv)

print("La cadena o frase es palindromo?,", frase == frase_inv)