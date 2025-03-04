from file_handling import read_file

def main():
    while True:
        file = input('What is the directory of the file you want the word count of?').strip()
        try:
            open(file, 'r')
        except:
            print("Please enter a valid file directory. Make sure you use /, and not \\.")
            continue
        length = read_file(file)
        print(f"The word count of this file is {length}.\nThe word count and timestamp have been added to the bottom of the file.")
        
main()