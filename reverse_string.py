import sys

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string
    
if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("You must provide a string to reverse")
    else:
        reversed_string = reverse_string(sys.argv[1])
        print(reversed_string)
