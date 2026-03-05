from functions.get_file_content import get_file_content

def main():
    print("Result for 'lorem.txt' file:\n" + get_file_content("calculator", "lorem.txt") + "\n")
    print("Result for 'main.py' file:\n" + get_file_content("calculator", "main.py") + "\n")
    print("Result for 'pkg/calculator.py' file:\n" + get_file_content("calculator", "pkg/calculator.py") + "\n")
    print("Result for '/bin/cat' file:\n" + get_file_content("calculator", "/bin/cat") + "\n")
    print("Result for 'pkg/does_not_exist.py' file:\n" + get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()
