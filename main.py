# TODO:
# - Use a main function to wrap the logic and call main() at the bottom of your file 
#   to execute your program.
# - Change main.py so that instead of printing "hello world", it reads the contents 
#   of the "frankenstein.txt" and prints it all to the console.

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

if __name__ == "__main__":
    main()

