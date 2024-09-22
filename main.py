def organization(texto, user_input):

	alphabet = {
		"a": "a",
		"b": "b",
		"c": "c",
		"d": "d",
		"e": "e",
		"f": "f",
		"g": "g",
		"h": "h",
		"i": "i",
		"j": "j",
		"k": "k",
		"l": "l",
		"m": "m",
		"n": "n",
		"o": "o",
		"p": "p",
		"q": "q",
		"r": "r",
		"s": "s",
		"t": "t",
		"u": "u",
		"v": "v",
		"w": "w",
		"x": "x",
		"y": "y",
		"z": "z"
	}

	texto_compl = ""
	alpha_check = user_input.isalpha()
	lowered_input = user_input.lower()
	

	if lowered_input == "all":

		contador_letras = letters_counted(texto)
		sorted_letras = sorted(contador_letras.keys())

		for letra in sorted_letras:
			numero = contador_letras.get(letra)
			frase = "The letter {} appears {} times.".format(letra, numero)
			texto_compl += frase + "\n"
		print(texto_compl)
	
	elif lowered_input == "none":
		pass

	elif alpha_check:
		if len(lowered_input) == 1:
			if lowered_input in alphabet:
				l_counted = letters_counted(texto)
				number = l_counted.get(alphabet[lowered_input])
				print(f"The letter {lowered_input} appears {number} times.\n")

	else:
		raise Exception("Invalid input. Please select one of the options above")


def main():
	book_path = "BookBot/bookbot/Shrek.txt"
	livro = get_book_text(book_path)
	checker_palavras = input("Do you wish to see how many words this script contain in total? (y/n)\n")
	checker_letras = input('''Letters counter:
	None - No letters.
	All - All letters.
	Single letter from A to Z - That letter count.
						
	Answer here: ''')
	print("\n--- Begin report of Shrek Script ---\n")

	palavras_contadas(livro, checker_palavras)
	organization(livro, checker_letras)


	print("\n--- End report ---")


def get_book_text(path):
	with open(path) as f:
		return f.read()


def palavras_contadas(texto, user_input):
	if user_input == "n":
		return None
	elif user_input == "y":
		numero = len(texto.split())
		print(f"{numero} words found in the document\n")
	else:
		raise Exception("Invalid answer! Choose yes or no.")


def letters_counted(texto):
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