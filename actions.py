# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Abdulmohsin"
my_age = 30
my_bio = "I like stuff and stuff likes me"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print(" Hello, %s. Welcome to our portal." % my_name)
    options()

def options():
    while True:
        print ("----------------")
        print (" What would you like to do?")
        print (" 1) Create a new Club. \n or:")
        print (" 2) Browse and join clubs. \n or:")
        print (" 3) View existing clubs. \n or:")
        print (" 4) Display members of a Club \n or:")
        print (" -1) Close Application")
        choice = input("Please enter an option number... ")
        options_interpretter(choice)

    
def options_interpretter(option):
    if (option == "1"):
        create_club()
    elif (option == "2"):
        join_clubs()
    elif (option == "3"):
        view_clubs()
    elif (option == "4"):
        view_club_members()
    elif (option == "-1"):
        exit()

def populate_newClub (tempClub):
    
    print ("Enter the number of a person you want to recruit to %s (-1 to stop):" %tempClub.name)
    while True:    
        for i in range (0, len(population)):
            print ("%s]%s"%(i+1, population[i].name))
        selection = input("Which person would you like to join your club? ")
        if (selection == "-1"):
            return
        elif (selection_check(selection)):
            if (tempClub.alreadyHas(population[int(selection)-1])):
                print ("That person is already a member of this club!")
            else:
                tempClub.recruit_member(population[int(selection)-1])
                
            
        else:
            print ("Please select a valid Number")
        print ("----------------")
        print ("Current Members:")
        print (tempClub.print_member_list())
        print ("----------------")

def selection_check(selection):
    try:
        val = int(selection)
    except ValueError:
        print ("Please enter a number")
        return False
    
    if val > 0 and val <= len(population):
        return True
    else:
        return False

def create_club():
    # Picking option 1 should prompt the user for a name for their new club and a description of their new club. Example:
    print ("Creating a new club!")
    club_name = input("What is your clubs name? ")
    descp = input("What is the club, %s, about? " %club_name)
    tempClub = Club(club_name, descp)
    
    populate_newClub (tempClub)
    tempClub.members = [myself] + tempClub.members
    tempClub.assign_president(myself)
    print (" Here is your club overview:")
    print (" Title: %s" %tempClub.name)
    print (" Description: %s" %tempClub.description)
    print (" Members:")
    print (tempClub.print_member_list_detail())
    clubs.append(tempClub)

def view_clubs():
        for club in clubs:
            print ("\tName: %s\n\tDescription: %s\n\tMembers: %s\n" %(club.name, club.description, len(club.members)))
       
    

def view_club_members():
    view_clubs()
    while True:
        selection = input(" Which club's members would you like to see? Type 'None' to exit...  ")
        if (selection.lower() == "none"):
            return
        else:
            for club in clubs:
                if (selection.lower() == club.name.lower()):
                    club.print_member_list_detail()
                    return
            print (" Please select a valid Club")    
    

def join_clubs():
    view_clubs()
    while True:
        selection = input(" Which club would you like to join? Type 'None' to exit...  ")
        if (selection.lower() == "none"):
            return
        else:
            for club in clubs:
                if (selection.lower() == club.name.lower()):
                    club.recruit_member(myself)
                    print (" %s has been added to %s" %(myself.name, club.name))
                    return
            print (" Please select a valid Club")    
    

def application():
    introduction()
    
    
