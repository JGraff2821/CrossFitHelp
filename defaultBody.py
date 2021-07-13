from MuscleGroup import MuscleGroup


class defaultBody:
    # List of Muscles:
    my_muscles:dict = {}
    # Basic Muscles Groups
    # For now we are assuming durability at 105ph for each, @ this, a full workout of a group is a 3*5 @ 70% weight.
    # Eventually, I will want to allow the user to set/edit durability based upon their position within
    # their workout journey.

    # Back
    back: MuscleGroup = MuscleGroup("Back")
    my_muscles["Back"] = back
    # Chest
    chest: MuscleGroup = MuscleGroup("Chest")
    my_muscles["Chest"] = chest
    # Hamstrings
    hamstrings: MuscleGroup = MuscleGroup("Hamstrings")
    my_muscles["Hamstrings"] = hamstrings
    # Quads
    quads: MuscleGroup = MuscleGroup("Quads")
    my_muscles["Quads"] = quads
    # Glutes
    glutes: MuscleGroup = MuscleGroup("Glutes")
    my_muscles["Glutes"] = glutes
    # Abbs
    abbs: MuscleGroup = MuscleGroup("Abbs")
    my_muscles["Abbs"] = abbs
    # Lats
    lats: MuscleGroup = MuscleGroup("Lats")
    my_muscles["Lats"] = lats
    # Forearms
    forearms: MuscleGroup = MuscleGroup("Forearms")
    my_muscles["Forearms"] = forearms
    # Hip Flexors
    hipFlexors: MuscleGroup = MuscleGroup("Hip Flexors")
    my_muscles["Hip Flexors"] = hipFlexors
    # Biceps
    biceps: MuscleGroup = MuscleGroup("Biceps")
    my_muscles["Biceps"] = biceps
    # Triceps
    triceps: MuscleGroup = MuscleGroup("Triceps")
    my_muscles["Triceps"] = triceps
    # Shoulders
    shoulders: MuscleGroup = MuscleGroup("Shoulders")
    my_muscles["Shoulders"] = shoulders
    # Cardio
    cardio: MuscleGroup = MuscleGroup("Cardio")
    my_muscles["Cardio"] = cardio

    @staticmethod
    def printCurrentMap():
        for muscle_group in defaultBody.my_muscles:
            print(defaultBody.my_muscles[muscle_group])
        print()

    @staticmethod
    def muscle_dictionary_to_list():
        copy:dict = defaultBody.my_muscles
        muscles_list = []
        for key in copy:
            muscles_list.append(copy[key])
        return muscles_list

    @staticmethod
    def find_index_of_first_highest_durability(current_list: list):
        copy = current_list
        best_case_index = 0
        for i in range(len(copy)):
            if copy[i].durability_current > copy[best_case_index].durability_current:
                best_case_index=i
        return best_case_index

    @staticmethod
    def find_top_five_durability():
        copy = defaultBody.muscle_dictionary_to_list()
        top_five = []
        for i in range(5):
            best_index = defaultBody.find_index_of_first_highest_durability(copy)
            top_five.append(copy[best_index])
            copy.pop(best_index)
        return top_five

    @staticmethod
    def names_of_top_five():
        top_five = defaultBody.find_top_five_durability()
        names = []
        for index in range(len(top_five)):
            names.append(top_five[index].name)
        return names

    @staticmethod
    def reset_body():
        for key in defaultBody.my_muscles:
            defaultBody.my_muscles[key].durability_current = defaultBody.my_muscles[key].durability_max
            defaultBody.my_muscles[key].day_last_worked = None
    @staticmethod
    def copy_of_muscle_group(name: str):
        return defaultBody.my_muscles[name]
    @staticmethod
    def find_current_durability(muscle_group:str):
        for key in defaultBody.my_muscles:
            if muscle_group == key:
                return defaultBody.my_muscles[key].durability_current
        return None
