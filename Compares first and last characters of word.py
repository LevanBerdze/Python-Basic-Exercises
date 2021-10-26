#Compares first and last characters of word
#Returns True if it is the same
#returs False if it isn't the same

x = input("Enter the word: ")

def first_and_last(message):
    if len(message) == 0:
        return True
    elif message[0] == message[-1]:
        return True   
    else:     
        return False

print(first_and_last(x))
