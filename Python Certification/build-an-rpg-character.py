full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"
    elif not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance (charisma, int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    elif strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    else:
        strength_dot = (strength * full_dot) + (10 - strength) * empty_dot
        intell_dot = (intelligence * full_dot) + (10 - intelligence) * empty_dot
        charisma_dot = (charisma * full_dot) + (10 - charisma) * empty_dot
        return (f"{name}\n"
                f"STR {strength_dot}\n"
                f"INT {intell_dot}\n"
                f"CHA {charisma_dot}")

print(create_character('ren', 4, 1, 2))
