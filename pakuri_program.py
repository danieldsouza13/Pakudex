from pakudex import *

# pakudex = Pakudex(capacity=userinput)
# 1. add pakuri
# pakudex.add_pakuri(userinput2)

if __name__ == "__main__":  # if name dunder

    print("Welcome to Pakudex: Tracker Extraordinaire!")

    isvalid = False  # try and except to only allow for valid capicity inputs
    while not isvalid:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity < 0:
                raise ValueError
            isvalid = True

        except ValueError:
            print("Please enter a valid size.")

    print(f"The Pakudex can hold {capacity} species of Pakuri.")  # capacity
    pakudex = Pakudex(capacity)  # handler
    size = 0


    pakudex_continue = True
    while pakudex_continue:

        menu_error = False  # try and except to only allow for valid capicity inputs
        while not menu_error:
            print("\nPakudex Main Menu")
            print("-----------------")
            print("1. List Pakuri")
            print("2. Show Pakuri")
            print("3. Add Pakuri")
            print("4. Evolve Pakuri")
            print("5. Sort Pakuri")
            print("6. Exit\n")
            try:
                option = int(input("What would you like to do? "))


                if option not in [1,2,3,4,5,6]:
                    raise ValueError
                menu_error = True

            except ValueError:
                print("Unrecognized menu selection!")

        if option == 1:  # list of pakuri

            if pakudex.get_species_array() == []:  # if no pakuri have been added
                print("No Pakuri in Pakudex yet!")

            else:
                print("Pakuri In Pakudex:")
                species = pakudex.get_species_array()  # str list of pakuri
                for order, pakuri in enumerate(species, start=1):  # formats the pakuri into a numbered list
                    print(f"{order}. {pakuri}")

        elif option == 2:  # displays the stats of a species
            display_species = input("Enter the name of the species to display: ")
            display_true = pakudex.get_stats(display_species)

            if display_true == None:
                print("Error: No such Pakuri!")
                continue

            print(f"\nSpecies: {display_species}")
            print(f"Attack: {display_true[0]}")
            print(f"Defense: {display_true[1]}")
            print(f"Speed: {display_true[2]}")

        elif option == 3:  # adds a pakuri to a list

            if capacity == size:
                print("Error: Pakudex is full!")
                continue

            else:
                creature = input("Enter the name of the species to add: ")
                res = pakudex.add_pakuri(creature)
                size += 1

        elif option == 4:  # evolves a pakuri
            evolve = input("Enter the name of the species to evolve: ")
            if pakudex.evolve_species(evolve) is False:
                print("Error: No such Pakuri!")

            else:
                print(f"{evolve} has evolved!")

        elif option == 5:  # sorts the pakuri
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif option == 6:  # quits the game
            pakudex_continue = False
            print("Thanks for using Pakudex! Bye!")


