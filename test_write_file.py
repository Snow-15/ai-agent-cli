from functions.write_file import write_file

def main():
    print("Result of writing to 'lorem.txt':\n" + write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum") + "\n")
    print("Result of writing to 'pkg/morelorem.txt':\n" + write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet") + "\n")
    print("Result of writing to '/tmp/temp.txt':\n" + write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    main()
