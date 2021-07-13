import datetime
class MuscleGroup:
    def __init__(self, name: str = "No Name", durability: int = 100):
        self.name: str = name
        self.durability_max: int = durability
        self.durability_current: int = durability
        self.day_last_worked: datetime = None

    def __str__(self):
        return self.name+", Durability: "+ str(self.durability_current)+ " of " + str(self.durability_max)+", last worked: "+str(self.day_last_worked)
    # We will calculate based on 1 rep-at 100% counting for 10 hp., therefore, 10 at 60% is 60hp,
    # This means that a 3*5 @ 70% = 105hp




