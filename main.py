# calculator to determine how many miles you could have driven for the amount of beef you ate
# or the amount of beef you could have eaten for how far you drove
from get_carbon_impact import get_carbon_impact_dict
from co2_impacts import co2_impacts
from co2_impacts_poore import ghg_poore as ghg

BEEF_KG_CO2_PER_KG = 40.2
CHICKEN_KG_CO2_PER_KG = 6.9
GASOLINE_CO2_PER_GALLON = 8.887
COFFEE_KG_CO2_PER_CUP_15g = 0.4
RICE_KG_CO2_PER_KG = 0.9 # per https://www.nature.com/articles/s43017-023-00482-1

keep_going = True

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

def calc_vehicle_equivalent(co2: float) -> float:
    vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
    distance_possibly_driven = float("{:.2f}".format((co2 / GASOLINE_CO2_PER_GALLON) * vehicle_mpg))
    return distance_possibly_driven

def main():

    while keep_going:

        choice = input("Did you drive, eat beef, eat chicken, or drink coffee? Please type 'drive', 'beef', 'chicken', or 'coffee'.\n").lower()

        match choice:
            case "drive":
                distance = float(input("How many miles did you drive? Please enter a number.\n"))
                vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
                gas_used = distance / vehicle_mpg
                CO2_emitted_driving = float("{:.2f}".format(get_carbon_impact_dict("gasoline", gas_used))) #float("{:.2f}".format(gas_used * GASOLINE_CO2_PER_GALLON))
                beef_equivalent = float("{:.2f}".format(CO2_emitted_driving / ghg["Beef (beef herd)"]))
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

            case "coffee":
                coffee_cups_consumed = float(input("How much coffee did you drink, in cups?\n"))
                CO2_of_coffee_consumed = float("{:.2f}".format((coffee_cups_consumed) * COFFEE_KG_CO2_PER_CUP_15g))
                vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
                beef_equivalent = float("{:.2f}".format(CO2_of_coffee_consumed / BEEF_KG_CO2_PER_KG))
                distance_possibly_driven = float("{:.2f}".format((CO2_of_coffee_consumed / GASOLINE_CO2_PER_GALLON)*vehicle_mpg))

                print(f"The coffee you drank emitted {CO2_of_coffee_consumed} kg of CO2. You could have driven your car {distance_possibly_driven}"
                      f" miles for the same emissions.")
                print(f"Or you could have eaten {beef_equivalent} kg of beef instead.")

                ask_again()

            case "pbh":
                pbh_eaten = input("How many peanut butter and honey sandwiches did you consume?\n")
                co2_PB = float("{:.2f}".format(.2 * co2_impacts["peanut butter"]))
                co2_honey = float("{:.2f}".format(.013 * co2_impacts["honey"]))
                co2_bread = float("{:.2f}".format(2 * co2_impacts["bread slice"]))
                co2_total = co2_bread + co2_PB + co2_honey

                vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
                beef_equivalent = float("{:.2f}".format(co2_total / BEEF_KG_CO2_PER_KG))
                distance_possibly_driven = float("{:.2f}".format((co2_total / GASOLINE_CO2_PER_GALLON)*vehicle_mpg))

                print(f"Your PB&H emitted {co2_total} kg of CO2. You could have driven your car {distance_possibly_driven}"
                      f" miles for the same emissions.")
                print(f"Or you could have eaten {beef_equivalent} kg of beef instead.")

                ask_again()

            case "egg":
                eggs_eaten = int(input("How many eggs did you eat?\n"))
                co2_eggs = float("{:.2f}".format(eggs_eaten * co2_impacts["eggs"]))
                print(f"Your eggs emitted {co2_eggs} kg of CO2.")
                print(f"You could have driven {calc_vehicle_equivalent(co2_eggs)} miles for the same emissions.")

                ask_again()

            case _:
                print("That options isn't currently supported. Please select one of the supported options.")

if __name__ == "__main__":
    main()