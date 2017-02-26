def main():
    file_name  = input("Full path to file: ")
    file  = open(file_name, 'r').read()
    search_string  = input("Enter the word: ")
    count = file.count(search_string)

    print("'" + search_string + "' was found " + str(count) + " times")

main()