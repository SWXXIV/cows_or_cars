# this is a dict of impacts that we can pull from

#TODO: Create an intermediate between the text on the frontend and the dict key


co2_impacts = {
  "Rolled Oats (Kg)": 1.25,
  "Rolled Oats (1/2 cup; 40g)": 0.05,
  "Dried Blueberries (Kg)": 4.00,
  "Dried Blueberries (1/3 cup; 40g)": 0.16,
  "Brown Sugar (Kg)": 1.4,
  "Brown Sugar (2 tsp, 8g)": 0.112,
  "Beef (Kg)": 40.2,
  "Butter, salted (Kg)": 10.179, # https://livelca.com/products/butter_273d0577-1c3b-4e5e-94fb-4084b0eebe78
  "Chicken (Kg)": 6.9,
  "Coffee (cups)": 0.4,
  "Rice (Kg)": 0.9,
  "Gasoline (US gal)": 8.887,
  "Honey (Kg)": 1.4,
  "Peanut Butter (Kg)": 2.88,
  "Bread (slices)": (.589 / 16), # (one loaf contains 16 slices, roughly)
  "Cottage Cheese": 7.75,
  "Eggs, Large (qty eggs)": (2.7 / 12), # 2.7kg per dozen eggs
  "English Muffin (qty of muffins)": (1.38 * 0.061), # from ClimateHub. Reported in CO2/ kg, and an english muffin is 61g per the package.https://apps.carboncloud.com/climatehub/product-reports/072220002751/USA
  "Milk, kg": (0.96), #see refs/milk_impacts.pdf
}