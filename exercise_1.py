def main():
    original_string = input("Enter your string: ")
    final_string = ""
    for char in reversed(original_string):
        final_string += char
    print(final_string)   
    

main()