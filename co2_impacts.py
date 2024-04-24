# this is a dict of impacts that we can pull from


co2_impacts = {
  "beef": 40.2,
  "chicken": 6.9,
  "coffee": 0.4,
  "rice": 0.9,
  "gasoline": 8.887,
  "honey": 1.4,
  "peanut butter": 2.88,
  "bread slice": (.0589 / 16), # (one loaf contains 16 slices, roughly)
  "cottage cheese": 7.75,
  "eggs": (2.7 / 12), # 2.7kg per dozen eggs
  "english muffin": (1.38 * 0.061), # from ClimateHub. Reported in CO2/ kg, and an english muffin is 61g per the package.https://apps.carboncloud.com/climatehub/product-reports/072220002751/USA
}