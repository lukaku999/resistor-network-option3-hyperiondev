import bracket_functions


text = '(1, [12, 4, (1, [10, (2, 8)])], [2, 3],2)'
#text = '[12, 4, (1, [10, (2, 8)]), [2, 4]]'

def update_resistance_for_all(text):
    bracket_data = bracket_functions.get_all_bracket_children(text)
    level = bracket_data['highest_level']
    result = 0

    while level >= 0:
        bracket_functions.update_resistance(bracket_data, level)
        level = level - 1

    return bracket_data['all_brackets'][0].resistance


print(update_resistance_for_all(text))