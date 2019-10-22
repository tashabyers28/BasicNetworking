# Demo testing for Basic Networking 10/22/19

#V is the number of grapevines that will fit in the row.
#R is the length of rows, in feet.
#E is the amount of space, in feet, used by an end-post assembly.
#S is the space between vines, in feet.

#Ask what the length of the row, in feet
R = float(input('Enter the length of the row in feet: '))

#Ask what is the amount of space used by an end-post assembly, in feet
E = float(input('Enter the amount of space used by an end-post assembly in feet: '))

#Ask what is the amount of space between the vines, in feet
S = float(input('Enter the amount of space between vines in feet: '))

#Once the input data has been entered, the program should calculate and display the number of grapevines that will fit in the row.

V = (R - 2*E)/S

Print('This is the number of grapevines that will fit into the row:', V)
