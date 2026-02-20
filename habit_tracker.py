

habit_tracker_dic = {
    "coding": [True, True, True],
    "workout": [True, False, True]
}
total_streak = {}                                                               #dictionary key habit   value is number of days streaked

while True:
    user_input = input("Enter action: create_habit / ongoing_habit / weekly_summary / total / quit : ").strip()
    streak_counter = 0

    if user_input == "create_habit":
        habit = input("What habbit would you like to track? ").strip()
        habit_completion = input(f"Has {habit} been completed today? (yes or no) ").strip()
        if habit_completion == "yes":
            habit_tracker_dic[habit] = habit_tracker_dic.get(habit, []) + [True]
        elif habit_completion == "no":
            habit_tracker_dic[habit] = habit_tracker_dic.get(habit, []) + [False]
        else:
            print("Invalid command")
    
    if user_input == "ongoing_habit":
        habit = input("What habit are we already tracking? ")
        habit_completion = input(f"Has {habit} been completed today? (yes or no) ").strip()
        if habit_completion == "yes":
            habit_tracker_dic[habit] = habit_tracker_dic.get(habit, []) + [True]
        elif habit_completion == "no":
            habit_tracker_dic[habit] = habit_tracker_dic.get(habit, []) + [False]

    elif user_input == "weekly_summary":
        for habit, habit_success in habit_tracker_dic.items():                      #do i use another for loop to loop through habit success as a list?
            for day in habit_success:
                if day == True:
                    streak_counter += 1
                    total_streak[habit] = streak_counter
                else:
                    streak_counter = 0
        print(total_streak)
    
    elif user_input == "quit":
        break

    elif user_input == "total":
        print(habit_tracker_dic)

    else:
        print("Invalid input... try again")
            

