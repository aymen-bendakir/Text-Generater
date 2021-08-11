from nltk.tokenize import regexp_tokenize
from nltk import trigrams
from collections import Counter
import random


def generate_sentence(bigrams_):
    """takes as input the bigram dict of the form {("token1 token2", "token3"): count}, and generates a coherent sentence that is more than 5 tokens long"""
    while True:  # choosing the first two tokens
        sentence = random.choice(tuple(bigrams_.keys()))[0]  # [0] index of the bigram tuples has two tokens in it
        if sentence[0].isupper() and sentence.split()[0][-1] not in ".?!":  # the first letter must be upCase and the first token shouldn't end with punctuation
            break
    i = 2  # number of tokens in the sentence
    while True:  # keep adding tokens to the sentence
        for key in bigrams_.most_common():  # trying all high probable tuples (i.e. keys with higher counts). We're iterating over a list of the form [(("token1 token2", "token3"), count)] ordered from highest count to lower
            if key[0][0] == ' '.join(sentence.split()[-2:]):  # if "token1 token2" == the last two tokens from the sentence
                sentence += " " + key[0][1]  # add the tail of this key i.e. token3 to the sentence
                i += 1  # increment the number of tokens in the sentence
                break  # we found our tail, so no need to continue the loop
        if i >= 5 and sentence[-1] in ".?!":  # IF the sentence has 5 tokens or more AND ends with punctuation THEN return the sentence
            return sentence


# Write your code here
file = open("corpus.txt", "r", encoding="UTF-8")
all_tokens = regexp_tokenize(file.read(), r"[^\s]+")  # get the tokens from the corpus file
file.close()

all_bigrams = Counter([(x[0] + " " + x[1], x[2]) for x in trigrams(all_tokens)])  # bigrams of the form {("token1 token2", "token3"): count}

print("Press enter to print a sentence, or 'exit' to exit the program. Enjoy :)")
while True:  # print the generated sentences
    if input("> ") == "exit":
        break
    print("  " + generate_sentence(all_bigrams))
print("Bye!")
