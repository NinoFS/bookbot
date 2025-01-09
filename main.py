
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
def main():
    return print(file_contents)

def wordcount():
    words = file_contents.split()
    wordnumber = 0
    for f in words:
        wordnumber += 1
    return print(wordnumber)


main()
wordcount()
