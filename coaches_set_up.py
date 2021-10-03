new_file = open("new_coaches.txt", "w")
id = 1
with open("coaches.txt", "r") as file:
    lines = file.readlines()
    for section in lines: 
       list = section.split("\t")
       name = list[0]
       title = list[1].replace("\n", "")
       formatted_string = f"{id}\t{title}\t{name}\n"
       new_file.write(formatted_string)
       id += 1
new_file.close() 