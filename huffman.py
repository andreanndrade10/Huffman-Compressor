import os, collections

print(" ")
print(" ")
print("Andre Luiz Lourenço de Andrade - 14/0016295")
print("Teoria da Informacao")

print(" ")
print(" ")

####################################################################

#return string or file choosen to compress

def main():
	init()

def init():
	my_stringOrFile = input("Please enter a string or file to compress >>> ")
	if my_stringOrFile.find("-c") != -1:
		file = my_stringOrFile.split()[1]
		print("You choose", file, "as file to be compressed...")
		readFile(file)
		return file 
	else:
		string = my_stringOrFile
		readString(string)
		return string

#read string
def readString(string):
	print(" ")
	print("This function is not ready yet... Please choose a .txt file in your directory: " + os.getcwd())
	init()


#open and read file
def readFile(file):
	f = open(file, "r", encoding="utf8")
	if f.mode == 'r':
		content = f.read()
		#print(content)
		dictionary(content)
		return content

def contentSize(contentFile):
	contentSize = len(contentFile)
	return contentSize


def dictionary(contentFile):
	dict = {}
	for i in contentFile:
		if i not in dict.keys():
			dict[i]=1
		else:
			dict[i]+=1
	print(dict)
	return dict


main()

