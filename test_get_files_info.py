from functions.get_files_info import get_files_info

def main():
    print("Result for current directory:\n" + get_files_info("calculator", ".") + "\n")
    print("Result for 'pkg' directory:\n" + get_files_info("calculator", "pkg") + "\n")
    print("Result for '/bin' directory:\n" + get_files_info("calculator", "/bin") + "\n")
    print("Result for '../' directory:\n" + get_files_info("calculator", "../"))


if __name__ == "__main__":
    main()
