from defaultBody import defaultBody
from datetime import date
from TestCalculator import TestCalculator


class Exercise:
    def __init__(self, name: str, muscle_groups: dict, max_weight: int = 1, weight_based: bool = True, source_link = ["Developer"]):
        self.name: str = name
        self.max_weight: int = max_weight
        self.weighted_muscle_groups: dict = muscle_groups
        self.weight_based = weight_based
        self.source = source_link

        # find maximum parts:
        self.max_parts = 0
        for key in self.weighted_muscle_groups:
           if self.weighted_muscle_groups[key] > self.max_parts:
               self.max_parts = self.weighted_muscle_groups[key]



    def reps_completed(self, weight: int, reps: int = 1, sets = 1, reps_per_set = 1):
        total_hp_loss: int = 0
        response = self.name + ", Total Loss: "
        if self.weight_based:
            # Calculate  Total Toll
            rep_percentage_of_max: int = int(weight / self.max_weight * 100)
            total_hp_loss: int = TestCalculator.compute_values_for_weight_based_exercises(current_weight_percentage=rep_percentage_of_max, number_of_sets=sets, reps_per_set=reps_per_set)
            response += str(total_hp_loss) + "\nMuscles Impacted (value): "
            # worth of one weighted part
        else:
            # total loss
            total_hp_loss = weight/self.max_weight*100
            response += str(total_hp_loss) + "\nMuscles Impacted (value): "

        # worth of one weighted part
        # one with the largest number of parts gets 100%, its part count = M
        # each other part recieves #/M * hp loss.

        max_parts = self.max_parts
        for key in self.weighted_muscle_groups:
            # Update the hit points
            given_muscle_hp_loss = (self.weighted_muscle_groups[key]/max_parts)*total_hp_loss
            defaultBody.my_muscles[key].durability_current -= given_muscle_hp_loss
            # Explain how the durability impacts different muscle groups.
            response += key + " (" + str(given_muscle_hp_loss) + "), "
            # Update the most recent workout time
            defaultBody.my_muscles[key].day_last_worked = date.today()

        # Print Response to User
        print(response + "\n")

    def find_leading_muscle_group(self):
        muscles = self.weighted_muscle_groups
        max_parts = 0
        leading_muscle_group = "None"
        for key in muscles:
            if muscles[key] > max_parts:
                max_parts = muscles[key]
                leading_muscle_group = key
        return leading_muscle_group


