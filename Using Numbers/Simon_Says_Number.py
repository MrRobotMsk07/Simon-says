import os
import time
import sys
import random

numbers_to_generate_from = list(range(0,8))
simon_questions_amount = 100

simon_says_list = []
for question in range (simon_questions_amount):
    chosen_number = random.choice(numbers_to_generate_from)
    simon_says_list.append(chosen_number)

    print('THERE ARE SOME NUMBERS YOU HAVE TO MEMORISE: {}'.format(simon_says_list))
    time.sleep(3)

    os.system('cls')

    for num in simon_says_list:
        student_answer = int(input('HI I AM SIMON PLEASE ENTER THE NUMBER I ASKED :'))

        if student_answer == num:
            print ('WELL DONE')
            continue

        else:
            print('WRONG NUMBER :( , GAME OVER !')
            print('YOUR SCORE IS: {0}'.format(question))
            sys.exit()