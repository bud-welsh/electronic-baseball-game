import random

play = round(random.random(), 3)

inning_number = 1

visiting_single = .333

home_single = .250

def visiting_inning(finning):
  return print("It's the top of inning number " + str(finning))

visiting_inning(inning_number)