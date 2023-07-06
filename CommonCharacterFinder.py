# This code compares two names and prints out the common characters between them.
# It also counts the number of common characters and prints it out.


def compare_names(name1, name2):
    common_characters = []
    count = 0
    
    for char1 in name1:
        if char1 in name2 and char1 not in common_characters:
            common_characters.append(char1)
            count += 1
    
    if count > 0:
        print(f"The common character(s) between {name1} and {name2} are:")
        print(common_characters)
        print(f"Number of common characters: {count}")
    else:
        print("No common characters found.")

# Example usage
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

name1 = name1.lower()
name2 = name2.lower()

compare_names(name1, name2)
