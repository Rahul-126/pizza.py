#Pizza Order
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
if size == "S": #Y
  bill = 15
  if add_pepperoni == "Y": #N
    bill += 2
    if extra_cheese == "Y": 
      bill += 1
      #print(f"Your final bill is: ${bill}.")
  elif extra_cheese == "Y": #N
    bill += 1
    #print(f"Your final bill is: ${bill}.")

  print(f"Your final bill is: ${bill}.")
elif size == "M":
  bill = 20
  if add_pepperoni == "Y": #N
    bill += 3
    if extra_cheese == "Y": 
      bill += 1
      #print(f"Your final bill is: ${bill}.")
  elif extra_cheese == "Y": #N
    bill += 1
    #print(f"Your final bill is: ${bill}.")

  print(f"Your final bill is: ${bill}.")
elif size == "L":
  bill = 25
  if add_pepperoni == "Y": #N
    bill += 3
    if extra_cheese == "Y": 
      bill += 1
      #print(f"Your final bill is: ${bill}.")
  elif extra_cheese == "Y": #N
    bill += 1
    #print(f"Your final bill is: ${bill}.")

  print(f"Your final bill is: ${bill}.")
