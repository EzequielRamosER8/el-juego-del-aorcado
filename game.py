import random
import os


def run():


 IMAGES  = [ ''' 
  + --- +
  |   |
      |
      |
      |
      |
========= ''' , '''
  + --- +
  |   | 
  O   |
      |
      |
      |
========= ''' , '''
  + --- +
  |   | 
  O   |
  |   |
      |
      |
========= ''' , '''
  + --- +
  |   |
  O   |
/ |   |
      |
      |
========= ''' , '''
  + --- +
  |   |
  O   |
/ | \ |
      |
      |
========= ''' , '''
  + --- +
  |   |
  O   |
/ | \ |
 /    |  
      |
========= ''' , '''
  + --- +
  |   |
  O   |
/ | \ |
 / \  |
      |
========= ''' ]

DB = ["C","PYTHON","JAVASCRIPT","JAVA","PHP"]


word = random.choice(DB)
space = ["_"] * len(word)
attemps = 6

while True:
    os.system("cls")
    for character in space:
        print(character, end=" ")
    print(IMAGES)[attemps]    
    letter = input("Elegi una letra: ").upper()

    foud = False
    for idx, character in enumerate(word):
        if character == letter:
            space[idx] = letter
            found = True

    if not found:
        attemps -= 1

    if "_" not in space:
        os.system("cls")
        print("Ganaste") 
        break
        imput()  

    if attemps == 0:
        os.system("cls")
        print("perdiste") 
        break
        imput()      

if __name__ == ' __main__':

    run() 