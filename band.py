#python3
#thinkful python track 1.3 "Modeling things using Python classes"

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
    
    def solo(self, length):
        for i in range(length):
            #modulus on length gets position of sound to be played 
            print(self.sounds[i % len(self.sounds)], end=" ")
        print("")


class Bassist(Musician):
    #every class has to have an init-function, but ...
    def __init__(self):
    #in this case we just call the parents init-method with super() 
    # (inheritance via super-call)
    #super() == call parent, dot to indicate method, then method name
        super().__init__(["Twang", "Thrumb", "Bling"])


class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])
        
    def tune(self):
        print("Be with you in a minute")
        print("Sploing, twoing, splang")
        
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bonk", "Boomb", "Baang", "Twifff"])
        
    def count(self):
        print("1.. 2\nand 1\n2\n3\n4!")
        
    def combust(self):
        print("The drummer exploded")


class Band(object):
    def __init__(self, band_name, members_list=[]):
        self.members = members_list
        self.band_name = band_name
        
    def get_members(self):
        if not len(self.members):
            print("There are no more members left in the band")
            print()
        else: 
            print("{} is now a band of {}:".format(self.band_name, len(self.members)), end=" ")
            for m in self.members:
                print(m.__class__.__name__.lower(), end=" ")
            print("\n")
        
    def hire(self, member):
        self.members.append(member)
        type = member.__class__.__name__
        print("We have a {} as the new member of '{}'".format(str(type).lower(), self.band_name))
        self.get_members()

    def fire(self, member):
        self.members.remove(member)
        type = member.__class__.__name__
        print("The {} is so fired from '{}'".format(str(type).lower(), self.band_name))
        self.get_members()

    def play_solos(self, length):
        print("Time for the solos!")
        #find instance of drummer in list - TODO: there has to be an easier way!
        for m in self.members:
            if m.__class__.__name__ == "Drummer":
                m.count()
                break
        for m in self.members:
            print(str(m.__class__.__name__) + ": ", end="")
            m.solo(length)


## TESTING 
david = Musician(["Pling", "Bum", "Gadong"])
guitargirl = Guitarist()
bazboy = Bassist()
drumboy = Drummer()
mojitos = Band("The Mojitos")
mojitos.hire(david)
mojitos.hire(guitargirl)
mojitos.hire(bazboy)
mojitos.hire(drumboy)
mojitos.play_solos(10)
print()