# ex_2_matrix_modification_exercises_multidimensional_lists-1

Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's rows - N. You will get elements for each column on the following N lines, separated with a single space. You will be receiving commands in the following format:
•	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
•	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.

Input
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END

Output
6 2 3
4 3 6
7 8 9
