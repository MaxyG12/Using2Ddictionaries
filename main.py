print("Mokebeasts Full-on Mokedex")
print()

mokedex = {}

def prettyPrint():
  print()
  for key, value in mokedex.items():
    print(key, end=": ")
    for subKey, subValue in value.items():
      print(subKey, subValue, end=" | ")
    print()

while True:
  name = input("Input the beast name > ")
  element = input("Input the beast element > ")
  specialMove = input("Input the beast special move > ")
  hp = input("Input the beast starting HP > ")
  mp = input("Input the beast starting MP > ")
  mokedex[name] = {"Element": element, "Special Move": specialMove, "HP": hp, "MP": mp}
  prettyPrint()
  
  again = input("Again? y/n > ")
  if again == "y":
    continue
  else:
    break