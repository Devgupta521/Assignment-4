try:
    with open("sample.txt", 'rt') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
except Exception as e:
    print(f"An error has occurred: {e}")