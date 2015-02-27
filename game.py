import os.path
import sys
from dependencies import *

gamestatuscheck()

if os.path.exists('save.py') == True:
        from save import *
        typefast('Save data detected, save loaded\n')
        file = open('save.py', 'r+')
elif os.path.exists('save.py') == False:
        file = open('save.py', 'w')
        type('Making new character\n')
        newchar = 1
        file.write("newchar = 1\n")




if newchar == 1:
        type("What is your name?\n>")
        name = raw_input()
        file.write("name = '%s' \n" % str(name))
        x = 'a'
        while x == 'a':
                typefast("Choose class 1, 2, or 3. Assasain, Mercenary, or Summoner\n>")
                jobt = raw_input()
                if intcheck(jobt) == True:
                        jobt = int(jobt)
                        x = 'c'
                else:
                        typefast("Invalid input\n")

        file.write("jobt = %s \n" % str(jobt))
        story1 = 1
        file.write("story1 = 1\n")
        newchar = 0
        file.write('newchar = 0\n')

#import stories from different .py to continue story











