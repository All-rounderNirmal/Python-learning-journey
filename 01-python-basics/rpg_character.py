def create_character(character_name, strength, intelligence, charisma):
    full_dot = '●'
    empty_dot = '○'

    if not isinstance(character_name, str):
        return "The character name should be a string"

    if character_name == "":
        return "The character should have a name"

    if len(character_name) > 10:
        return "The character name is too long"

    if " " in character_name:
        return "The character name should not contain spaces"

    stats = (strength, intelligence, charisma)

    if not all(isinstance(stat, int) and not isinstance(stat, bool) for stat in stats):
        return "All stats should be integers"

    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"

    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"

    if sum(stats) != 7:
        return "The character should start with 7 points"

    strength_bar = full_dot * strength + empty_dot * (10 - strength)
    intelligence_bar = full_dot * intelligence + empty_dot * (10 - intelligence)
    charisma_bar = full_dot * charisma + empty_dot * (10 - charisma)

    return (
        f"{character_name}\n"
        f"STR {strength_bar}\n"
        f"INT {intelligence_bar}\n"
        f"CHA {charisma_bar}"
    )


print(create_character('ren', 4, 2, 1))
