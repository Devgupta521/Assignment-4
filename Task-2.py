user_input = input("Enter text to write to the file: ")
with open("output.txt", 'wt')as file:
    file.write(user_input)
    print("Data successfully written to output.txt\n")

additional_input = input("Enter additional text to append: ")
with open("output.txt", 'at') as file:
    file.write(additional_input)
    print("Data successfully appended\n")

print("Final content of output.txt:\n")

with open("output.txt", 'rt') as file:
    content = file.read()
    print(content)