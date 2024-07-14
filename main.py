def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_chars(text):
    foo = list(text.lower())

    bar = {}

    for i in foo:
        if i not in bar:
            bar[i] = 1
        else:
            bar[i] = bar[i] + 1

    return bar


def sort_on(dict):
    return dict["count"]


def print_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    chars_count = count_chars(text)

    foo = []
    for i in chars_count:
        foo.append({"char": i, "count": chars_count[i]})

    foo.sort(reverse=True, key=sort_on)
    for i in foo:
        if i["char"].isalpha():
            print(f"The '{i["char"]}' character was found {i["count"]} times")
    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text)


main()
