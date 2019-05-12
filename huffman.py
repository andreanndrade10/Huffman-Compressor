print(" ")
print(" ")
print("Andre Luiz Lourenço de Andrade - 14/0016295")
print("Teoria da Informacao")

print(" ")
print(" ")
####################################################################

#return string or file choosen
def init():
	my_stringOrFile = input("Please enter a string or file to compress >>> ")
	if my_stringOrFile.find("-c") != -1:
		file = my_stringOrFile.split()[1]
		print("You choose", file, "as compress file")
		return file 
	else:
		string = my_stringOrFile
		return string



