# counties = ["Arapahoe","Denver","Jefferson"]

# if counties[1] == "Denver":
#     print(counties[1])

# if counties[3] == "Jefferson":
#     print(counties[2])

# if "El Paso" in counties:
#     print("El paso is in the list of counties.")
# else:
#     print("El paso is not in the list of counties.")

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso are in the list of counties.")
# else:
#      print("Arapahoe and El paso is not in the list of counties.")

# for county in counties:
#     print(county)

# for i in range(len(counties)):
#     print(counties[i])

counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

# for county in counties_dict:
#     print(counties_dict.get(county))

# for county, voters in counties_dict.items():
#     print(county + " county has "+ str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:6,} registered voters.")

voting_data = [{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]

# for county_dict in voting_data:
#     print(county_dict['county'])