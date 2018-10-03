import numpy as np
import sys
from itertools import combinations

#citations
#https://docs.python.org/3.6/library/stdtypes.html?highlight=set#set
#https://docs.python.org/3/tutorial/datastructures.html
#https://docs.python.org/3/library/itertools.html?highlight=itertools#itertools.combinations

#Template 1 input
def template1():
    finalrules = set()
    #Getting the input parameters for template 1
    parameter1 = (input('Enter the first parameter: '))
    parameter2 = (input('Enter the second parameter: '))
    paremeter3 = (input('Enter the third parameter: ').upper().split(','))

    #Checking valid inputs
    if parameter1.upper() not in ('RULE','BODY','HEAD'):
        sys.exit("Invalid Parameter 1")

    #Checking in the rules generated based on the parameters and adding it to final rules
    for r in rules:
        #Splitting the rule into headpart and bodypart
        headpart = r.split('->')[0].split(',')
        bodypart = r.split('->')[1].split(',')
        headpart_set = set(headpart)
        bodypart_set = set(bodypart)

        #Checking if the first parameter is RULE or HEAD or BODY and creating a newset based on it
        if parameter1.upper() == 'RULE':
            newset = headpart_set.union(bodypart_set)
        elif parameter1.upper() == 'BODY':
            newset = bodypart_set
        elif parameter1.upper() == 'HEAD':
            newset = headpart_set

        #Checking if the second parameter is ANY or NONE or ONE and comparing the newset with the third parameter
        #and generating final rules
        if parameter2.upper() == 'ANY' and len(set(paremeter3).intersection(newset)) > 0:
            finalrules.add(r)
        elif parameter2.upper() == 'NONE' and len(set(paremeter3).intersection(newset)) == 0:
            finalrules.add(r)
        elif parameter2.upper() == '1' and len(set(paremeter3).intersection(newset)) == 1:
            finalrules.add(r)
    return finalrules

#Template 2 input
def template2():
    finalrules = set()
    #Getting the input parameters for template 2
    parameter1 = (input('Enter the first parameter: '))
    parameter2 = (input('Enter the second parameter: '))

    #Checking valid inputs
    if parameter1.upper() not in ('RULE','BODY','HEAD'):
            sys.exit("Invalid Parameter 1")
    #Splitting the rule into headpart and bodypart
    for r in rules:
        headpart = r.split('->')[0].split(',')
        bodypart = r.split('->')[1].split(',')
        headpart_set = set(headpart)
        bodypart_set = set(bodypart)

        #Checking if the first parameter is RULE or HEAD or BODY and creating a newset based on it
        if parameter1.upper() == 'RULE':
            newset = headpart_set.union(bodypart_set)
        elif parameter1.upper() == 'BODY':
            newset = bodypart_set
        elif parameter1.upper() == 'HEAD':
            newset = headpart_set

        #Checking if the length of the rule is equal to the second parameter then adding it to the final list
        length_parm2 = int(parameter2)
        if len(newset) >= length_parm2:
            finalrules.add(r)
    return finalrules

#Finding frequent itemset
def findfrequent(gene_data,data_count,support_threshold):
    frequent_itemset = {}
    frequent_itemset_list = []
    for x in gene_data:
        if (gene_data[x]/data_count)>=(support_threshold/100):
            frequent_itemset[x] = gene_data[x]
            frequent_itemset_list.append(x.replace(" ","").replace("]","").replace("[","").replace("'","").split(","))
    return frequent_itemset,frequent_itemset_list

#Finding the count of the combinations in the data
def getCount(gene,new_combinations):
    gene_count = {}
    for c in new_combinations:
        for g in range(len(gene)):
            if set(c) < set(gene[g]):
                if str(c) in gene_count:
                    gene_count[str(c)] = gene_count[str(c)] + 1
                else:
                    gene_count[str(c)] = 1
    return gene_count

#Opening and reading the file line by line
file_name = input("Enter the name of the file: ")
file = open(file_name, "r")
lines = file.readlines()

#Getting the Support Threshold and printing it as per the report format
support_value = int(input("Enter the minimum support value: "))
print("Support is set to be "+str(support_value)+"%")

#Initializing gene matrix, gene_data dictionary, global_freq_itemset_list and global_freq_itemset_dict
gene_matrix = []
gene_data = {}
global_freq_itemset_list = []
global_freq_itemset_dict = {}

# splittng the line into individual data
for line in lines:
    data = line.strip().replace(" ","-").split("\t")
    gene_matrix.append(data)


#Converting it into array and adding the prefix to get it in the desired format
gene = np.asarray(gene_matrix)
rows = gene.shape[0]
cols = gene.shape[1]

for x in range(0, rows):
    for y in range(0, cols):
        if(y != cols-1):
            gene[x,y] = "G" + str(y+1) + "_" + gene[x,y]


