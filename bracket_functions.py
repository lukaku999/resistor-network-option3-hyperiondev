import bracket_class

# class for each bracket (applicable for both series and parallel)
def get_all_bracket_children(text):
    r0 = bracket_class.resistor(text)
    highest_level = 0
    all_brackets = []
    all_brackets.append(r0)
    continue_finding_children = True

    while continue_finding_children:
        prev_all_bracket_count = len(all_brackets)

        filtered_brackets = get_brackets_for_highest_level(all_brackets, highest_level)

        all_brackets = find_children_bracket_for_highest_level(all_brackets, filtered_brackets, highest_level + 1)

        continue_finding_children = False if prev_all_bracket_count == len(all_brackets) else True
        highest_level = highest_level + 1

    return {"highest_level": highest_level - 1, "all_brackets": all_brackets}


def update_resistance_inside_object(bracket_data, bracket, values):
    bracket.resistance = bracket.calculate_resistance(values)
    for index in range(len(bracket_data['all_brackets'])):
        if bracket_data['all_brackets'][index].id == bracket.id:
            bracket_data['all_brackets'][index] = bracket


def update_resistance(bracket_data, level):
    filtered_brackets = get_brackets_for_highest_level(bracket_data['all_brackets'], level)

    for bracket in filtered_brackets:
        if bracket.level == bracket_data['highest_level']:
            update_resistance_inside_object(bracket_data, bracket, bracket.children['int'])
        else:
            bracket_values = []

            for child_bracket in bracket.children['brackets']:
                for i in bracket_data['all_brackets']:

                    if child_bracket.id == i.id:
                        bracket_values.append(i.resistance)
            values = bracket_values + (bracket.children['int'])
            update_resistance_inside_object(bracket_data, bracket, values)

    return bracket_data


def find_children_bracket_for_highest_level(all_brackets, brackets, child_level):
    for bracket in brackets:

        child_bracket = bracket.find_children(child_level)

        if (bool(child_bracket)):
            for index, id in enumerate(child_bracket):
                all_brackets.append(child_bracket[id])
            # all_brackets.append(brackets)

    return all_brackets


def get_brackets_for_highest_level(all_brackets, highest_level):
    filtered_brackets = []
    for bracket in all_brackets:
        if bracket.level == highest_level:
            filtered_brackets.append(bracket)
    return filtered_brackets


