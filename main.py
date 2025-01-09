
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
def main():
    return print(file_contents)

def wordcount():
    words = file_contents.split()
    wordnumber = 0
    for f in words:
        wordnumber += 1
    return print("Word Count",wordnumber)

def charactercount():
    lowercased = file_contents.lower()
    charactercounts = {}
    abc = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    for f in lowercased:
        if f in abc.split():
            if f in charactercounts:
                charactercounts[f] += 1
            else:  
                charactercounts[f] = 1

    return print(charactercounts)


#main()
wordcount()
charactercount()
