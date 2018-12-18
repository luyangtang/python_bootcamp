#! usr/bin/env python

from script.questionDefiner.questionDefiner import *

'''
Testing:

7 * 6
8 % 3
7 == 3
print("Hello world")

'''

welcoming_msg = '''
Welcome to the Python bootcamp! 

In this section we will warm ourselves up for the upcoming challenges. 

Feel free to skip this section if you have already got some coding experience.

In this section we will be covering some basic operations, for each question you will just need to write a line of code that meets the requirement. Note that this is a marked exercise and your scores will be submitted. However you can attempt as many times as you wish.

For example, a sample question may be

"Substract a number from another."

In the console you will probably want to type

> 8 - 9

This will show a correct answer. 

> 8 + (10 - 2)

Also great!

> 2 -

Ooops you will get an error message if the expression does not evaluate.

Steady, ready, go!
==================
'''





def warm_up_exercise():
  welcomeInstr = Instruction(welcoming_msg)
  welcomeInstr.show()

  multiplication = CodingQuestion("Multiple a number with another number","*",10)

  modulo = CodingQuestion("Find the remainder of dividing a number by another","%",10)

  logical_operator = CodingQuestion("Check if two numbers are equal.", "==",10)

  string_literal = CodingQuestion("Use print() to print out something. Hint: check help(print) if you are stuck", "print",10)

  list_literal = CodingQuestion("Type a list literal here ", "[",10)

  questionBank = QuestionBank(multiplication,modulo,logical_operator,string_literal,list_literal)

  
  questionBank.run(passing_score = 80)
  