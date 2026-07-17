# ask user for input and split the input into a list
words = input("Enter Sentence: ").split()

#My approach: loops through each word in the list and prints out the reverse order of the word using the negative index method.
#Immediately i use the end keyword for print to avoid printing on a new line for each word so the sentence is reserved
#with this, the end always prints and extra space at the end of the sentence
"""for word in words:
    print(word[::-1], end=" ")
print()"""

for word in words:
    result = "".join(reversed(word))
    print(result, end=" ")
print()

#final_result = "".join(" ".join(reversed(word)) for word in words)

#print(final_result)
