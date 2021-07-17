import json
from difflib import get_close_matches

data = json.load(open("data.json"))  

def translate(word):

    word = word.lower() #dealing with case-sensitive words
    
    if word in data:
        return data[word]
    
    elif word.title() in data: #case:if word is a proper noun
        return data[word.title()]

    elif word.upper() in data: #case:if word is an acronym
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0: #case:similar words --> user enters bookk/boook instead of book
        # help(get_close_matches) --> get_close_matches(word, possibilities, n=3, cut0ff=0.6)
        yn = input(f"Did you mean {get_close_matches(word, data.keys(), n = 2, cutoff = 0.8)[0]} instead? Enter Y if yes, or N if no: ")
        
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys(), n = 2, cutoff = 0.8)[0]]
        elif yn == "N" or yn == "n":
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
