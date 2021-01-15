import time, sys,os

def typingPrint(text):
    """ Displays text incessantly using the time.sleep() method """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03) # 0.5 for half a second...

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()  
    return value

def clearScreen():
    os.system("cls")
    

typingPrint("hello world...\n")
time.sleep(1)
typingPrint("You've entered the Matrix!\n")
time.sleep(1)
name = typingInput("what is your name: \n")
typingPrint(name)

# DRAMATICALLY CLEARS THE SCREEN...
typingPrint("\nThis screen will clear itself in 3..")
time.sleep(1)
typingPrint("2..")
time.sleep(1)
typingPrint("1..")
time.sleep(1)
clearScreen()

print("\nordinary sample text")