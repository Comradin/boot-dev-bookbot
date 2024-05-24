from string import ascii_lowercase


def count_words(content):
    words = content.split()
    # print(f"Words: {len(words)}")
    return len(words)


def count_letters(content):
    letters = dict.fromkeys(ascii_lowercase)

    for letter in content.lower():
        if letter not in ascii_lowercase:
            continue

        if letters[letter] == None:
            letters[letter] = 1
        else:
            letters[letter] += 1

    report_letters(letters)


def sort_on(dict):
    return dict["num"]


def report_letters(letters):
    result = []

    for key in letters.keys():
        result.append({"letter": key, "num": letters[key]})

    result.sort(reverse=True, key=sort_on)

    for element in result:
        print(f"The '{element["letter"]}' character was found {element["num"]} times")


def report_book(book_path, content):
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(content)} words found in the document")

    count_letters(content)
    print("--- End report ---")


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

        report_book("books/frankenstein.txt", file_contents)


main()
