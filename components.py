# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        self.name = name
        self.bio = bio
        self.age = age
        self.president = False
        # your code goes here!


class Club():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.members = []
        self.president = None
        

    def assign_president(self, person):
        self.president = person
        

    def recruit_member(self, person):
        self.members.append(person)
        

    def print_member_list(self):
        for member in self.members:
            print ("%s"%member.name)
        return

    def alreadyHas(self, person):
        if person in self.members:
            return True
        else:
            return False        

    def print_member_list_detail(self):
        avg = 0
        for member in self.members:
            avg += member.age
            if (self.president.name == member.name):
                print (" %s (%s years old, President) - %s" %(member.name, member.age, member.bio))
            else:
                print (" %s (%s years old) - %s" %(member.name, member.age, member.bio))
        print (" - Average age = %s" %(avg/len(self.members)))
        