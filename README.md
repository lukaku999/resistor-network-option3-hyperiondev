# resistor-network-option3-hyperiondev

*************************************
Calculating resistors

Resistors are electrical components that add resistance to a circuit. Resistance is measured in ohms. When resistors are connected in series, the total resistance is merely the sum of the individual resistances:

Rtotal = R1 + R2 + R3 + ...
When resistors are connected in parallel, the reciprocal of the total resistance is equal to the sum of the reciprocals of the individual resistances:

1/(Rtotal) = 1/R1 + 1/R2 + 1/R3 + ...
Let's specify that series resistors be designated by enclosing them in parentheses, and parallel resistors by enclosing them in square brackets. Now we can calculate the equivalent resistance of the network:

(2, 3, 6) = 11 ohms
[2, 3, 6]= 1 ohm
Nesting these structures in the same way tuples and arrays are nested allows us to model complex resistor networks.

Create a function that takes a nested network as a string and returns the equivalent resistance of the network. Round results to the nearest tenth of an ohm.

Examples
resist("(10, [20, 30])") ➞ 22.0
// 10 in series with [20, 30] in parallel.

resist("[10, (20, 30)]") ➞ 8.3
// 10 in parallel with (20, 30) in series.

resist("([10, 20], (30, 40))") ➞ 76.7
// [10, 20] in parallel in series with (30, 40) in series.

resist("(1, [12, 4, (1, [10, (2, 8)])])") ➞ 3.0

resist("(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])") ➞ 10

********************************************************************

Running the code

1. Download the zip file or clone the project
2. In the root folder open main.py
3. Run Program. The program will ran the for following example:

text1 = "(2, 3, 6)"
text2 = "[10, 20, [30, (40, 50), 60, (70, 80)], 90]" #on edabit it says the answer is 5.4 when running this code, but the output is 4.4 
text3 = "(1, [12, 4, (1, [10, (2, 8)])])" which the correct answer
text4 = "([10, 15], (5, 6, 5))"
text5 = "[22, 6, (10, 18, [33, 15]), (10, [63, 50], 45)]"
text6 = "[([(470, 1000), 330], 470), 680]"
text7 = "([([(470, 680), 330], 1000), 470], 680)"
text8 = "(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])"

4. If you want to enter your own values, run the function: update_resistance_for_all(text) in main.py.
