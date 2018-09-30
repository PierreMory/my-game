#!/usr/bin/env python
# -*-coding:Utf-8 -*

from random import randint

random_number = randint(1, 100)

print "The program chose an integer between 1 and 100. Can you guess its value?"

success = False
steps = 1

while not success:
    try:
        proposed_value = int(raw_input("Try a number: "))
    except ValueError:
        print "Please enter an integer"
        continue
    if proposed_value == random_number:
        success = True
        print "Well done! You win in %s step(s)!" % steps
        break
    else:
        if proposed_value > random_number:
            print "Program: -"
        else:
            print "Program: +"
        steps += 1
