def clac_caloried():
    
    user_input= input("Calories: ")
    lower_input = user_input.lower()
    if lower_input == "apple":
        print("130")
    elif lower_input == "avocado ":
          print("50")
    elif lower_input == "sweet cherries ":
          print("100")
    else:
        print("")
        
clac_caloried()