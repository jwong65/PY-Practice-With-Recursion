# Write code for algorithm 5 below
# Palindrome
def palindrome(n):
    # Reversing a string in python
    reverse = n[::-1]
    if (reverse.lower() == n.lower()):
        return True
    else:
        return False
    
# print(palindrome("radar")) = True
# print(palindrome("Random")) = False
# print(palindrome("Radar")) = Now true with the .lower statements