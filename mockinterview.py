# Ask the candidate to write a function that will determine if the given string is full of unique characters.
# We can assume that spaces don’t count, and the characters are not case sensitive (i.e. “A” is the same as “a”).
# The most efficient solution is going to use a Hashmap. The candidate should iterate through the string. and for each of the characters put them in the Hashset, if the value already exists, they can return false as soon as a duplicate occurs.
# We can assume they have a Hashset readily available (they do not have to implement one).
# This solution is of an O(n) time and O(n) space.


def has_unique_characters(string):
    char_set = set()
    #create a dictionary 
    for i in string:
        if i != " ":
            i = i.lower()  # Convert character to lowercase
            if i in char_set:
                # راح يجي ع اول اشي وما يلاقي اشي بعدها بروح بضيف الحرف الاول ثم بضل يضيف عبين ما يلاقي حرف متكرر بوقف وبرجع 
                # False
                return False
            char_set.add(i)
    return True


print(has_unique_characters('salah'))


# The char_set is a HashSet that stores the unique characters encountered.
# We iterate through each character in the string.
# If the character is a space, we skip it as spaces are not counted.
# We convert the character to lowercase using the lower() method to ensure case insensitivity.
# If the character is already present in the char_set, we return False since it is a duplicate.
# Otherwise, we add the character to the char_set.
# If the loop completes without finding any repeated characters, we return True.