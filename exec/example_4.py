if __name__ == "__main__":
    with open("file1.txt", "r") as fileptr:
        content = fileptr.readlines()
        print(content)