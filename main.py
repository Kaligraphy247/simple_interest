# Simple Interest Calculator TUI
import time, sys,os

def typingPrint(text):
    """ Displays text incessantly using the time.sleep() method """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) # 0.5 for half a second...

def simple_interest(p, r, t):"""
    ''' Calculates Simple Intrest , where 'p' = Principal, 'r' = Rate in % and 't' = Time'''
    interest = p * r * t / 100
    print(interest)"""

#simple_interest(1000, 5, 1)

typingPrint("Simple Interest Calculator\nEnter values for P as in Principal, R as in Rate, T as in Time\n")
principal = int(input("Enter principal: "))
rate = int(input("Enter rate: "))
time = int(input("Enter time (1 for one year):  "))
interest = principal * rate * time / 100
print(interest)