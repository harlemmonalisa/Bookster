import requests
import random

#source where random words will be pulled from
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

#pulling random words
response = requests.get(word_site)
WORDS = response.content.splitlines()

#execute random word
random_word = random.choice(WORDS)
#convert to string type
string_word = str(random_word)
#to omit the extra b letter at the front
final_random_word = string_word[1:]

return final_random_word