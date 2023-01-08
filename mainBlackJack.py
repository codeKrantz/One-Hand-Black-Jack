import random
import time

#END OF IMPORTS

CardNames = ["ace","two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "Jack", "Queen",  "King"]
CardValues = [0,2,3,4,5,6,7,8,9,10,11,12,13]
# 11 is a Jack, 12 is a Queen, and 13 is a King

#END OF LISTS

UserHandValues = [] # is handnumbers and list
UserCardNames = [] # is hand 
UserHandValueNumber = 0 # is HandValue
DealerHandValues = []
DealerCardNames = []
DealerHandValueNumber = 0

# END OF PLAYER AND DEALER LISTS

print("""Welcome to one hand Black Jack!

The rules are simple. Try to beat the dealers hand without going over 21 by asking for more cards or keeping the cards you have.

Aces can be 1 or 11 and all face cards are worth 10.

Good Luck
 """)
time.sleep(8) #CHANGE TO 8!!!

UserFirstCard = random.choice(CardNames)
UserCardNames.append(UserFirstCard)

if UserFirstCard == "ace":
  UserHandValues.append("0")
elif UserFirstCard== "two":
  UserHandValues.append("2")
elif UserFirstCard == "three":
  UserHandValues.append("3")
elif UserFirstCard== "four":
  UserHandValues.append("4")
elif UserFirstCard== "five":
  UserHandValues.append("5")
elif UserFirstCard== "six":
  UserHandValues.append("6")
elif UserFirstCard== "seven":
  UserHandValues.append("7")
elif UserFirstCard== "eight":
  UserHandValues.append("8")
elif UserFirstCard== "nine":
  UserHandValues.append("9")
elif UserFirstCard== "ten":
  UserHandValues.append("10")
elif UserFirstCard == "Jack":
  UserHandValues.append("11")
elif UserFirstCard == "Queen":
  UserHandValues.append("12")
elif UserFirstCard =="King":
  UserHandValues.append("13")

UserHandValueNumber= 0
for card in UserHandValues:
  if card == "0":
    if UserHandValueNumber+ 1 > 21:
      print("Bust")
    elif UserHandValueNumber<= 10:
      UserHandValueNumber= (UserHandValueNumber+ 11)
    else:
      UserHandValueNumber= (UserHandValueNumber+ 1)
  elif card == "2":
    UserHandValueNumber= (UserHandValueNumber+ 2)
  elif card == "3":
    UserHandValueNumber= (UserHandValueNumber+ 3)
  elif card == "4":
    UserHandValueNumber= (UserHandValueNumber+ 4)
  elif card == "5":
    UserHandValueNumber= (UserHandValueNumber+ 5)
  elif card == "6":
    UserHandValueNumber= (UserHandValueNumber+6)
  elif card == "7":
    UserHandValueNumber= (UserHandValueNumber+ 7)
  elif card == "8":
    UserHandValueNumber= (UserHandValueNumber+ 8)
  elif card == "9":
    UserHandValueNumber= (UserHandValueNumber+ 9)
  else:
    UserHandValueNumber= (UserHandValueNumber + 10)

# KEEP THINGS OUSIDE OF DEF'S FOR SOME REASON!

UserSecondCard = random.choice(CardNames)
UserCardNames.append(UserSecondCard)

if UserSecondCard == "ace":
  UserHandValues.append("0")
elif UserSecondCard== "two":
  UserHandValues.append("2")
elif UserSecondCard == "three":
  UserHandValues.append("3")
elif UserSecondCard== "four":
  UserHandValues.append("4")
elif UserSecondCard== "five":
  UserHandValues.append("5")
elif UserSecondCard== "six":
  UserHandValues.append("6")
elif UserSecondCard== "seven":
  UserHandValues.append("7")
elif UserSecondCard== "eight":
  UserHandValues.append("8")
elif UserSecondCard== "nine":
  UserHandValues.append("9")
elif UserSecondCard== "ten":
  UserHandValues.append("10")
elif UserSecondCard == "Jack":
  UserHandValues.append("11")
elif UserSecondCard == "Queen":
  UserHandValues.append("12")
elif UserSecondCard =="King":
  UserHandValues.append("13")

UserHandValueNumber= 0
for card in UserHandValues:
  if card == "0":
    if UserHandValueNumber+ 1 > 21:
      print("Bust")
    elif UserHandValueNumber<= 10:
      UserHandValueNumber= (UserHandValueNumber+ 11)
    else:
      UserHandValueNumber= (UserHandValueNumber+ 1)
  elif card == "2":
    UserHandValueNumber= (UserHandValueNumber+ 2)
  elif card == "3":
    UserHandValueNumber= (UserHandValueNumber+ 3)
  elif card == "4":
    UserHandValueNumber= (UserHandValueNumber+ 4)
  elif card == "5":
    UserHandValueNumber= (UserHandValueNumber+ 5)
  elif card == "6":
    UserHandValueNumber= (UserHandValueNumber+6)
  elif card == "7":
    UserHandValueNumber= (UserHandValueNumber+ 7)
  elif card == "8":
    UserHandValueNumber= (UserHandValueNumber+ 8)
  elif card == "9":
    UserHandValueNumber= (UserHandValueNumber+ 9)
  else:
    UserHandValueNumber= (UserHandValueNumber + 10)

print("""
You will now be delt two cards.
""")
time.sleep(2)
print("Here are your cards"+str(UserCardNames))

print("Here is your hand's current total "+str(UserHandValueNumber))
print(" ")
time.sleep(4)


#now for the dealer to get some cards
DealerFirstCard = random.choice(CardNames)
DealerCardNames.append(DealerFirstCard)


if DealerFirstCard == "ace":
  DealerHandValues.append("0")
elif DealerFirstCard== "two":
  DealerHandValues.append("2")
elif DealerFirstCard == "three":
  DealerHandValues.append("3")
elif DealerFirstCard== "four":
  DealerHandValues.append("4")
elif DealerFirstCard== "five":
  DealerHandValues.append("5")
elif DealerFirstCard== "six":
  DealerHandValues.append("6")
elif DealerFirstCard== "seven":
  DealerHandValues.append("7")
elif DealerFirstCard== "eight":
  DealerHandValues.append("8")
elif DealerFirstCard== "nine":
  DealerHandValues.append("9")
elif DealerFirstCard== "ten":
  DealerHandValues.append("10")
elif DealerFirstCard == "Jack":
  DealerHandValues.append("11")
elif DealerFirstCard == "Queen":
  DealerHandValues.append("12")
elif DealerFirstCard =="King":
  DealerHandValues.append("13")

DealerHandValueNumber= 0
for card in DealerHandValues:
  if card == "0":
    if DealerHandValueNumber+ 1 > 21:
      print("Bust")
    elif DealerHandValueNumber<= 10:
      DealerHandValueNumber= (DealerHandValueNumber+ 11)
    else:
      DealerHandValueNumber= (DealerHandValueNumber+ 1)
  elif card == "2":
    DealerHandValueNumber= (DealerHandValueNumber+ 2)
  elif card == "3":
    DealerHandValueNumber= (DealerHandValueNumber+ 3)
  elif card == "4":
    DealerHandValueNumber= (DealerHandValueNumber+ 4)
  elif card == "5":
    DealerHandValueNumber= (DealerHandValueNumber+ 5)
  elif card == "6":
    DealerHandValueNumber= (DealerHandValueNumber+6)
  elif card == "7":
    DealerHandValueNumber= (DealerHandValueNumber+ 7)
  elif card == "8":
    DealerHandValueNumber= (DealerHandValueNumber+ 8)
  elif card == "9":
    DealerHandValueNumber= (DealerHandValueNumber+ 9)
  else:
    DealerHandValueNumber= (DealerHandValueNumber + 10)
print(" ")
print("Here is the Dealer's first card."+str(DealerCardNames))
print(DealerHandValueNumber)
time.sleep(4)

DealerSecondCard = random.choice(CardNames)
DealerCardNames.append(DealerSecondCard)

if DealerSecondCard == "ace":
  DealerHandValues.append("0")
elif DealerSecondCard== "two":
  DealerHandValues.append("2")
elif DealerSecondCard == "three":
  DealerHandValues.append("3")
elif DealerSecondCard== "four":
  DealerHandValues.append("4")
elif DealerSecondCard== "five":
  DealerHandValues.append("5")
elif DealerSecondCard== "six":
  DealerHandValues.append("6")
elif DealerSecondCard== "seven":
  DealerHandValues.append("7")
elif DealerSecondCard== "eight":
  DealerHandValues.append("8")
elif DealerSecondCard== "nine":
  DealerHandValues.append("9")
elif DealerSecondCard== "ten":
  DealerHandValues.append("10")
elif DealerSecondCard == "Jack":
  DealerHandValues.append("11")
elif DealerSecondCard == "Queen":
  DealerHandValues.append("12")
elif DealerSecondCard =="King":
  DealerHandValues.append("13")

DealerHandValueNumber= 0
for card in DealerHandValues:
  if card == "0":
    if DealerHandValueNumber+ 1 > 21:
      print("Bust")
    elif DealerHandValueNumber <= 10:
      DealerHandValueNumber= (DealerHandValueNumber+ 11)
    else:
      DealerHandValueNumber= (DealerHandValueNumber+ 1)
  elif card == "2":
    DealerHandValueNumber= (DealerHandValueNumber+ 2)
  elif card == "3":
    DealerHandValueNumber= (DealerHandValueNumber+ 3)
  elif card == "4":
    DealerHandValueNumber= (DealerHandValueNumber+ 4)
  elif card == "5":
    DealerHandValueNumber= (DealerHandValueNumber+ 5)
  elif card == "6":
    DealerHandValueNumber= (DealerHandValueNumber+6)
  elif card == "7":
    DealerHandValueNumber= (DealerHandValueNumber+ 7)
  elif card == "8":
    DealerHandValueNumber= (DealerHandValueNumber+ 8)
  elif card == "9":
    DealerHandValueNumber= (DealerHandValueNumber+ 9)
  else:
    DealerHandValueNumber= (DealerHandValueNumber + 10)

while True:
  if UserHandValueNumber == 21:
    print("You have reached the higest hand possible now you must beat the dealer.")
    time.sleep(4)
    break
  elif UserHandValueNumber >= 22:
    break
  else:
    print("You may now hit for another card by typing 1 or stand by typing 2.")
    HitAnswer = input()
    if  HitAnswer == "1":
      
      UserHitCard = random.choice(CardNames)
      UserCardNames.append(UserHitCard)
      print(" ")
      print("You have been delt a(n) "+str(UserHitCard))
      print(" ")
      time.sleep(4)

      if UserHitCard == "ace":
        UserHandValues.append("0")
      elif UserHitCard== "two":
        UserHandValues.append("2")
      elif UserHitCard == "three":
        UserHandValues.append("3")
      elif UserHitCard== "four":
        UserHandValues.append("4")
      elif UserHitCard== "five":
        UserHandValues.append("5")
      elif UserHitCard== "six":
        UserHandValues.append("6")
      elif UserHitCard== "seven":
        UserHandValues.append("7")
      elif UserHitCard== "eight":
        UserHandValues.append("8")
      elif UserHitCard== "nine":
        UserHandValues.append("9")
      elif UserHitCard== "ten":
        UserHandValues.append("10")
      elif UserHitCard == "Jack":
        UserHandValues.append("11")
      elif UserHitCard == "Queen":
        UserHandValues.append("12")
      elif UserHitCard =="King":
        UserHandValues.append("13")
      UserHandValueNumber= 0
      for card in UserHandValues:
        if card == "0":
          if UserHandValueNumber+ 1 > 21:
            print("Bust")
          elif UserHandValueNumber<= 10:
            UserHandValueNumber= (UserHandValueNumber+ 11)
          else:
            UserHandValueNumber= (UserHandValueNumber+ 1)
        elif card == "2":
          UserHandValueNumber= (UserHandValueNumber+ 2)
        elif card == "3":
          UserHandValueNumber= (UserHandValueNumber+ 3)
        elif card == "4":
          UserHandValueNumber= (UserHandValueNumber+ 4)
        elif card == "5":
          UserHandValueNumber= (UserHandValueNumber+ 5)
        elif card == "6":
          UserHandValueNumber= (UserHandValueNumber+6)
        elif card == "7":
          UserHandValueNumber= (UserHandValueNumber+ 7)
        elif card == "8":
          UserHandValueNumber= (UserHandValueNumber+ 8)
        elif card == "9":
          UserHandValueNumber= (UserHandValueNumber+ 9)
        else:
          UserHandValueNumber= (UserHandValueNumber + 10)
      if UserHandValueNumber <= 21:
        print("Your hand total is "+str(UserHandValueNumber))
        time.sleep(4)
    elif HitAnswer == "2":
      print("You have decided to stand.")
      print("Here are your cards  "+str(UserCardNames))
      print("Here is your hand's current total "+str(UserHandValueNumber))
      print(" ")
      time.sleep(4)
      break
#time for card counting and or bust
if UserHandValueNumber <=21:
  time.sleep(4)
  print(" ")
  print("Here is the Dealer's full hand "+str(DealerCardNames))
  print("And their hand's total value "+str(DealerHandValueNumber))
  print(" ")
  time.sleep(4)
  while True:
    if DealerHandValueNumber > 16:
      print("""
      The Dealer's hand is over 16 so they will not hit again.
      """)
      time.sleep(4)
      break
    elif DealerHandValueNumber <= 16:
      print("""Because the Dealer's hand is not higher than 16 they must hit""")
      time.sleep(4)
      DealerHitCard = random.choice(CardNames)
      DealerCardNames.append(DealerHitCard)
      print(" ")
      print("The Dealer has been delt a(n) "+str(DealerHitCard))
      print(" ")
      time.sleep(4)
      if DealerHitCard == "ace":
        DealerHandValues.append("0")
      elif DealerHitCard== "two":
        DealerHandValues.append("2")
      elif DealerHitCard == "three":
        DealerHandValues.append("3")
      elif DealerHitCard== "four":
        DealerHandValues.append("4")
      elif DealerHitCard== "five":
        DealerHandValues.append("5")
      elif DealerHitCard== "six":
        DealerHandValues.append("6")
      elif DealerHitCard== "seven":
        DealerHandValues.append("7")
      elif DealerHitCard== "eight":
        DealerHandValues.append("8")
      elif DealerHitCard== "nine":
        DealerHandValues.append("9")
      elif DealerHitCard== "ten":
        DealerHandValues.append("10")
      elif DealerHitCard == "Jack":
        DealerHandValues.append("11")
      elif DealerHitCard == "Queen":
        DealerHandValues.append("12")
      elif DealerHitCard =="King":
        DealerHandValues.append("13")
      DealerHandValueNumber= 0
      
      for card in DealerHandValues:
        if card == "0":
          if DealerHandValueNumber+ 1 > 21:
            print("Bust")
          elif DealerHandValueNumber<= 10:
            DealerHandValueNumber= (DealerHandValueNumber+ 11)
          else:
            DealerHandValueNumber= (DealerHandValueNumber+ 1)
        elif card == "2":
          DealerHandValueNumber= (DealerHandValueNumber+ 2)
        elif card == "3":
          DealerHandValueNumber= (DealerHandValueNumber+ 3)
        elif card == "4":
          DealerHandValueNumber= (DealerHandValueNumber+ 4)
        elif card == "5":
          DealerHandValueNumber= (DealerHandValueNumber+ 5)
        elif card == "6":
          DealerHandValueNumber= (DealerHandValueNumber+6)
        elif card == "7":
          DealerHandValueNumber= (DealerHandValueNumber+ 7)
        elif card == "8":
          DealerHandValueNumber= (DealerHandValueNumber+ 8)
        elif card == "9":
          DealerHandValueNumber= (DealerHandValueNumber+ 9)
        else:
          DealerHandValueNumber= (DealerHandValueNumber + 10)
      
  if DealerHandValueNumber > 21:
    print("""
    The Dealer's hand has bust so you win by default!""")
  elif DealerHandValueNumber <= 21:
    print("Here are the final hands.")
    print(" ")
    time.sleep(1)
    print("Here are the dealer's cards "+str(DealerCardNames))
    print("Here is the Dealer's total value "+str(DealerHandValueNumber))
    time.sleep(4)
    print(" ")
    print("Here are your cards "+str(UserCardNames))
    print("Here is your hand's total value "+str(UserHandValueNumber))
    print(" ")
    time.sleep(4)
    if UserHandValueNumber > DealerHandValueNumber:
      print("""
      Your hand has beat the Dealer's!
      You Win!
      """)
    elif UserHandValueNumber == DealerHandValueNumber:
      print("""
      Your and the Dealer have the same value hand, so you have tied!""")
    elif UserHandValueNumber < DealerHandValueNumber:
      print("""
      The Dealer's hand has beat yours!
      You Lose!""")


      
else:
  print("Your hand bust!")