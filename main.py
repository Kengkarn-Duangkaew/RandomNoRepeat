from random import randint, seed
from datetime import datetime
import termcolor
import os

def randomTest():
    os.system('color')
    person = 0
    count = 0
    num_arr = []
    max_Random = int(input("Total number of people: "))
    while (True):
        if (count != 2):
            txt = input()
            person += 1
        if (txt == ""):
            seed(datetime.now().microsecond)
            if (person == max_Random + 1):
                break
            if (count != 2):
                print("Person " + str(person), end="")
            count = 0
            num = randint(1, max_Random)
            num_arr.append(num)
            for i in num_arr:
                if (num == i):
                    count += 1
                    if (count == 2):
                        num_arr.remove(num)
            # print(num_arr)
            if (count != 2):
                print(" ---> Number: " + termcolor.colored(str(num), 'blue'))
                print()
        else:
            break
randomTest()