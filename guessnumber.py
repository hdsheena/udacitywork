"""print 'Hello! What is your name?'
myname = input()
print 'Well, ' + myname + ', I am thinking of a number between 1 and 20.'
realnum = 4
print 'Take a guess.'
def TakeGuess:
	mynum = input()
	guess = 1
	if mynum == realnum:
		print "Good job, " + str(myname) + "! You guessed my number in " + str(guess) + " guesses!"
	elif mynum > realnum:
		guess = guess + 1
		print "Your guess is too high."
		print "Take a guess."
		
	elif mynum < realnum:
		guess = guess + 1
		print "Your guess is too low."
		print "Take a guess."
"""

#The actual source code:
# This is a guess the number game.
import random
guessesTaken = 0
print('Hello! What is your name?')
myName = raw_input()
lownum = 1
highnum = 20
number = random.randint(lownum, highnum)  #added these three lines and changed the one below to eliminat human error of forgetting edits
print('Well, ' + myName + ', I am thinking of a number between ' + str(lownum) + ' and ' + str(highnum) + '.')  
while guessesTaken < 6:
    print('Take a guess.') # There are four spaces in front of print.
    guess = raw_input()
    guess = int(guess)  # <--this line doesnt seem necessary in pyth 2.x except bryan made me change it from input() to raw_input and now it matters
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
else:   # i changed this to "else" instead of if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