#Storing the itemsets of length one in a dictionary
for x in range(0, rows):
    for y in range(0, cols):
        if(str((gene[x,y]).split(" ")) in gene_data):
            gene_data[str((gene[x,y]).split(" "))] = gene_data[str((gene[x,y]).split(" "))] + 1
        else:
            gene_data[str((gene[x,y]).split(" "))] = 1

#Getting the frequent itemsets of length 1 as a dictionary and a list
frequent_itemset,frequent_itemset_list = findfrequent(gene_data,rows,support_value)

#Updating the itemsets in a global list and dictionary to get the total at end
global_freq_itemset_dict.update(frequent_itemset)
for x in frequent_itemset_list:
            global_freq_itemset_list.append(x)

#Printing the count of frequent itemsets of length 1
print("number of length-1 frequent itemsets: "+str(len(frequent_itemset_list)))

itemset_length = 2

while len(frequent_itemset_list) != 0:
    #Sorting the itemsets and comparing all the elements except the last one so that we can create new
    #itemset by joining two similar itemsets and removing duplicates using set
    new_combinations = []
    sorted_freq_itemset_list=sorted(frequent_itemset_list)
    for i in range(len(sorted_freq_itemset_list)):
        for j in range(i+1, len(sorted_freq_itemset_list)):
            if(sorted_freq_itemset_list[i][:itemset_length-2] == sorted_freq_itemset_list[j][:itemset_length-2]):
                new_combinations.append(sorted(set(sorted_freq_itemset_list[i]).union(set(sorted_freq_itemset_list[j]))))
    #Checking the count of these itemsets in the given data
    gene_count = getCount(gene,new_combinations)

    #Getting the frequent itemsets of length (itemset_length) as a dictionary and a list
    frequent_itemset,frequent_itemset_list = findfrequent(gene_count,rows,support_value)
    if len(frequent_itemset_list) != 0:
        #Updating the itemsets in a global list and dictionary to get the total at end
        global_freq_itemset_dict.update(frequent_itemset)
        for x in frequent_itemset_list:
            global_freq_itemset_list.append(x)
        #Printing the freqent itemset of itemset_length
        print("number of length-"+str(itemset_length)+" frequent itemsets: "+str(len(frequent_itemset_list)))
    itemset_length = itemset_length + 1

#Printing the count of total frequent itemsets
print("number of all lengths frequent itemsets: "+str(len(global_freq_itemset_list)))

rules = set()
head = set()
body = set()
finalrule1 = set()
finalrule2 = set()
finalrules = set()
rule_count = 0
#getting the confidence value
confidence_value = int(input('Enter confidence percentage: '))
#Generating the rules
for x in global_freq_itemset_list:
    length = 1
    while (length<=len(x)):
        for comb in set(combinations(x,length)):
            confidence = global_freq_itemset_dict[str(x)]/global_freq_itemset_dict[str(list(comb))]
            if confidence >=confidence_value/100:
                #Removing sets with empty body part
                if(len(list(set(x) - set(comb)))!=0):
                    rule = (",".join(list(comb))) + "->" + (",".join(list(set(x)-set(comb))))
                    rule_count = rule_count + 1
                    rules.add(rule.upper())
                    head.add(str(list(comb)))
                    body.add(str(list(set(x)-set(comb))))
        length = length + 1;

print("The total rules generated: " + str(rule_count))

template_number = int(input('Enter the template number: '))
if template_number == 1:
    finalrules=template1()

elif template_number == 2:
    finalrules=template2()

elif template_number == 3:
    parameter1 = input('Enter the first parameter: ').upper()
    if 'OR' in parameter1:
        first = int(parameter1.split('OR')[0]);
        second = int(parameter1.split('OR')[1]);
        if (first == 1):
            print('Enter template 1 parameters')
            finalrule1 = template1()
        elif(first == 2):
            print('Enter template 2 parameters')
            finalrule1 = template2()
        else:
            print("First part is invalid")

        if (second == 1):
            print('Enter template 1 parameters')
            finalrule2 = template1()
        elif(second == 2):
            print('Enter template 2 parameters')
            finalrule2 = template2()
        else:
            print("First part is invalid")

        finalrules = finalrule1.union(finalrule2)

    elif 'AND' in parameter1:
        first = int(parameter1.split('AND')[0]);
        second = int(parameter1.split('AND')[1]);
        if (first == 1):
            print('Enter template 1 parameters')
            finalrule1 = template1()
        elif(first == 2):
            print('Enter template 2 parameters')
            finalrule1 = template2()
        else:
            print("First part is invalid")

        if (second == 1):
            print('Enter template 1 parameters')
            finalrule2 = template1()
        elif(second == 2):
            print('Enter template 2 parameters')
            finalrule2 = template2()
        else:
            print("Second part is invalid")

        finalrules = finalrule1.intersection(finalrule2)
else:
    print("The template number is invalid")

print('Final set of rules: ')
print(finalrules)
print("Total number of final rules: " + str(len(finalrules)))
