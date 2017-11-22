## Train an Swedish Dependency Parser for Stanford CoreNLP

 - 1. Download Stanford CoreNLP 3.8.0 from https://stanfordnlp.github.io/CoreNLP/index.html#download
 - 2. Download training data for Swedish dependency parsing from http://universaldependencies.org
 - 3. Run the script ```clean_conllu.py``` to remove all comments from the conllu file. Make sure to edit the filename for your .conllu file here before running. 
 - 4. Go to https://github.com/klintan/wiki-word2vec and follow the instructions to create an embeddings.txt file.
 - 5. Run the train.sh script (or copy paste the one liner from the script to the terminal.) Make sure your path to the downloaded CoreNLP package is correct before you run the script. Make sure to match the embeddings dimensions of your trained embeddings file and the -embeddingSize flag.

This model is using the english default TLP file or TreebankLanguagePack. It might not be the best one. Further to improve the training there are bunch of arguments/hyperparameters to be set for training which might be more appropriate than the default one. 

Samples of TLPs are available here: https://github.com/stanfordnlp/CoreNLP/tree/master/src/edu/stanford/nlp/trees/international


#### Important
Before testing the model I noticed there is a "bug" in the model, before it can be loaded it needs to be in the proper format "<word> <vector>". However because of errors in tokenizing abbrevation, we get "<word/letter> <word/letter> <vector>" and tries to parse the second part of the abbrevation as a number, which of course fails. 

A quick fix for this is by adding "." between the words so you get the proper format "<word> <vector>". After this you should be able to use or test the model using the test cmd in the test.sh file.


Let me know if anything is missing or create a pull request for any changes. 

