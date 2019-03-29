#Python has a module called time, which I use here to define my own function 'pause'#
import time
#Here I define my function, the 'p' is a variable which I use to make it possible to add any delay you want.#
def pause(p = 1):
  time.sleep(p)
#Here I will import the random module, which lets me generate random numbers.#
import random
#Using random, I can create a random delay by combining both time and random. I will define a new function. It has two parameters, min and max, which will be the minimum and maximum numbers to choose from.#
def randpause(min = 1, max = 2):
  time.sleep(random.randint(min, max))
#Here I will show the functions being used, and how to change the parameters.#
print('Pause after this')
pause(p = 2)
#This will make a 2 second delay, instead of the one second, if you want to keep the pause function at one second, just type "pause()".#
print('Random pause after this')
randpause(min = 1, max = 10)
print('Pauses complete')
