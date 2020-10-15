import random


def generate_password(p_type, length=0):

	# Lists containing characters, numbers and symbols for password creation
	alpha_arr = [i for i in 'abcdefghijklmnopqrstuvwxyz']
	nums_arr = [str(i) for i in range(0, 10)]
	symbols = [i for i in '!$"#%&()*+-./:;<=>?@[^_{|}~']
	all_chars = alpha_arr + nums_arr + symbols

	# All characters shuffled for better randomized password
	shuffled = "".join(random.sample(all_chars, len(all_chars)))

	# Length of password
	generate_pass = []


	if p_type == "5dig": # Generate 5 digit codes
		length = 4
		while length >= 0:
			generate_pass.append(nums_arr[random.randint(0, len(nums_arr)-1)])
			length -= 1

	if p_type == "shortpass": # Password length of 8
		length = 7
		while length >= 0:
			generate_pass.append(shuffled[random.randint(0, len(shuffled)-1)])
			length -= 1

	if p_type == "longpass": # Password length of 20
		length = 19
		while length >= 0:
			generate_pass.append(shuffled[random.randint(0, len(shuffled)-1)])
			length -= 1

	if p_type == "custom": # Custom password with variable length

		while length >= 0:
			generate_pass.append(shuffled[random.randint(0, len(shuffled)-1)])
			length -= 1

	return "".join(generate_pass)


# Create a file for the created passwords
pass_file = open("password.txt", "a")


get_use = input("What is the password for? ")
account_name = input("What is the username? ")

print("\nPassword options:"
	  "\n	(5dig) 5 digit numeric code."
	  "\n	(shortpass) Random password with a length of 8"
	  "\n	(longpass) Random password with a length of 20"
	  "\n	(custom) Random password with a custom length")


user_input = input("\nEnter option: ")
info = "\n		" + str(get_use).title() + "\nAccount username:	" + str(account_name) + "\nPassword:			"

if user_input == "custom":

	user_input2 = input("Enter length: ")
	generated_pass = generate_password(user_input.lower(), int(user_input2))
	output = info + generated_pass

	print(output)
	pass_file.write(output)
else:
	generated_pass = generate_password(user_input.lower())
	output = info + generated_pass

	print(output)
	pass_file.write(output)

pass_file.write("\n-----------------------------------------")