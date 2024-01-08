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

def get_carbon_impact(activity: str, qty: float) -> float:
    return co2_impacts[activity] * qty

print(get_carbon_impact("beef"))