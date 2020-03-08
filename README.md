# ProfanityDegree
A simple python program to check degree of profanity in a sentence.

The data is taken from a file facebook_comments.txt. The file has to be provided.
The data is read line by line and then converted into a dataframe.

The list of the profane word is downloaded from 'https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt'

The comments is cleaned in 3 steps: 
1. Punctuations like -> !@#%^!@ are removed
2. Stop words are removed -> myself, here, there, me, or, etc. Removing stop words helps in creating a list of sentences with only meaningful words which can help in determing profanity and sentiment in a more robust way.
3. Stemming and Lemmatizing-> stemming and lemmatizing helps in removing tenses and parts of words that donot give any necessary meanings as such like removing -ing or -ed from a word

The degree of profanity is calculated as:

#### Degree of Profanity = sum(number of profane words in the sentence)/ total number of words

###### Some assumptions are made and the degree of profanity can be calculated in a more robust way in these ways:
1. Assigning a degree of profanity to each profane word.
2. Considering the words that come before and after the profane word.
3. Using Machine Leaning to train a model based on the data on what senetences did people think were more profane than others.
4. Considering the emojies used in the text/comment can help in finding more about the intent of the comment.
