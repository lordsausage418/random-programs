import random
print("Do I want to the stupid thing Im about to do?")
a = input("type hm to start\n")
run = True
while run == True:
    if a == "hm":
        print(random.choice(["Do it", "[softly] dont"]))
        b = input("Do you want to make another decision?y/n\n")
        if b == "y" or b == "Y":
          print("Ok here is ur answer")
        elif b == "n" or b == "N":
            break