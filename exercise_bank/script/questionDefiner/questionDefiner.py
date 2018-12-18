#! usr/bin/env python

class Instruction(object):
  def __init__ (self,description):
    self.description = description
  def show(self):
    print(self.description)


class Question(Instruction):
  def __init__(self,description, score = 1, number = 0):
    # initialise the description
    super(Question,self).__init__(description)
    self.response = None
    self.status = False
    self.score = score
    self.number = number

  def attempt(self):
    '''
    Prompt for input
    '''
    self.response = input('''
    ////////////////////////////////////
    Question %d
    -----------

    %s 
    
    Please key in your answer now:
    ''' % (self.number,self.description))
    return self.response

  
  def check(self):
    pass

  def feedback(self):
    if self.status:
      print("Correct!")
      return self.score
    else:
      print("Sorry this is not correct")
      return 0

  def run(self):
    self.attempt();
    self.check();
    return self.feedback();
    
    
      


class CodingQuestion(Question):
  '''
  coding checking questions
  '''

  def __init__(self,description,keyword, score = 1, number = 0):
    super(CodingQuestion,self).__init__(description, score)
    self.keyword = keyword

  def check(self):
    if(self.keyword in self.response):
      try:
        evaluation = eval(self.response)
        print('''
        => %s.
        ''' % evaluation)
        self.status = True
      except:
        pass
    else:
      pass



class QuestionBank():
  '''
  list of Questions
  '''

  def __init__(self,*args):
    self.questions = []
    self.total_score = 0
    self.score = 0
    questionCount = 0
    for arg in args:
      if issubclass(arg.__class__,Question):
        questionCount += 1
        self.questions += [arg]
        arg.number = questionCount 
        self.total_score += arg.score

    print("There are %d questions in this exercise" % questionCount)
  
  def get_score(self, passing_score = 60):

    score = self.score * 100/self.total_score
    print('''
    ------------
    Score report
    ------------
    ''')
    print("Your score is %1.1f%%" % score)

    if score >= passing_score:
      print("You have passed the quiz")
    else:
      print("You haven't passed the quiz")

    return score


  def run(self, resit_enabled = True, passing_score = 60):
    resit_questions = []
    for question in self.questions:

      score = question.run()
      self.score += score

      if score == 0:
        resit_questions += [question]

      self.questions = resit_questions
    
    isContinue = 'y'
    self.get_score(passing_score)

    while resit_enabled and (len(self.questions)>0) and (isContinue == 'y'):
      isContinue = input("Do you wish to try again? (y/n)  ").lower()

      if isContinue == 'y':
        self.run()
      else:
        break

    



    