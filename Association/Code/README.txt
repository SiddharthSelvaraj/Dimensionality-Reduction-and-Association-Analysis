Install Python3

Step I. Run the command:
python apriori.py

Step II. File Name:
Enter the name of the file: associationruletestdata.txt

Step III. Minimum support value:
Enter the minimum support value: 50

Step IV. Confidence percentage:
Enter confidence percentage: 70

Step V. Template(1,2 or 3)
Enter the template number: 1

Step VI. Depending on the template number enter the parameters
Enter the first parameter: RULE
Enter the second parameter: ANY
Enter the third parameter: G59_Up

python3 apriori.py
Enter the name of the file: a.txt
Enter the minimum support value: 50
Support is set to be 50%
number of length-1 frequent itemsets: 109
number of length-2 frequent itemsets: 63
number of length-3 frequent itemsets: 2
number of all lengths frequent itemsets: 174
Enter confidence percentage: 70
The total rules generated: 117
Enter the template number: 1
Enter the first parameter: body
Enter the second parameter: 1
Enter the third parameter: g59_up,G10_down
Final set of rules:
{'G13_DOWN->G59_UP', 'G82_DOWN->G72_UP,G59_UP', 'G38_DOWN->G10_DOWN', 'G72_UP->G59_UP,G82_DOWN', 'G87_UP->G59_UP', 'G72_UP,G96_DOWN->G59_UP', 'G82_DOWN->G59_UP', 'G47_UP->G10_DOWN', 'G6_UP->G59_UP', 'G10_DOWN->G59_UP', 'G70_DOWN->G10_DOWN', 'G72_UP->G59_UP', 'G1_UP->G59_UP', 'G28_DOWN->G59_UP', 'G96_DOWN->G72_UP,G59_UP', 'G1_UP->G10_DOWN', 'G72_UP,G82_DOWN->G59_UP', 'G88_DOWN->G59_UP', 'G38_DOWN->G59_UP', 'G88_DOWN->G10_DOWN', 'G32_DOWN->G59_UP', 'G96_DOWN->G59_UP', 'G94_UP->G10_DOWN', 'G28_DOWN->G10_DOWN'}
Total number of final rules: 24