import os
import string

# Prompt the user for the path to a file
# Trying to open a file in read mode when the file doesn't exist will cause 
# program to crash!
# If the file doesn't exist, display an error message and quit the program
def file_data_and_path(filename):
    if os.path.isfile(filename):
       path = os.path.dirname(filename)
       with open(filename, "rU") as f:
            lines = f.readlines()
       return lines, path
    else:
       print ("Error: cannot fine "), filename
       return None, None


# Main Function of the program
# Prompt user to input the path of the two input files
f_name1 = raw_input("Path to a file to parse: ").strip()
f_name2 = raw_input("Path to an encoded message: ").strip()

lines1, path1 = file_data_and_path(f_name1)
lines2, path2 = file_data_and_path(f_name2)


#print lines1
sortedLines1 = sorted(lines1, key = lambda value: value[2])
#print sortedLines1

newLines1 = [i.split(' ', 1)[0] for i in sortedLines1]

# Create new list to store the ord values for the newLines1
newLines1_ord = []
for i in range(len(newLines1)):
    newLines1_ord.append(ord(newLines1[i]))

print newLines1_ord

# Convert the string list into char list
newLines2 = []
for i in lines2:
    newLines2.extend(i)


# Convert newLines2 into ASCII
newLines2_ord1 = [newLines1_ord[0] if x == 'A' else x for x in newLines2]
newLines2_ord2 = [newLines1_ord[1] if x == 'B' else x for x in newLines2_ord1]
newLines2_ord3 = [newLines1_ord[2] if x == 'C' else x for x in newLines2_ord2]
newLines2_ord4 = [newLines1_ord[3] if x == 'D' else x for x in newLines2_ord3]
newLines2_ord5 = [newLines1_ord[4] if x == 'E' else x for x in newLines2_ord4]
newLines2_ord6 = [newLines1_ord[5] if x == 'F' else x for x in newLines2_ord5]
newLines2_ord7 = [newLines1_ord[6] if x == 'G' else x for x in newLines2_ord6]
newLines2_ord8 = [newLines1_ord[7] if x == 'H' else x for x in newLines2_ord7]
newLines2_ord9 = [newLines1_ord[8] if x == 'I' else x for x in newLines2_ord8]
newLines2_ord10 = [newLines1_ord[9] if x == 'J' else x for x in newLines2_ord9]
newLines2_ord11 = [newLines1_ord[10] if x == 'K' else x for x in newLines2_ord10]
newLines2_ord12 = [newLines1_ord[11] if x == 'L' else x for x in newLines2_ord11]
newLines2_ord13 = [newLines1_ord[12] if x == 'M' else x for x in newLines2_ord12]
newLines2_ord14 = [newLines1_ord[13] if x == 'N' else x for x in newLines2_ord13]
newLines2_ord15 = [newLines1_ord[14] if x == 'O' else x for x in newLines2_ord14]
newLines2_ord16 = [newLines1_ord[15] if x == 'P' else x for x in newLines2_ord15]
newLines2_ord17 = [newLines1_ord[16] if x == 'Q' else x for x in newLines2_ord16]
newLines2_ord18 = [newLines1_ord[17] if x == 'R' else x for x in newLines2_ord17]
newLines2_ord19 = [newLines1_ord[18] if x == 'S' else x for x in newLines2_ord18]
newLines2_ord20 = [newLines1_ord[19] if x == 'T' else x for x in newLines2_ord19]
newLines2_ord21 = [newLines1_ord[20] if x == 'U' else x for x in newLines2_ord20]
newLines2_ord22 = [newLines1_ord[21] if x == 'V' else x for x in newLines2_ord21]
newLines2_ord23 = [newLines1_ord[22] if x == 'W' else x for x in newLines2_ord22]
newLines2_ord24 = [newLines1_ord[23] if x == 'X' else x for x in newLines2_ord23]
newLines2_ord25 = [newLines1_ord[24] if x == 'Y' else x for x in newLines2_ord24]
newLines2_ord26 = [newLines1_ord[25] if x == 'Z' else x for x in newLines2_ord25]

# Decode newLines_ord26 
for i in range(len(newLines2_ord26)):
    if newLines2_ord26[i] != ' ': 
       x = chr(newLines2_ord26[i])
       print x,
    else: 
       x = newLines2_ord26[i]
       print x,

