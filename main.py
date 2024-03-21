# Read the book
def read_book():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    return file_content

# count the words from the book
def word_count(text):
    # first get rid of whitespaces with split()
    text = text.split()
    count = 0
    for i in text:
        count+=1
    return count

# count letters
def count_letters(text):
    # string is already iterable by character
    dict = {}
    # we just need to convert each char to lowercase to reduce variability
    text = text.lower()
    for i in text:
        # skips whitespaces and non-alphabetic-letters
        if i!= " " and i.isalpha() :
            if i in dict:
                dict[i]+=1
            elif i not in dict:
                dict[i] = 1
    return dict

# Now we need to consolidate all the data into a clean report
def print_report(dict):
    # we need to use the sort method on our dictionary but its for lists
    list_dict = []

    # we need a function for the key argument in .sort()
    def sort_on(dict):
        return dict['num']
    
    for i, value in dict.items():
        # we create two accessible keys with each element as a dict
        list_dict.append({"char": i, "num": value})
    list_dict.sort(reverse=True, key=sort_on)
  
    for i in list_dict:
        print(f"The {i['char']} character was found {i['num']} times")

        
        


def main():
    text = read_book()
    print("Word Count of Text: " + str(word_count(text)))
    print()
    print_report(count_letters(text))

main()

