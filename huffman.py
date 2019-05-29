import os, collections
import buildTree

print(" ")
print(" ")
print("Andre Luiz Lourenço de Andrade - 14/0016295")
print("Teoria da Informacao - Huffman Compressor")

print(" ")


####################################################################

#return string or file choosen to compress

def main():
	init()

def init():
	my_stringorfile = input("Please enter a string or file to compress >>> ")
	if my_stringorfile.find("-c") != -1:
		file = my_stringorfile.split()[1]
		print("You choose", file, "as file to be compressed...")
		readFile(file)
		return file 
	else:
		string = my_stringorfile
		readString(string)
		return string

#read string
def readString(string):
	print(" ")
	print("This function is not ready yet... Please choose a .txt file in your directory: " + os.getcwd())
	init()


#open and read file
def readFile(file):
	f = open(file, "rb")
	if f.mode == 'rb':
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
	proportions(dict, contentFile)
	#print(dict)
	return dict

def proportions(dictionary, contentFile):
	for key in dictionary:
		dictionary[key] /= len(contentFile)
		proportions = sorted(dictionary.values(), reverse=True)
	buildTree(proportions)
	return dictionary

def buildTree(proportions):
	root = build(proportions)
	#print(proportions)
	print(root)




main()

