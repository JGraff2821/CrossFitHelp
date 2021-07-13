from defaultBody import defaultBody
from Exercise import Exercise
from WorkoutFinder import WorkoutFinder
from ListOfExercistes import listOfExercises
from TestCalculator import TestCalculator
if __name__ == '__main__':
    possible_exercises = listOfExercises.listOfExercises
    # test_space = defaultBody()
    # test_space.printCurrentMap()
    #
    # WOD 6.7.21
    # 21-15-9 of
    # Assault Bike
    possible_exercises["Assault Bike"].reps_completed(45)
    # # Dumbbell Front Squats
    possible_exercises["Dumbbell Front Squat"].reps_completed(50, 45)
    # # Assault Bike
    possible_exercises["Assault Bike"].reps_completed(45)
    defaultBody.printCurrentMap()
    WorkoutFinder.daily_recommendation()
    # #
    # # print()
    # # print()
    # # # defaultBody.resetBody()
    # possible_exercises["Toes To Bar"].reps_completed(21)
    # # possible_exercises["Bench Press"].reps_completed(104, 15)
    # #
    # defaultBody.printCurrentMap()

    #
    # TestCalculator.main()




