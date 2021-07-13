from defaultBody import defaultBody
from ListOfExercistes import listOfExercises
from Exercise import Exercise
from MuscleGroup import MuscleGroup
from TestCalculator import TestCalculator


class WorkoutFinder:

    completed_workout_hp_target:int = 20
    @staticmethod
    def daily_recommendation():
        print("Muscle Groups to Focus Today:")
        recommended_exercises_with_duplicates: list = []
        working_on = defaultBody.names_of_top_five()
        print(working_on)
        for index in range(len(working_on)):
            tagged = WorkoutFinder.find_tag_matches(working_on[index])
            for index_tagged in range(len(tagged)):
                recommended_exercises_with_duplicates.append(tagged[index_tagged])
        # print(recommended_exercises_with_duplicates)

        # Shifting to a weighted format:
        recommended_exercises = []
        for index in range(len(recommended_exercises_with_duplicates)):
            searching_for = recommended_exercises_with_duplicates[index]
            count = 0
            for index in range(len(recommended_exercises_with_duplicates)):
                if recommended_exercises_with_duplicates[index] == searching_for:
                    count += 1
            if not recommended_exercises.__contains__({searching_for: count}):
                recommended_exercises.append({searching_for: count})
        WorkoutFinder.find_reps_and_weight(recommended_exercises)



    @staticmethod
    def find_tag_matches(tag: str):
        print(f"Searching for an exercise that works: {tag}")
        names_of_exercises_that_match_tag = []
        exercises = listOfExercises.listOfExercises
        for exercise in exercises:
            for muscle in exercises[exercise].weighted_muscle_groups:
                # print(f"Comparing {muscle} to {tag}")
                if muscle == tag:
                    # print(f"{exercise} works {tag}.")
                    names_of_exercises_that_match_tag.append(exercise)
        return names_of_exercises_that_match_tag

    @staticmethod
    def find_reps_and_weight(recommended_exercises: list):
        # Have the user select an exercise

        workout_selected = WorkoutFinder.user_select_exercise(recommended_exercises)
        exercise: Exercise = listOfExercises.listOfExercises[workout_selected]

        muscle_group = exercise.find_leading_muscle_group()
        leading_muscle_weighted_parts = exercise.weighted_muscle_groups[muscle_group]
        # Find Hp Loss
        targeted_hp_loss = WorkoutFinder.find_ideal_durability_loss(workout_selected)
        # one rep max OR maximum reps
        rep_max = listOfExercises.listOfExercises[workout_selected].max_weight
       # can not assume that the exercise needs to be worked.
        if targeted_hp_loss is not None:
            # if the exercise is weight based, calculate weight, sets, and reps
            if exercise.weight_based:
                # find number of reps
                number_of_reps = WorkoutFinder.find_number_of_reps(defaultBody.find_current_durability(muscle_group))
                sets = 3
                reps_per_set = int(number_of_reps/sets)
                print(f"{sets} sets of {reps_per_set}")

                print(f"rep max: {rep_max}")
                # find the weight percentage
                weight_percentage = TestCalculator.weight_percentage_calculator(number_of_sets=sets, reps_per_set=reps_per_set,ideal_hp_toll=targeted_hp_loss)
                # weight per repetition
                weight_per_rep = (weight_percentage/100)*rep_max
                # Present Findings to the User
                print(f"User will complete {sets} sets of {reps_per_set} reps @ {weight_per_rep} lbs.")
            # if not, the exercise is reps based.
            else:
                # find the number of reps.
                number_of_reps = TestCalculator.rep_calculator(targeted_hp_loss, rep_max)




    @staticmethod
    def user_select_exercise(recommended_exercises:list):
        print(recommended_exercises)
        print("Which exercise would you like to complete?")
        selected_dictionary = recommended_exercises[int(input())]
        selected_exercise: str = "None"
        for key in selected_dictionary:
            selected_exercise = key
        print(f"Selected: {selected_exercise}")
        return selected_exercise

    @staticmethod
    def find_ideal_durability_loss(workout_selected: str):
        # make a copy of the workout
        workout:Exercise  = listOfExercises.listOfExercises[workout_selected]
        # find the leading muscle group
        leading_muscle_group = workout.find_leading_muscle_group()
        print(f"Leading Muscle Group: {leading_muscle_group}")
        # find current durability (access muscle group)
        current_hp = defaultBody.find_current_durability(leading_muscle_group)
        # ideal durability loss = current-target  *** asuming that current is above target
        if current_hp > WorkoutFinder.completed_workout_hp_target:
            ideal_hp_loss = current_hp-WorkoutFinder.completed_workout_hp_target
            print(f"Ideal hp loss: {ideal_hp_loss}")
            return ideal_hp_loss
        else:
            print("You should not be working this muscle group")
            return None


    @staticmethod
    def find_number_of_reps(current_hp:int):
        if current_hp>75:
            return 15
        elif current_hp>60:
            return 30
        else:
            return 45










