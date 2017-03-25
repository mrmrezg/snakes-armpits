import random

def main():
	print "Guess a number between 1 and 100."
	randomnumber = random.randint(1,100)
	found = False
	while not found:
		userguess = input("Your Guess: ")
	if userguess == randomnumber:
				print "You got it!"
				found = True
	elif userguess > randomnumber:
				print "Guess Lower!"
	else:
		print "Guess Higher!"
	if __name__ == '__main__':
		main()