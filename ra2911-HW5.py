import sys, string

# This program noun tagging algorithm that uses features of an input file and produces a file 
# consisting of feature value pairs for use with the maxent trainer and classifier. The features
# I tried were the previous word, its BIO tag, its POS tag, the next word, its BIO tag, its POS tag,
# the following word after the next, its BIO tag, its POS tag, the previous word after the first previous, 
# its BIO tag, its POS tag, and whether it had a capital letter. 
# Author: Reema Amhaz 

#open the trainining and test files 
train = open(sys.argv[1]).readlines()
test = open(sys.argv[2]).readlines()
final = open(sys.argv[3]).readlines()

#create final and training results
output_train = open("training.feature", "w")
output_test = open("test.feature", "w")
output_final = open("WSJ_23.chunk", "w")

# to tag the training set with BIO tags
def word_features(sets, output):
    last = len(sets) - 1 
    output.write('\n')
    for s in range(1, len(sets)):
        # pre-process and set all the previous and next sets
        two_prev = []
        two_next = []
        next = []
        prev = sets[s - 1]
        if s != 1:
            two_prev = sets[s - 2]
        if s != last:
            next = sets[s + 1]
        if s != last and s != last-1:
            two_next = sets[s + 2]
        if not sets[s]:
            output.write("\n")
        else:        
            output.write(sets[s][0]+'\t'+'pos='+sets[s][1]+'\t')
            output.write('w='+sets[s][0]+'\t')
            # check if there is a previous set, tag those values
            if not prev:
                output.write('prev_pos=START'+'\t'+'prev_word=START'+'\t'+'prev_bio=O'+'\t')
            else:
                output.write('prev_pos='+ prev[1] +'\t'+'prev_word='+ prev[0]+'\t'+'prev_bio='+ prev[2]+'\t')
            # check if there is a second previous set, tag those values
            if not two_prev:
                output.write('prev_pos2=START'+'\t'+'prev_word2=START'+'\t'+'prev_bio2=O'+'\t')
            else:
                output.write('prev_pos2='+ two_prev[1] +'\t'+'prev_word2='+ two_prev[0]+'\t'+'prev_bio2='+ two_prev[2]+'\t')
            #check if there is a next set, tag those values
            if not next:
                output.write('next_pos=END'+'\t'+'next_word=END'+'\t'+'next_bio=O'+'\t')
            else:
                output.write('next_pos='+ next[1] + '\t'+'next_word='+ next[0]+'\t'+'next_bio='+ next[2]+'\t')
            # check if there is a second next set, tag those values  
            if not two_next:
                output.write('next_pos2=END'+'\t'+'next_word2=END'+'\t'+'next_bio2=O'+'\t')
            else:
                output.write('next_pos2='+ two_next[1] + '\t'+'next_word2='+ two_next[0]+'\t'+'next_bio2='+ two_next[2]+'\t')
            # check if it is uppercase     
            if sets[s][0][0].isupper():
                output.write('upper='+'1'+'\t')
            else:
                output.write('upper='+'0'+'\t')
            output.write(sets[s][2]+'\n')
# to tag the test set without BIO tags
def test_features(sets, outputs):
    last = len(sets) - 1 
    outputs.write('\n')
    for s in range(1, len(sets)):
        # pre-process and set all the previous and next sets
        two_prev = []
        two_next = []
        next = []
        prev = sets[s - 1]
        if s != 1:
            two_prev = sets[s - 2]
        if s != last:
            next = sets[s + 1]
        if s != last and s != last-1:
            two_next = sets[s + 2]
        
        if not sets[s]:
            outputs.write('\n')
        else:        
            outputs.write(sets[s][0]+'\t'+'pos='+sets[s][1]+'\t')
            outputs.write('w='+sets[s][0]+'\t')
            # check if there is a previous set, tag those values
            if not prev:
                outputs.write('prev_pos=START'+'\t'+'prev_word=START'+'\t')
            else:
                outputs.write('prev_pos='+ prev[1] +'\t'+'prev_word='+ prev[0]+'\t')
            # check if there is a second previous set, tag those values
            if not two_prev:
                outputs.write('prev_pos2=START'+'\t'+'prev_word2=START'+'\t')
            else:
                outputs.write('prev_pos2='+ two_prev[1] +'\t'+'prev_word2='+ two_prev[0]+'\t')
            #check if there is a next set, tag those values
            if not next:
                outputs.write('next_pos=END'+'\t'+'next_word=END'+'\t')
            else:
                outputs.write('next_pos='+ next[1] + '\t'+'next_word='+ next[0]+'\t')
            # check if there is a second next set, tag those values  
            if not two_next:
                outputs.write('next_pos2=END'+'\t'+'next_word2=END')
            else:
                outputs.write('next_pos2='+ two_next[1] + '\t'+'next_word2='+ two_next[0]+'\t')
            # check if it is uppercase       
            if sets[s][0][0].isupper():
                outputs.write('upper='+'1'+'\t')
            else:
                outputs.write('upper='+'0'+'\t')
            outputs.write('\n')

#append all sets to a list
def process_pos(file):
    set = []
    for line in file:
        if line.strip() == "":
            set.append([])
        else:
            token = line.split()
            if len(token) == 3:
                set.append(token)
            elif len(token) == 2:
                set.append(token)
    return set
                

#call the functions
train_set = process_pos(train)
word_features(train_set, output_train)
test_set = process_pos(test)
test_features(test_set, output_test)
final_set = process_pos(final)
test_features(final_set, output_final)