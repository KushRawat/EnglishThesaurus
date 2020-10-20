import json
from difflib import get_close_matches

data = json.load(open("data.json"))  

def translate(word):

    word = word.lower()
    
    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0:
        
        yn = input(f"Did you mean {get_close_matches(word, data.keys(), n = 2, cutoff = 0.8)[0]} instead? Enter Y if yes, or N if no: ")
        
        if yn == "Y":
            return data[get_close_matches(word, data.keys(), n = 2, cutoff = 0.8)[0]]
        elif yn == "N":
            return "Word does not exist. Please double check it."
        else:
            return "We didn't understand your entry."
    
    else:
        return "Word does not exist. Please double check it"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
