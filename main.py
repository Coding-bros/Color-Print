# Importing Random and Time (They are default modules so there is no need to download them)
import random
import time

# The input takes the value what you want to print
text = str(input('What do you want to print: '))

# This is the while loop, to make our code run forever
while True:
    print('\033[1;31;1m' + text)
    # Pauses for 0.1 sec to avoid spamming the system
    time.sleep(0.1)
    print('\033[1;32;1m' + text)
    time.sleep(0.1)
    print('\033[1;33;1m' + text)
    time.sleep(0.1)
    print('\033[1;34;1m' + text)
    time.sleep(0.1)
    print('\033[1;35;1m' + text)
    time.sleep(0.1)
    print('\033[1;36;1m' + text)
    time.sleep(0.1)
