import random
import string

letter = False
number = True
symbol = False
length = 20

def choose(letters, numbercase, symbolcase):
    chosenOnes = ""

    if letters:
        chosenOnes += string.ascii_letters
    if numbercase:
        chosenOnes += string.digits 
    if symbolcase:
        chosenOnes += string.punctuation
    
    return chosenOnes
        
        
def generate(chosenStuff):
    result = ''.join(random.choice(chosenStuff) for i in range(length))
    return result

stuffchosen = choose(letter, number, symbol)
pwd = generate(stuffchosen)

print(pwd)
