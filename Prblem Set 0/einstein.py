# make a fucntion 
def calculateEnergy(mass_kg):
    c = 300000000
    energy_joules = mass_kg * c ** 2
    return energy_joules

# make  a main func
def main():
    mass_kg = int(input("Enter mass in kilogram : "))
    energy_joules = calculateEnergy(mass_kg) 
    print("Equivalent energy in joules" , energy_joules)

main()