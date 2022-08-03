import random

play = round(random.random(), 3)

inning_number = 1

visiting_single = .333

home_single = .250

# def visiting_inning(finning):
  # return print("It's the top of inning number " + str(finning))

def visiting_inning():
  if play < visiting_single:
    return print("HIT")
  return print("OUT")

visiting_inning()

# visiting_inning(inning_number)

