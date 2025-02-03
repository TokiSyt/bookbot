import string
alphabet = {letter: letter for letter in string.ascii_lowercase}


def organization(text, user_input):
	if user_input == "all":

		total_letters = letters_counted(text)
		sorted_letters = dict(sorted(total_letters.items()))

		for letter in alphabet:
			letter_amount = sorted_letters.get(letter, 0)
			if letter == "z":
				print(f"The letter {letter} appears {letter_amount} times.")
			else:
				print(f"The letter {letter} appears {letter_amount} times.\n")

	elif user_input in alphabet:
			l_counted = letters_counted(text)
			number = l_counted.get(alphabet[user_input])
			print(f"The letter {user_input} appears {number} times.")


def words_option():
	while True:
		try:
			checker_words = input("Do you wish to see how many words this script contain in total? (y/n)\n")
			if checker_words in ["y", "n"]:
				return checker_words
			else:
				print('Please enter "y" or "n".')
		except:
			print("Enter a valid answer.")


def letters_option():
	while True:
		try:
			checker_letters = input('''\nRegarding a letters count, how my letters do you wish to see:
	Zero - No letters.
	All - All letters.
	Single letter from A to Z - That letter count.
						
	Answer here: ''')
			if (checker_letters.lower() in alphabet and len(checker_letters) == 1) or checker_letters.lower() in ["zero", "all"]:
				return checker_letters.lower()
			else:
				print('Please enter Zero, All or a single letter from the alphabet.')
		except:
			print("Enter a valid answer from the options below.")


def get_book_text(path):
	with open(path) as f:
		return f.read()


def main():
	book_path = "shrek.txt"
	book = get_book_text(book_path)
	checker_words = words_option()
	checker_letters = letters_option()

	print("\n--- Begin report of Shrek Script ---\n")

	if checker_words == "y":
		counted_words(book)
	elif checker_words == "n" and checker_letters != "zero":
		print("Words count display skipped.\n")
	
	if checker_letters != "zero":
		organization(book, checker_letters)
	elif checker_letters == "zero" and checker_words == "y":
		print("Letters count display skipped.")

	if checker_words == "n" and checker_letters == "zero":
		print("No information to print.")

	print("\n--- End report ---")


def counted_words(text):
	words_amount = len(text.split())
	print(f"{words_amount} words found in the selected document.\n")


def letters_counted(text):
	lowered_string = text.lower()
	letters_counter = {}
	for char in lowered_string:
		if char.isalpha():
			letters_counter[char] = letters_counter.get(char, 0) + 1
	return letters_counter


main()
