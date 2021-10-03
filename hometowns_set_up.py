import country_list
all_countries = []
id = 1

for i in country_list.countries_for_language("en"):
    all_countries.append(i[1].lower())

new_file = open("new_hometowns.txt", "w")
with open("players.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        sections = line.split("\t")
        # Get id, city, state, country
        if len(sections) == 11:
            full = sections[6]
        else:
            full = sections[5]

        city = full.split(",")[0].strip()
        state = full.split(",")[1].strip()

        if state.lower() in all_countries:
            country = state
        else:
            country = "United States"
       
        formatted_string = f"{id}\t{city}\t{state}\t{country}\n"
        new_file.write(formatted_string)
        id += 1
   
new_file.close()