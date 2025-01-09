def main():
    book_path = "books/frankenstein.txt"
    text = getbook(book_path)
    num_words = wordcount(text)
    character_count_dict = charactercount(text)
    character_count_sorted = charactercount_sort(character_count_dict)
    
    print(f"xxxx Begin report of {book_path} xxxx")
    print(num_words, "words found in document")
    for item in character_count_sorted:
        print(f"The '{item['character']}' character appeared {item['number']} times")
    return print("xxxx Report over xxxx")

def getbook(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def wordcount(text):
    words = text.split()
    wordnumber = 0
    for f in words:
        wordnumber += 1
    return wordnumber

def charactercount(text):
    lowercased = text.lower()
    charactercounts = {}
    abc = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    for f in lowercased:
        if f in abc.split():
            if f in charactercounts:
                charactercounts[f] += 1
            else:  
                charactercounts[f] = 1
    return charactercounts

def sort_on(dict):
    return dict["number"]
#part of charactercount_sort

def charactercount_sort(character_count_dict):
    sorted_list = []
    for character in character_count_dict:
        sorted_list.append({'character': character, 'number': character_count_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




main()