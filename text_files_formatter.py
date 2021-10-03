from os import stat
import country_list

def set_up(text_file): 
    with open(text_file, "r") as file:
        sections_list = []
        lines = file.readlines()
        for line in lines:
            sections = line.split("\t")
            sections_list.append(sections)
    return sections_list

def players(section_list, new_file_name):
    new_file = open(new_file_name, "w")
    # generate uuid, get name, number, height, weight
    id = 0
    for i in section_list:
        id +=1
        if len(i) == 11:
            name = i[1]
            number = i[0]
            height = i[4]
            weight = i[5]
        elif len(i) == 10:
            name = i[0]
            number = ""
            height = i[3]
            weight = i[4]
        else:
            name = i[0]
            number = ""
            height = i[3]
            weight = i[4]
        formatted_string = f"{id}\t{name}\t{number}\t{height}\t{weight}\n"
        new_file.write(formatted_string)
    new_file.close()
    
def coaches(section_list, new_file_name):
    new_file = open(new_file_name, "w")
    # get id, title, and name
    id = 1
    for section in section_list: 
        list = section.split("\t")
        name = list[0]
        title = list[1].replace("\n", "")
        formatted_string = f"{id}\t{title}\t{name}\n"
        new_file.write(formatted_string)
        id += 1
    new_file.close() 

def hometowns(section_list, new_file_name):
    all_countries = []
    unique_hometowns = []
    id = 1

    # get a list of all countries
    for i in country_list.countries_for_language("en"):
        all_countries.append(i[1].lower())

    new_file = open(new_file_name, "w")
    for section in section_list:
        # Get id, city, state, country
        if len(section) == 11:
            full = section[6]
        else:
            full = section[5]
        city = full.split(",")[0].strip()
        state = full.split(",")[1].strip()

        if state.lower() in all_countries:
            country = state
        else:
            country = "United States"

        if (city, state, country) not in unique_hometowns:
            unique_hometowns.append((city, state, country))
        
    for ht in unique_hometowns:
        formatted_string = f"{id}\t{ht[0]}\t{ht[1]}\t{ht[2]}\n"
        new_file.write(formatted_string)
        id += 1
    new_file.close()
 
def classes(section_list, new_file_name):
    # get id and name
    new_file = open(new_file_name, "w")
    class_names = []
    for section in section_list:
        if len(section) == 10 or len(section) == 7:
            class_name = section[1]
        else:
            class_name = section[2]
        if class_name not in class_names:
            class_names.append(class_name)
    id = 1
    for name in class_names:
        formatted_string = f"{id}\t{name}\n"
        new_file.write(formatted_string)
        id += 1
    new_file.close()

def high_schools(section_list, new_file_name):
    new_file = open(new_file_name, "w")
    unique_high_school_list = []
    id = 1
    for section in section_list:
        if len(section) == 7 or len(section) == 10:
            name = section[6]
        else: 
            name = section[7]
        if name not in unique_high_school_list:
            unique_high_school_list.append(name)

    for hs in unique_high_school_list:
        formatted_string = f"{id}\t{hs}\n"
        new_file.write(formatted_string)
        id +=1 
    new_file.close()

def positions(section_list, new_file_name): 
    new_file = open(new_file_name, "w")
    unique_positions = []
    id = 1
    for section in section_list:
        if len(section) == 11:
            name = section[3]
        elif len(section) == 7 or len(section) == 10:
            name = section[2]
        if name not in unique_positions:
            unique_positions.append(name)
    for up in unique_positions:
        formatted_string = f"{id}\t{up}\n"
        new_file.write(formatted_string)
        id +=1 
    new_file.close()

if __name__ == "__main__":
    all_data = set_up("all_data.txt")
    coaches_data = set_up("coaches.txt")

    players(all_data, "new_player.txt")
    coaches(coaches_data, "new_coaches.txt") 
    hometowns(all_data, "hometowns.txt")
    classes(all_data, "classes.txt")
    high_schools(all_data, "highschools.txt")
    positions(all_data, "positions.txt")




