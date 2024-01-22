def main():
    original_string = input("Enter your string: ")
    lowerCase = []
    upperCase = []
    for char in original_string:
        if (char.islower()):
            lowerCase.append(char)
        if(char.isupper()):
            upperCase.append(char)
            
    print("".join(lowerCase) +"".join(upperCase))
            
            
    

main()