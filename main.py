def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        num_char = count_char(file_contents)
        char_list = convert_to_list(num_char)

        print(char_list)
        print(num_char)

        print("--- Begin report of books/frankenstein.txt ---")
        print("")
        print(f"{num_words} words found in the document")
        print("")
        display_chars(char_list)
        
        print("--- End report ---")


############ MAIN DEF ONLY ABOVE ###################

def count_words(file_contents):
    list_of_words = file_contents.split()
    num_words = len(list_of_words)
    return num_words

def count_char(file_contents):
    text = file_contents.lower()
    char_dict = {}

    for char in text:
        if char.isalpha():    
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def convert_to_list(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    
def sort_on(dict):
    return dict["count"]

def display_chars(char_list):
    for key in char_list:
        print(f"The '{key["char"]}' character was found {key["count"]} times")
    
#################### MAIN FUNCTIONS BELOW ####################    
main()
