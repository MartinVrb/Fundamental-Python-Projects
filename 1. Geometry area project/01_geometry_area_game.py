from math import pi

my_list = []
stop_outer_loop = False
maybe_cm = False
figure = ""

first_side = 0
second_side = 0
side = 0
height = 0
measurement = "cm"
area = 0
welcome = input("Hi! Do you want to start the area calculator? (Yes/No): ")

# Dobavi na ostanalite figuri.Proverki na stranite dali sa chisla

if welcome == "Yes":
    while True:
        figure = input("Whats your figure? (square, triangle, rectangle, rhombus, trapezium, circle): ")
        if figure in ["square", "triangle", "rectangle", "rhombus", "trapezium", "circle"]:
            break
        else:
            print("Please enter a valid figure.")

    while not stop_outer_loop:
        ask_if_they_are_cm = input("Are your values in cm? (Yes/No): ")
        if ask_if_they_are_cm == "Yes":
            print("Great!")
            maybe_cm = True
            break
        elif ask_if_they_are_cm == "No":
            while not stop_outer_loop:
                ask_to_transform_to_cm = input("Do you want to transform your values in cm? (Yes/No): ")
                if ask_to_transform_to_cm == "No":
                    print("Ok!:)")
                    stop_outer_loop = True

                elif ask_to_transform_to_cm == "Yes":
                    while not stop_outer_loop:
                        what_measurement = input("In what unit of measurement are your values? (dm/m/km): ")
                        if what_measurement in ["dm", "m", "km"]:
                            measurement = what_measurement
                            conversion_factors = {"dm": 10, "m": 100, "km": 100000}
                            factor = conversion_factors[what_measurement]
                            while True:
                                value = input("Enter your values for the area and type 'Stop' when you're ready.: ")
                                if value == 'Stop':
                                    stop_outer_loop = True
                                    break
                                else:
                                    try:
                                        value = float(value)
                                        if value > 0:
                                            value_in_cm = value * factor
                                            if value_in_cm.is_integer():
                                                value_in_cm = int(value_in_cm)
                                                print(value_in_cm)
                                                while True:
                                                    first_save = input(
                                                        "Do you want to save the value? (Yes/No): ")
                                                    if first_save == "Yes":
                                                        my_list.append(value_in_cm)
                                                        print("Your value is saved!")
                                                        break
                                                    elif first_save == "No":
                                                        print("Ok!")
                                                        break
                                                    else:
                                                        print("Please enter a valid answer.")
                                            else:
                                                print(value_in_cm)
                                                while True:
                                                    save_value = input(
                                                        "Do you want to save the value? (Yes/No): ")
                                                    if save_value == "Yes":
                                                        my_list.append(value_in_cm)
                                                        print("Your value is saved!")
                                                        break
                                                    elif save_value == "No":
                                                        print("Ok!")
                                                        break
                                                    else:
                                                        print("Please enter a valid answer.")

                                        else:
                                            print("Please enter a positive num.")

                                    except ValueError:
                                        print("Please enter a valid value.")
                        else:
                            print("Please enter a valid unit of length.")
                else:
                    print("Please enter a valid answer.")
        else:
            print("Please enter a valid answer.")

    stop_outer_loop = False

    while not stop_outer_loop:
        if figure == "square":
            if maybe_cm:
                while True:
                    side = input(f"Length of the side in {measurement}: ")
                    try:
                        side = float(side)
                        if side.is_integer():
                            side = int(side)
                            stop_outer_loop = True
                            area = side ** 2
                            break
                        else:
                            stop_outer_loop = True
                            area = side ** 2
                            break
                    except ValueError:
                        print("Please enter valid number.")

            elif not maybe_cm:
                while not stop_outer_loop:
                    if my_list:
                        match_question = input("Does your first saved value match with your side? (Yes/No): ")
                        if match_question == "Yes":
                            while True:
                                try:
                                    side = float(my_list[0])
                                    if side.is_integer():
                                        side = int(side)
                                        stop_outer_loop = True
                                        area = side ** 2
                                        break
                                    else:
                                        stop_outer_loop = True
                                        area = side ** 2
                                        break
                                except ValueError:
                                    print("Please enter valid number.")

                        elif match_question == "No":
                            while True:
                                user_input = input(f"Enter the length of your side in {measurement}: ")
                                try:
                                    side = float(user_input)
                                    if side.is_integer():
                                        side = int(side)
                                        stop_outer_loop = True
                                        area = side ** 2
                                        break
                                    else:
                                        stop_outer_loop = True
                                        area = side ** 2
                                    break
                                except ValueError:
                                    print("Please enter valid number.")
                        else:
                            print("Please enter a valid answer.")
                    else:
                        while True:
                            user_input = input(f"Enter the length of your side in {measurement}: ")
                            try:
                                side = float(user_input)
                                if side.is_integer():
                                    side = int(side)
                                    stop_outer_loop = True
                                    area = side ** 2
                                    break
                                else:
                                    stop_outer_loop = True
                                    area = side ** 2
                                break
                            except ValueError:
                                print("Please enter valid number.")

    stop_outer_loop = False

    # Vsichko e topa, otkomentirai go tva.
    # elif figure == "triangle":
    #         choice_of_triangle = input("Is your triangle right (Yes/No)?: ")
    #         if maybe_cm:
    #             if choice_of_triangle == "Yes":
    #                 first_side = float(input(f"Length of the first side in {measurement}: "))
    #                 second_side = float(input(f"Length of the second side in {measurement}: "))
    #                 area = (first_side * second_side) / 2
    #
    #             elif choice_of_triangle == "No":
    #                 side = float(input(f"Length of the side in {measurement}: "))
    #                 height = float(input(f"Length of the height in {measurement}: "))
    #                 area = (side * height) / 2
    #
    #             else:
    #                 is_it_true = False
    #
    #         elif ask_if_they_are_cm == "No":
    #             if choice_of_triangle == "Yes":
    #                 if transform:
    #                     match_question = input(
    #                         "Does your first saved value (if there is one) match with your first side? (Yes/No): "
    #                     )
    #                     if match_question == "Yes":
    #                         first_side = float(my_list[0])
    #                     elif match_question == "No":
    #                         first_side = float(input(f"Length of the first side in {measurement}: "))
    #                     else:
    #                         is_it_true = False
    #                     if is_it_true:
    #                         second_match_question = input(
    #                             "Does your second saved value (if there is one) match with your second side? ("
    #                             "Yes/No): "
    #                         )
    #                         if second_match_question == "Yes":
    #                             second_side = float(my_list[1])
    #                         elif second_match_question == "No":
    #                             second_side = float(input(f"Length of the second side in {measurement}: "))
    #                         else:
    #                             is_it_true = False
    #                         area = (first_side * second_side) / 2
    #                 else:
    #                     ask_what_measurement_second = input(
    #                         "In what unit of measurement are your values? (dm/m/km): "
    #                     )
    #                     if ask_what_measurement_second not in ["dm", "m", "km"]:
    #                         is_it_true = False
    #                     else:
    #                         measurement = ask_what_measurement_second
    #                         first_side = float(input(f"Length of the side in {measurement}: "))
    #                         second_side = float(input(f"Length of the height in {measurement}: "))
    #                         area = (first_side * second_side) / 2
    #
    #             elif choice_of_triangle == "No":
    #                 if transform:
    #                     match_question = input(
    #                         "Does your first saved value (if there is one) match with your side? (Yes/No): ")
    #                     if match_question == "Yes":
    #                         side = float(my_list[0])
    #                     elif match_question == "No":
    #                         side = float(input(f"Length of the side in {measurement}: "))
    #                     else:
    #                         is_it_true = False
    #                     if is_it_true:
    #                         second_match_question = input(
    #                             "Does your second saved value (if there is one) match with your height? (Yes/No): "
    #                         )
    #                         if second_match_question == "Yes":
    #                             height = float(my_list[1])
    #                         elif second_match_question == "No":
    #                             height = float(input(f"Length of the height in {measurement}: "))
    #                         else:
    #                             is_it_true = False
    #                         area = (side * height) / 2
    #                 else:
    #                     ask_what_measurement_second = input(
    #                         "In what unit of measurement are your values? (dm/m/km): "
    #                     )
    #                     if ask_what_measurement_second not in ["dm", "m", "km"]:
    #                         is_it_true = False
    #                     else:
    #                         measurement = ask_what_measurement_second
    #                         side = float(input(f"Length of the side in {measurement}: "))
    #                         height = float(input(f"Length of the height in {measurement}: "))
    #                         area = (side * height) / 2
    #
    #             else:
    #                 is_it_true = False
    #
    #         else:
    #             is_it_true = False
    #         #
    #         #     elif figure == "rectangle":
    #         #         first_side = float(input("Length of first side(cm): "))
    #         #         second_side = float(input("Length of second side(cm):"))
    #         #         area = first_side * second_side
    #         #
    #         #     elif figure == "rhombus":
    #         #         first_diagonal = float(input("Length of first diagonal(cm): "))
    #         #         second_diagonal = float(input("Length of second diagonal(cm): "))
    #         #         area = (first_diagonal * second_diagonal) / 2
    #         #
    #         #     elif figure == "trapezium":
    #         #         first_side = float(input("Length of first side(cm): "))
    #         #         second_side = float(input("Length of second side(cm):"))
    #         #         height = float(input("Length of height(cm):"))
    #         #         area = ((first_side + second_side) * height) / 2
    #         #
    #         #     elif figure == "circle":
    #         #         radius = float(input("Length of radius(cm):"))
    #         #         area = pi * (radius ** 2)
    #         #
    #         #     else:
    #         #         is_it_true = False
    #         #
    #         #     if is_it_true:
    #         #         if area.is_integer():
print(f"Your area is {int(area)} {measurement}")
#         else:
#             print(f"{area:.2f} {measurement}")
#             print("Your area is formatted to the second integer.")
#     else:
#         print("Incorrect!")
#
# else:
#     print("Incorrect!")
