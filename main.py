def organization(texto):
	contador_letras = letras_contadas(texto)
	sorted_letras = sorted(contador_letras.keys())

	for letra in sorted_letras:
		numero = contador_letras.get(letra)
		frase =  "The letter {} appears {} times.".format(letra, numero)
		print(frase)

def main():
	book_path = "books/frankenstein.txt"
	livro = get_book_text(book_path)
	print("--- Begin report of books/frankenstein.txt ---\n")
	print(palavras_contadas(livro), "words found in the document\n")
	organization(livro)
	print("\n--- End report ---")

def get_book_text(path):
	with open(path) as f:
		return f.read()
	
def palavras_contadas(texto):
	numero = texto.split()
	return len(numero)

def letras_contadas(texto):
	lowered_string = texto.lower()
	contador_letras = {}
	for char in lowered_string:
		if char.isalpha():
			if char in contador_letras:
				contador_letras[char] += 1
			else:
				contador_letras[char] = 1
	return contador_letras

main()