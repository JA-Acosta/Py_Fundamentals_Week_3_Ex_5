'''
>>> JAAR
>>> 08/11/2023
>>> Practicing Fundamentals Program 17
>>> Version 1
'''

'''
>>> Creates a program that takes a file and copies all of it's contents to another file. The user then signs the file.
'''

import datetime

time = datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S')

def main() :
    with open('the_little_prince.txt', 'r') as story :
        with open('copy.txt', 'w') as copy :
            for line in story.readlines() :
                copy.write(line)
            copy.write(f'\n\n\tCopied by { input("Enter your name: ") } on { time }')

if __name__ == '__main__' :
    main()