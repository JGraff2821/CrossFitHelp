class TestCalculator:

    @staticmethod
    def main():
        TestCalculator.rep_calculator(ideal_hp_toll=80, maximum_repetitions=100)
    @staticmethod
    def percent_difference_calculator(v_min: int, v_max: int):
        return ((v_max-v_min)/v_max)*100

    # ********************************** Methods for Rep Based Exercises ***********************************************
    @staticmethod
    def rep_calculator(ideal_hp_toll:float, maximum_repetitions: int):
        print("rep calculator called")
        # Ideal percentage of maximum reps
        percentage_target_hp_toll = ideal_hp_toll/100
        # Percentage multiplied by maximum.
        reps_to_complete = int(percentage_target_hp_toll*maximum_repetitions)
        print(f"User should do {reps_to_complete} reps.")
        return reps_to_complete
    # ********************************** Methods for Weight Based Exercises ********************************************
    @staticmethod
    def weight_percentage_calculator(number_of_sets: int, reps_per_set:int, ideal_hp_toll):
        percent_difference_toll = None
        current_weight_percentage = 1
        current_toll = TestCalculator.compute_values_for_weight_based_exercises(current_weight_percentage, number_of_sets, reps_per_set)
        while current_toll < ideal_hp_toll:
            current_weight_percentage += 1
            current_toll = TestCalculator.compute_values_for_weight_based_exercises(current_weight_percentage, number_of_sets,
                                                                                    reps_per_set)
        print(f"Recommended Percentage: {current_weight_percentage-1}")
        return current_weight_percentage-1

    @staticmethod
    def compute_values_for_weight_based_exercises(current_weight_percentage, number_of_sets, reps_per_set):
        # computed_values = []
        # for weight based exercises:
        # the lower that this number is, the harder the workout.
        weight_factor_x = 0.72
        weighted_base_constant = current_weight_percentage*weight_factor_x

        # the weight of the exercise has great value
        total_difficulty_value = 10*weighted_base_constant

        # this variable tracks additional fatigue for sequential reps
        fatigue_weight_contstant = 1*weighted_base_constant

        # finding additional fatigue
        rep_count =0
        new_set_decrease=0 # tracks new set relief
        for sets in range(number_of_sets):
            for current_rep_count in range(reps_per_set):
                # muscles fatigue as the number of reps increas => greater difficulty
                ten_percent_weight =  .1*fatigue_weight_contstant
                increase_in_value =(ten_percent_weight*ten_percent_weight*ten_percent_weight*rep_count-new_set_decrease)/100
                total_difficulty_value+=increase_in_value

                rep_count+=1
            # new sets decrement the fatigue value, in a 3 by 5 the 6th rep is marginally easier than the 5th
            new_set_decrease+=20
        total_difficulty_value/=10
        # print(computed_values)
        return total_difficulty_value




