def main():
    with open("/home/anthony/workspace/github.com/anbguye/bookbot/books/frankenstein.txt") as file:
        file_contents = file.read()
        print(file_contents)

        words = file_contents.split()
        
        count = {}

        print(f"Total words: {len(words)} found in the document")

        for word in words:
            for letter in word:
                count[letter.lower()] = count.get(letter.lower(), 0) + 1

        for letter, count in sorted(count.items()):
            print(f"Letter {letter} found {count} times")

if __name__ == "__main__":
    main()