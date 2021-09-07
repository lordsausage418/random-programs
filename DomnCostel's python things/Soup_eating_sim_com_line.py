from time import sleep

#soup
soup = """
 \##############/
  \____________/"""

#list of soupy answers
soupyanswers = ["eat soup", "eat", "eat the soup", "soup"]
soupyanswerswithnosoup = ["eat soup", "eat", "eat the soup"]

#soupy functions
def eatsoup():
  print("U were dumb, the soup was poisoned, like all soup is, so u ded now")

def die():
  print("You die a soupy death, and ascend into the Eternal Sea, and meet Crab God, and rave.")
  print("                                     THE END.                                       ")

#the eating
print("Eat the soup.")
print(soup)
answer1 = 0
soupeaten = False

while answer1 not in soupyanswerswithnosoup: #loop of soup
  answer1 = input(">")

  if answer1 not in soupyanswers:
    print("Not an option you dumdum")
  else:
    if answer1 == "soup":
      print("soup") #soup
    else:
      soupeaten = True

#soupy death
if soupeaten:
  eatsoup() #consumption
  print("say \"die\" to ascend")
  answer2 = 0

  while answer2 != "die": #loop of soup 2: dead boogaloo
    answer2 = input(">")

    if answer2 != "die":
      print("Not an option you dumdum")
    else:
      die() #very dead
      sleep(3)
