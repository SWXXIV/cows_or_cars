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



#print(get_carbon_impact("beef", 0.54))

if __name__ == "__main__":
    list_carbon_impact_poore()