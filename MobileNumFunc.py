def clean_phone_number(phone_number):
	"""
	This function accepts a phone number as input and cleans it
	by removing all non-numeric characters and adding an initial
	zero if it is missing.

	If the resulting phone number is not the correct length (11 digits),
	a ValueError is raised.

	Returns the cleaned phone number as a string.
	"""

	# Remove all non-numeric characters
	cleaned_number = ''.join(c for c in phone_number if c.isdigit())

	# Add an initial zero if it is missing
	if len(cleaned_number) == 10:
		cleaned_number = '0' + cleaned_number

	# Raise an error if the number is not the correct length
	if len(cleaned_number) != 11:
		raise ValueError('Invalid phone number')

	return cleaned_number


if __name__ == '__main__':
	phone_number = input('Please enter a phone number: ')
	cleaned_number = clean_phone_number(phone_number)
	print('The cleaned number is: {}'.format(cleaned_number))