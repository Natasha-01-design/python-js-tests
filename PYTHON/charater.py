# Given a string, find the first character 
# that does not repeat anywhere in the string. Return None if all characters repeat.



# Input: "Hello"

# Output: "H"
# Input: "Swiss"
# Output: "w"
def first_none_repeating(*words):
    counts={}
    for word in words:
       for letter in word:
          counts[letter.lower()]=counts.get(letter.lower(),0)+1
    for word in words:
     for letter in word:
        if counts[letter.lower()]==1:
            return("the first none repeat letter is:",letter)

    return("no non repeating number")
print(first_none_repeating("Hello"))
print(first_none_repeating("Swiss"))
