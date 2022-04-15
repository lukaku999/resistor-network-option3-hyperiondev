import bracket_functions

#test values from edabit
text1 = "(2, 3, 6)"
text2 = "[10, 20, [30, (40, 50), 60, (70, 80)], 90]"
text3 = "(1, [12, 4, (1, [10, (2, 8)])])" #on edabit it says the answer is 5.4 when running this code, but the output is 4.4 which the correct answer
text4 = "([10, 15], (5, 6, 5))"
text5 = "[22, 6, (10, 18, [33, 15]), (10, [63, 50], 45)]"
text6 = "[([(470, 1000), 330], 470), 680]"
text7 = "([([(470, 680), 330], 1000), 470], 680)"
text8 = "(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])"

def update_resistance_for_all(text):
    bracket_data = bracket_functions.get_all_bracket_children(text)
    level = bracket_data['highest_level']
    result = 0

    while level >= 0:
        bracket_functions.update_resistance(bracket_data, level)
        level = level - 1

    #the first object is the outer most bracket. Its resistance is the overall resistance of the circuit
    return bracket_data['all_brackets'][0].resistance


print("resistor equation: " + text1, 'resistance: ' + str(update_resistance_for_all(text1)))
print("resistor equation: " + text2, 'resistance: ' + str(update_resistance_for_all(text2)))
print("resistor equation: " + text3, 'resistance: ' + str(update_resistance_for_all(text3)))
print("resistor equation: " + text4, 'resistance: ' + str(update_resistance_for_all(text4)))
print("resistor equation: " + text5, 'resistance: ' + str(update_resistance_for_all(text5)))
print("resistor equation: " + text6, 'resistance: ' + str(update_resistance_for_all(text6)))
print("resistor equation: " + text7 , 'resistance: ' + str(update_resistance_for_all(text7)))
print("resistor equation: " + text8, 'resistance: ' + str(update_resistance_for_all(text8)))
