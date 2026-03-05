from functions.run_python_file import run_python_file

def main():
    print("Result for running 'main.py':\n" + run_python_file("calculator", "main.py") + "\n")
    print("Result for running 'main.py' with '3 + 5' as an argument:\n" + run_python_file("calculator", "main.py", ["3 + 5"]) + "\n")
    print("Result for running 'tests.py':\n" + run_python_file("calculator", "tests.py") + "\n")
    print("Result for running '../main.py':\n" + run_python_file("calculator", "../main.py") + "\n")
    print("Result for running 'nonexistent.py':\n" + run_python_file("calculator", "nonexistent.py") + "\n")
    print("Result for running 'lorem.txt':\n" + run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()
