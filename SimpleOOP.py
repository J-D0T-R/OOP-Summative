###   Simple OOP   ###
###   James Rutley   ###
###   Start Date: 11/04/2021   ###
###   End Date: 11/04/2021   ###

# Classes
class teachers:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        
    def __str__(self):
        print(f"{self.name} teaches {self.subjects}")
        return f"{self.name} teaches {self.subjects}."

class coaches(teachers):
    def __init__(self, name, subjects, sport):
        teachers.__init__(self, name, subjects)
        self.sport = sport
        
# Instances
Mr_Whyte = teachers("Mr. Whyte", "Comp Sci")

Mrs_Snell = teachers("Mrs. Snell", "Tutorial")

Ms_Wintonyk = teachers("Ms. Wintonyk", "ELA, Art and Tutorial")

Mr_Parker = coaches("Mr. Parker", "Math", "Volleyball")

Mr_Clark = coaches("Mr. Clark", "Social and Gym", "Football")


Mr_Whyte.__str__()

Mr_Clark.__str__()


        
