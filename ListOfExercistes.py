from Exercise import Exercise


class listOfExercises:
    #Unmandated Rule ********* Make sure that the most worked muscle group is the first one written.
    # Bench Press
    listOfExercises: dict= {"Bench Press": Exercise(name="Bench Press", muscle_groups={"Chest": 3, "Triceps": 1, "Shoulders": 1}, max_weight=205)}

    # Hell Bike
    # Cardio is different, we are doing max within a given increment of time
    # For the bike, most calories within a minute.
    listOfExercises["Assault Bike"] = Exercise(name="Assault Bike", muscle_groups={"Cardio": 2, "Quads": 1}, max_weight=100, weight_based=False)

    # Dumbbell Front Squat
    listOfExercises["Dumbbell Front Squat"] = Exercise(name="Dumbbell Front Squat", muscle_groups={"Glutes": 1, "Hamstrings": 1, "Quads": 1},  max_weight=125)

    # Toes to Bars
    listOfExercises["Toes To Bar"] = Exercise(name="Toes To Bar", muscle_groups={"Abbs": 6, "Hip Flexors": 1, "Forearms": 1, "Lats": 2},  max_weight=30, weight_based=False)

    # Burpees
    listOfExercises["Burpees"] = Exercise(name="Burpees", muscle_groups={"Cardio": 4, "Quads": 1},  max_weight=50, weight_based=False)
