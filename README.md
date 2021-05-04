# POS-Tagger
This program noun tagging algorithm that uses features of an input file and produces a file 
consisting of feature value pairs for use with the maxent trainer and classifier. The features
I tried were the previous word, its BIO tag, its POS tag, the next word, its BIO tag, its POS tag,
the following word after the next, its BIO tag, its POS tag, the previous word after the first previous, 
its BIO tag, its POS tag, and whether it had a capital letter. 
Author: Reema Amhaz 

I found that these were the most important features after testing different features
such as numbers, etc. 

### My results: 
31514 out of 32853 tags correct
  accuracy: 95.92
8378 groups in key
8902 groups in response
7625 correct groups
  precision: 85.65
  recall:    91.01
  F1:        88.25

## How to run the program:
1. python ra2911-HW5.py WSJ_02-21.pos-chunk WSJ_24.pos WSJ_23.pos
2. cd MAX_ENT_FILES
3. java -Xmx16g -cp .:maxent-3.0.0.jar:trove.jar MEtrain ../training.feature model.chunk      
4. java -Xmx16g -cp .:maxent-3.0.0.jar:trove.jar MEtag ../test.feature model.chunk response.chunk
5. cd ..
6. python MAX_ENT_FILES/score.chunk.py WSJ_24.pos-chunk MAX_ENT_FILES/response.chunk
