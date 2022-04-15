import uuid

#the resistor class is an class the describes resistors whose values need to be calculated within brackets
class resistor:
    def __init__(self, text):
        #self text refers to text inside brackets enclosures
        self.children = {}
        self.level = 0
        self.id = uuid.uuid4()
        self.resistance = "N/A"
        self.resistor_type = "series" if text[0] == '(' else "parallel"
        self.text = text[1:-1]
        self.parent = ""

    def calculate_series(self, values):
        # calculates series resistors
        overall_value = 0
        for value in values:
            overall_value = value + overall_value
        return overall_value

    def calculate_parallel(self, values):
        # calculates parallel resistors
        overall_value = 0
        for value in values:
            overall_value = 1 / value + overall_value

        return 1 / overall_value

    def calculate_resistance(self, values):
        # determines if resistor is series or parallel, then calculates the resistance
        if self.resistor_type == 'series':
            return self.calculate_series(values)
        elif self.resistor_type == 'parallel':
            return self.calculate_parallel(values)
        else:
            return "entered wrong resistor_type"

    def obtain_bracket_indexes(self):
        # determines the index of child brackets from self.text(round or square brackets).
        bracket_array = []
        bracket_object = {}
        for index, bracket in enumerate(self.text):

            if bracket == '(' or bracket == '[':
                bracket_array.append(index)
            if bracket == ')' or bracket == ']':
                try:
                    bracket_object[bracket_array.pop()] = index
                except IndexError:
                    print('Too many closing parentheses')

        if bracket_array:  # check if stack is empty afterwards
            print('Too many opening parentheses')

        return bracket_object

    def find_children_brackets_indexes(self):
        #the method determines all children indexes (does not determine children that is a number) with brackets text within current bracket
        result = []
        children_brackets = []
        bracket_indexes = self.obtain_bracket_indexes()
        for i, c in enumerate(bracket_indexes):
            if i == 0:
                children_brackets.append([c, bracket_indexes[c]])
            else:
                for index in range(len(children_brackets)):
                    if c < children_brackets[index][0] and bracket_indexes[c] > children_brackets[index][1]:
                        children_brackets[index] = [c, bracket_indexes[c]]
                    else:
                        children_brackets.append([c, bracket_indexes[c]])
                        break
        [result.append(x) for x in children_brackets if x not in result]
        return result

    def find_children(self, child_level):
        #finds all children brackets and creates a resistor object that. The resistance for child values will be calculated and later updated within this object. Afterwards, all values will be used to determine the resistance value
        translation = 0
        string = self.text
        child_brackets_index = self.find_children_brackets_indexes()
        children_object_to_return = {}
        children_bracket_array = []
        for child_bracket in child_brackets_index:
            bracket_id = uuid.uuid4()
            child_bracket_text = self.text[child_bracket[0]: child_bracket[1] + 1]

            bracket_object = resistor(child_bracket_text)
            bracket_object.id = bracket_id
            bracket_object.parent = self.id
            bracket_object.level = child_level
            children_object_to_return[bracket_id] = bracket_object
            children_bracket_array.append(bracket_object)
            start = child_bracket[0] + translation
            stop = child_bracket[1] + translation
            string = string[0: start:] + string[stop + 1::]
            translation = start - stop - 1

        #finds all the children within bracket enclosure that are numbers
        self.children['brackets'] = children_bracket_array
        children_int = string.split(',')
        self.children['int'] = []

        for child in children_int:
            if (child.strip().isnumeric()):
                self.children['int'].append(int(child))

        return children_object_to_return
