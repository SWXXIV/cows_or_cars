''' this is a function that should take as inputs what you did and how much, and return a float of kg CO2
I have this idea that you can do this if you have a backing data structure like a dict like:

co2_impacts = {
  "beef": 40.2,
  "chicken": 6.9,
  "coffee": 0.4,
  "rice": 0.9,
}

I don't know why I want this to be a table in a RDB. A dict works fine so far!
'''

from co2_impacts import co2_impacts
import csv

def get_carbon_impact_dict(activity: str, qty: float) -> float:
    return (co2_impacts[activity] * qty)

def get_fuel_impact(qty: float) -> dict:
    '''get_fuel_impact takes a float of the quantity of emitted carbon and returns a dict
    of fuels, showing the amount of fuel you could have burned to emit the same carbon.'''
    fuel_carbons = {
        "KWh": .092, # kg per KWh, WA state, from https://www.eia.gov/electricity/state/washington/, converted to kg/ KWh
        "propane, gal": 5.75, # kg per gallon, from https://www.eia.gov/environment/emissions/co2_vol_mass.php
        "cordwood, cords": 2200, # per cord, https://extension.psu.edu/conversions-commonly-used-when-comparing-timber-and-carbon-values
        "gasoline, US gal": 8.1, # kg per gal, accounts for ethanol blending
        "diesel, US gal": 10.19,
        "natural gas, 1000 cf": 54.87, # kg per thousand cubic feet
    }
    fuel_quantities = {
        "KWh": None,
        "propane, gal": None,
        "cordwood, cords": None,
        "gasoline, US gal": None,
        "diesel, US gal": None,
        "natural gas, 1000 cf": None
    }
    for i in fuel_carbons:
        fuel_quantities[i] = qty/ fuel_carbons[i]
    return fuel_quantities

def list_carbon_impacts_poore():
    with open('ghg-per-kg-poore.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} have {row[3]} kgCO2/kg.')
                line_count += 1
        print(f'Processed {line_count} lines.')

def build_CO2_dict():
    res = {}
    with open('ghg-per-kg-poore.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'\t{row[0]} have {row[3]} kgCO2/kg.')
                res[row[0]] = float(row[3])
                line_count += 1
        print(f'Processed {line_count} lines.')
    out = open("co2_impacts_poore.py", "w")
    out.write(f"ghg_poore = {res}")
    out.close()


#print(get_carbon_impact("beef", 0.54))

if __name__ == "__main__":
    # build_CO2_dict()
    print(get_fuel_impact(10.5))
    for key, value in get_fuel_impact(10.5).items():
        print(f"<p>{'{:.2f}'.format(value)} {key}</p>")