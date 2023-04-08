# Day 7 challange

print(" Fake Fan Finder ")
print("-----------------")
favorite_anime = input("What's Yor favorite Anime ? ")


if favorite_anime == 'One piece':
  print("oh really?! Name me any of the charaters ",favorite_anime)
  charaters = input("Favorite charater of anime ? ")
  if charaters == 'Nami':
    print("Right Choose")
  else:
    print("this is not a good charaters")
elif favorite_anime == 'dead Note':
  print("Aww, Not a good deal")
  fav_charater = input("Favorite Charaters : ")
  if fav_charater == 'Yes':
    print("Yes")
  else:
    print("No")
else:
  print("see! Fake",favorite_anime, "fan!")





# fix my code
'''
order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  else: 
    print("No cheese it is.")
elif order == pizza:
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")




tvShow = input("What is your favourite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favourite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
'''