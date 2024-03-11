def give_info(first_name: str, birth_year: int):
    age = 2024 - birth_year
    print(f"{first_name} is {age} years old.")
    
# intentionally wrong
give_info("Aygün", "1990") # TypeError: unsupported operand type(s) for -: 'int' and 'str'

