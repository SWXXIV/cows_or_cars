# calculator to determine how many miles you could have driven for the amount of beef you ate
# or the amount of beef you could have eaten for how far you drove
from get_carbon_impact import get_carbon_impact_dict, get_fuel_impact
from co2_impacts import co2_impacts
from co2_impacts_poore import ghg_poore as ghg

# BEEF_KG_CO2_PER_KG = 40.2
# CHICKEN_KG_CO2_PER_KG = 6.9
# GASOLINE_CO2_PER_GALLON = 8.887
# COFFEE_KG_CO2_PER_CUP_15g = 0.4
# RICE_KG_CO2_PER_KG = 0.9 # per https://www.nature.com/articles/s43017-023-00482-1

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
                print("Thanks for using the ghg equivalence calculator!")
                break
            case _:
                print("Please enter 'Y' or 'n'.")

def ask_for_mpg() -> float:
    #TODO: handle case where user doesn't enter a float-convertable string
    vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
    return vehicle_mpg

def ask_for_distance_driven() -> float:
    #TODO: handle case where user doesn't enter a float-convertable string
    distance_driven = float(input("How many miles did you drive? Please enter a number.\n"))
    return distance_driven

# need to refactor this function to take a dataclass or simply a dict as an input
def calc_vehicle_equivalent(co2: float, vehicle_mpg: float) -> float:
    # vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
    distance_possibly_driven = float("{:.2f}".format(get_fuel_impact(co2)["gasoline, US gal"] * vehicle_mpg))
    return distance_possibly_driven

def calc_beef_equivalent(co2: float) -> float:
    # beef_equivalent = float("{:.2f}".format(co2 / ghg["Beef (beef herd)"]))
    beef_equivalent = float("{:.2f}".format(co2 / get_carbon_impact_dict("Beef (Kg)")))
    return beef_equivalent

def calc_chicken_equivalent(co2: float) -> float:
    # beef_equivalent = float("{:.2f}".format(co2 / ghg["Beef (beef herd)"]))
    chicken_equivalent = float("{:.2f}".format(co2 / get_carbon_impact_dict("Chicken (Kg)")))
    return chicken_equivalent

def calc_co2_emitted_driving(distance_driven: float, vehicle_mpg: float) -> float:
    gas_used = distance_driven / vehicle_mpg
    co2_emitted_driving = float("{:.2f}".format(get_carbon_impact_dict("Gasoline (US gal)", gas_used)))
    return co2_emitted_driving

def main():

    while keep_going:

        choice = input("Did you drive, eat beef, eat chicken, or drink coffee? Please type 'drive', 'beef', 'chicken', or 'coffee'.\n").lower()

        match choice:
            case "drive":
                distance = ask_for_distance_driven()
                # vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
                vehicle_mpg = ask_for_mpg()
                # co2_emitted_driving = float("{:.2f}".format(get_carbon_impact_dict("Gasoline (US gal)", gas_used))) #float("{:.2f}".format(gas_used * GASOLINE_CO2_PER_GALLON))
                co2_emitted_driving = calc_co2_emitted_driving(distance, vehicle_mpg)
                beef_equivalent = float("{:.2f}".format(co2_emitted_driving / ghg["Beef (beef herd)"]))
                chicken_equivalent = float("{:.2f}".format(get_carbon_impact_dict("Chicken (Kg)", co2_emitted_driving)))

                print(f"Your drive emitted {co2_emitted_driving} kg of CO2. You could have eaten {beef_equivalent} kg of "
                      f"beef, or {chicken_equivalent} kg of chicken.")

                ask_again()

            case "beef":
                beef_eaten = float(input("How much beef did you eat, in kg?\n"))
                CO2_of_beef_eaten = float("{:.2f}".format(get_carbon_impact_dict("Beef (Kg)", beef_eaten)))
                vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
                chicken_equivalent = float("{:.2f}".format(CO2_of_beef_eaten / co2_impacts["Chicken (Kg)"]))
                distance_possibly_driven = float("{:.2f}".format((get_fuel_impact(CO2_of_beef_eaten)["gasoline (US gal)"])*vehicle_mpg))

                print(f"The beef you ate emitted {CO2_of_beef_eaten} kg of CO2. You could have driven your car {distance_possibly_driven}"
                      f" miles for the same emissions.")
                print(f"Or you could have eaten {chicken_equivalent} kg of chicken instead.")

                ask_again()

            case "chicken":
                chicken_eaten = float(input("How much chicken did you eat, in kg?\n"))
                CO2_of_chicken_eaten = float("{:.2f}".format(get_carbon_impact_dict("Chicken (Kg)", chicken_eaten)))
                vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
                beef_equivalent = float("{:.2f}".format(get_carbon_impact_dict("beef", CO2_of_chicken_eaten)))
                distance_possibly_driven = float("{:.2f}".format(get_fuel_impact(CO2_of_chicken_eaten)["gasoline"]*vehicle_mpg))

                print(f"The chicken you ate emitted {CO2_of_chicken_eaten} kg of CO2. You could have driven your car {distance_possibly_driven}"
                      f" miles for the same emissions.")
                print(f"Or you could have eaten {beef_equivalent} kg of beef instead.")

                ask_again()

            case "coffee":
                coffee_cups_consumed = float(input("How much coffee did you drink, in cups?\n"))
                CO2_of_coffee_consumed = float("{:.2f}".format(get_carbon_impact_dict("coffee", (coffee_cups_consumed*.017))))
                vehicle_mpg = float(input("What mpg does your car get? Please enter a number.\n"))
                beef_equivalent = float("{:.2f}".format(get_carbon_impact_dict("beef", CO2_of_coffee_consumed)))
                distance_possibly_driven = float("{:.2f}".format(get_fuel_impact(CO2_of_coffee_consumed)["gasoline"]*vehicle_mpg))

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
                beef_equivalent = float("{:.2f}".format(get_carbon_impact_dict("beef", co2_total)))
                distance_possibly_driven = float("{:.2f}".format(get_fuel_impact(co2_total)["gasoline"]*vehicle_mpg))

                print(f"Your PB&H emitted {co2_total} kg of CO2. You could have driven your car {distance_possibly_driven}"
                      f" miles for the same emissions.")
                print(f"Or you could have eaten {beef_equivalent} kg of beef instead.")

                ask_again()

            case "egg":
                eggs_eaten = int(input("How many eggs did you eat?\n"))
                co2_eggs = float("{:.2f}".format(eggs_eaten * co2_impacts["Eggs, Large (qty eggs)"]))
                print(f"Your eggs emitted {co2_eggs} kg of CO2.")
                mpg = ask_for_mpg()
                print(f"You could have driven {calc_vehicle_equivalent(co2_eggs, mpg)} miles for the same emissions.")

                ask_again()

            case _:
                print("That options isn't currently supported. Please select one of the supported options.")

if __name__ == "__main__":
    main()