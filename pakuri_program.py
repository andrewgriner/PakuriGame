from pakudex import Pakudex #Importing pakedex

def main(): #Main fucntion
  print("Welcome to Pakudex: Tracker Extraordinaire!")
  capacity = input("Enter max capacity of the Pakudex: ")

  while not capacity.isdigit(): #This evalutes the user input and if it is not a digit the user is asked for input
    print("Please enter a valid size.")
    capacity = input("Enter max capacity of the Pakudex: ")


  capacity=int(capacity) #Size of index
  input_pakudex = Pakudex(capacity)
  print("The Pakudex can hold "+str(capacity)+" species of Pakuri.")
  game=True
  menu_text="\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit\n\nWhat would you like to do? "
  while game:
    menu = input(menu_text)
    while True:
      if menu.isdigit(): #This evalutes the menu options and breaks if its not in range
        if 1<=int(menu)<=6:
          break

      print("Unrecognized menu selection!")
      menu = input(menu_text)
    menu = int(menu)

    if menu == 1: #This prints the pakuri species
      pakudex_array = input_pakudex.get_species_array()
      if pakudex_array is not None:
        print("Pakuri In Pakudex:")
        for i, species in enumerate(pakudex_array):
          print(str(i + 1) + ". " + species)
      else: #If there are none yet then it returns this
        print("No Pakuri in Pakudex yet!")


    elif menu == 2: #This allows tue user to see the stats of a pakuri
      species = input("Enter the name of the species to display: ")
      species_stats = input_pakudex.get_stats(species)
      if species_stats is not False and species_stats is not None:
        defense = str(species_stats[1])
        atk = str(species_stats[0])
        spd = str(species_stats[2])
        print("\nSpecies: " + species + "\nAttack: " + atk + "\nDefense: " + defense + "\nSpeed: " + spd)
      else:
        print("Error: No such Pakuri!") #else statement incase of no pakuri

    elif menu == 3: #This evalues capacity space and allows addition
      if len(input_pakudex.pakudex) == input_pakudex.get_capacity():
        print("Error: Pakudex is full!") #print statement if it is full
      else:
        species = input("Enter the name of the species to add: ")
        if input_pakudex.add_pakuri(species):
          print(f"Pakuri species {species} successfully added!") #adding a pakuri
        else:
          print("Error: Pakudex already contains this species!")

    elif menu == 4: #This option allowes users to evolve pakuri
      species_to_evolve = input("Enter the name of the species to evolve: ")
      evolved = False
      for pakuri in input_pakudex.pakudex: #evalutes if it is in pakedex
        if pakuri.get_species() == species_to_evolve:
          pakuri.evolve()
          evolved = True
          print(pakuri.get_species() + " has evolved!")
          break
      if not evolved: #Statement in case theres not that pakuri in pakedex
        print("Error: No such Pakuri!")

    elif menu == 5: #calls upon the pakedex class to sort pakuri
      input_pakudex.sort_pakuri()
      print("Pakuri have been sorted!")

    elif menu == 6: #This will break the user out of the game cycle
      print("Thanks for using Pakudex! Bye!")
      game = False
      break

if __name__ == "__main__": #main function that is required
  main()