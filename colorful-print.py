# Importing Random and Time (They are default modules so there is no need to download them)
import random
import time

# This loops out code forever
while 1:
    # declaring a as 1
    a = 1

    # checks if a is 1, if yes, then it prints the text in Red colour
    if a == 1:
        print('\033[1;31;1mcolorful')
        # declares a as 2
	    a = 2
        # Pauses for 0.1 sec to avoid spamming the system
	    time.sleep(0.1)

    # checks if a is 2, if yes, then it prints the text in Green colour
    if a == 2:
        print('\033[1;32;1mcolorful')
        # declares a as 3
	    a = 3
        # Pauses for 0.1 sec to avoid spamming the system
	    time.sleep(0.1)

    # checks if a is 3, if yes, then it prints the text in Yellow colour
    if a == 3:
        print('\033[1;33;1mcolorful')
        # declares a as 4
	    a = 4
        # Pauses for 0.1 sec to avoid spamming the system
	    time.sleep(0.1)

    # checks if a is 4, if yes, then it prints the text in Blue colour
    if a == 4:
        print('\033[1;34;1mcolorful')
        # declares a as 5
	    a = 5
         # Pauses for 0.1 sec to avoid spamming the system
	    time.sleep(0.1)

    # checks if a is 5, if yes, then it prints the text in Purple colour
    if a == 5:
        print('\033[1;35;1mcolorful')
	    # declares a as 6
        a = 6
        # Pauses for 0.1 sec to avoid spamming the system
	    time.sleep(0.1)

    # checks if a is 6, if yes, then it prints the text in Cyan colour
    if a == 6:
        print('\033[1;36;1mcolorful')
        # declares a as 1 to loop this program
	    a = 1
        # Pauses for 0.1 sec to avoid spamming the system
	    time.sleep(0.1)
