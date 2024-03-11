names_list = []

def add_names(name: str):
    names_list.append(name)
    return names_list


print(add_names("Mustafa")) # ['Mustafa']

add_names("Kağan")
add_names("Börü")
add_names("Kürşat")

def show_names(names: list[str]):
    for name in names:
        print(f"Name: {name}")


show_names(names_list)    

"""
Name: Mustafa
Name: Kağan
Name: Börü
Name: Kürşat
"""
