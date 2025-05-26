def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
    return book_text

def count_words(book_text):
    words = book_text.split()
    return len(words)

def main():
    path_to_file = "/home/josholdfield/bookbot/books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    word_count = count_words(book_text)
    print(book_text)
    print(f"{word_count} words found in the document")


main()


