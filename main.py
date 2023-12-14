# calculator to determine how many miles you could have driven for the amount of beef you ate
# or the amount of beef you could have eaten for how far you drove

BEEF_KG_CO2_PER_KG = 40.2
CHICKEN_KG_CO2_PER_KG = 6.9
GASOLINE_CO2_PER_GALLON = 8.887

def ask_again():
    while True:
        go_again = input("Would you like to go again? Please enter 'Y' or 'n'.\n")
        match go_again:
            case 'Y':
                break
            case 'n':
                global keep_going
                keep_going = False
                break
            case _:
                print("Please enter 'Y' or 'n'.")

keep_going = True

while keep_going:

    choice = input("Did you drive, eat beef, or eat chicken? Please type 'drive', 'beef', or 'chicken'.\n").lower()

    match choice:
        case "drive":
            distance = float(input("How many miles did you drive? Please enter a number.\n"))
            vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
            gas_used = distance / vehicle_mpg
            CO2_emitted_driving = float("{:.2f}".format(gas_used * GASOLINE_CO2_PER_GALLON))
            beef_equivalent = float("{:.2f}".format(CO2_emitted_driving / BEEF_KG_CO2_PER_KG))
            chicken_equivalent = float("{:.2f}".format(CO2_emitted_driving / CHICKEN_KG_CO2_PER_KG))

            print(f"Your drive emitted {CO2_emitted_driving} kg of CO2. You could have eaten {beef_equivalent} kg of "
                  f"beef, or {chicken_equivalent} kg of chicken.")

            ask_again()

        case "beef":
            beef_eaten = float(input("How much beef did you eat, in grams?\n"))
            CO2_of_beef_eaten = float("{:.2f}".format((beef_eaten/1000) * BEEF_KG_CO2_PER_KG))
            vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
            chicken_equivalent = float("{:.2f}".format(CO2_of_beef_eaten / CHICKEN_KG_CO2_PER_KG))
            distance_possibly_driven = float("{:.2f}".format((CO2_of_beef_eaten / GASOLINE_CO2_PER_GALLON)*vehicle_mpg))

            print(f"The beef you ate emitted {CO2_of_beef_eaten} kg of CO2. You could have driven your car {distance_possibly_driven}"
                  f" miles for the same emissions.")
            print(f"Or you could have eaten {chicken_equivalent} kg of chicken instead.")

            ask_again()

        case "chicken":
            chicken_eaten = float(input("How much chicken did you eat, in grams?\n"))
            CO2_of_chicken_eaten = float("{:.2f}".format((chicken_eaten/1000) * CHICKEN_KG_CO2_PER_KG))
            vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
            beef_equivalent = float("{:.2f}".format(CO2_of_chicken_eaten / BEEF_KG_CO2_PER_KG))
            distance_possibly_driven = float("{:.2f}".format((CO2_of_chicken_eaten / GASOLINE_CO2_PER_GALLON)*vehicle_mpg))

            print(f"The chicken you ate emitted {CO2_of_chicken_eaten} kg of CO2. You could have driven your car {distance_possibly_driven}"
                  f" miles for the same emissions.")
            print(f"Or you could have eaten {beef_equivalent} kg of beef instead.")

            ask_again()

        case _:
            print("That options isn't currently supported. Please select one of the supported options.")

