# calculator to determine how many miles you could have driven for the amount of beef you ate
# or the amount of beef you could have eaten for how far you drove

BEEF_KG_CO2_PER_KG = 40.2
GASOLINE_CO2_PER_GALLON = 8.887

choice = input("Did you drive or did you eat beef? Please type 'drive' or 'beef'.\n").lower()

if choice == "drive":
    distance = float(input("How many miles did you drive? Please enter a number.\n"))
    vehicle_mpg = float(input("What mpg does your car get? Please enter a number."))

    gas_used = distance / vehicle_mpg
    CO2_emitted_driving = gas_used * GASOLINE_CO2_PER_GALLON
    beef_equivalent = float("{:.2f}".format(CO2_emitted_driving / BEEF_KG_CO2_PER_KG))

    print(f"Your drive emitted {CO2_emitted} kg of CO2. You could have eaten {beef_equivalent} kg of beef!")

elif choice == "beef":
    beef_eaten = float(input("How much beef did you eat, in grams?\n"))
    CO2_of_beef_eaten = (beef_eaten/1000) * BEEF_KG_CO2_PER_KG
