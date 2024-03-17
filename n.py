##Guess the word
#print("What is the capital of france: ")
#capital = "paris"
#ms = "-" * len(capital)
#
#while "-" in ms:
#    print(ms)
#    letter = input("Enter a letter: ")
#    
#    for i in range (len(capital)):
#        if capital[i] == letter:
#            ms = ms[:i] + letter + ms[i + 1:]
#print("You win: " , capital)

def get_content(filename):
	f = open(filename)
	return f.read()

def create_user_dict(ml):
	md = {}
	for line in ml:
		line = line.strip().split(": ")
		md[line[0]] = line[1]	
	return md


def another_read(fname):
	with open(fname) as f:
		cnt = f.readlines()
	return cnt


def get_letters_count(mstr):
	md = {}
	for el in mstr:
		if el.isalpha():
			if el in md:
				md[el] += 1
			else:
				md[el] = 1
	return md

def word_count(mstr):
	ml = mstr.split()
	return len([el for el in ml if el.isalpha()])

def sentence_count(mstr):
	return len(mstr.split("."))

def sort_dict(md):
	ml = list(md.items())
	ml.sort(key=lambda x: x[1])
	return ml

def custom_write(f, mstr, data):
	f.write(mstr)
	f.write(data + "\n")
	f.write("___\n")

def write_into_file(fname):
	cnt = get_content("a.txt")
	letter = get_letters_count(cnt)
	sorted_list = sort_dict(letter)
	print(sorted_list)
	with open(fname, "w") as f:
		f.write("LETTERS COUNT:\n")
		f.write("___\n")
		for k, v in sorted_list:
			f.write(k + " " + str(v) + "\n")
		custom_write(f, "WORDS COUNT: ", str(word_count(cnt)))
		custom_write(f, "SENTENCE COUNT: ", str(sentence_count(cnt)))

		
write_into_file("results.txt")


