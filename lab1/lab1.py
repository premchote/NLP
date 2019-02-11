"""
Title: Lab1
Author: Prem Chotepanit
Registration number: 180127900
OS: Window10
Python version: 3.6.8
"""

import sys,os,random,regex as re
from numpy.random import choice

random.seed(777)
dir_name = sys.argv[1]
print(dir_name)
Path = os.path.dirname((os.path.realpath(__file__)))\
    +'\\'+dir_name\
    +'\\'+"txt_sentoken"
    #Accessing folder "review_palarity"
Class = os.listdir(Path)
"""
Part 1: Choosing training data and testing data 
- using random 800 file names for training data and 200 for testing data
"""
#Training Data
Training_pos_data = []
Training_neg_data = []
random.sample(range(1, 100), 3)

"""
Firstly, the program randoms a file with its path for 800 times 
for both the positive class.
Then, it appends them to training data.
"""
text_class = 'pos' #class positive
pos_path = Path + '\\' + text_class
pos_files = set(os.listdir(pos_path)) 
Training_pos_data = set(random.sample(pos_files, 800))
Testing_pos_data = pos_files - Training_pos_data #filtering training data from total files
"""
Next, the program does the same process with negative files
"""

text_class = 'neg' #class negative
neg_path = Path + '\\' + text_class
neg_files = set(os.listdir(neg_path)) 
Training_neg_data = set(random.sample(neg_files, 800))
Testing_neg_data = neg_files - Training_neg_data #filtering training data from total files
print(neg_path+'\\'+list(Testing_neg_data)[0])
"""
Part 2: Define the function which returns bag of words from
an input file.
"""
def Generate_BOF(file):
    f = open(file, "r")
    text = f.read()
    output = {}
    text = re.sub("[^\w']"," ",text).split()
    for word in text:
	    if word in output:
	        output[word] += 1
	    else:
	        output[word] = 1
    return output
## Input: a text file's name with path
## Output: {"there's": 1, 'a': 10, 'scene': 3, 'early': 1,...


"""
Part3: the program combines training data and shuffle it
Then, it initials W as null dictionary and y_train.
"""
X_train = list(Training_pos_data.union(Training_neg_data))
Y_train = [y in pos_files for y in X_train] 
W ={}

"""
Part4: the program makes the repeating learing process
to adjust W.
"""
iteration = 1000 #set the number of repeating time.
#for i in range(iteration)
#random.shuffle(x) random index of list 
#for doc in Training_pos_data