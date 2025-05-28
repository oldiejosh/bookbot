from stats import count_words, count_characters, generate_character_report


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
    return book_text


def main():
    path_to_file = "/home/josholdfield/bookbot/books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    word_count = count_words(book_text)
    character_counts = count_characters(book_text)
    character_report = generate_character_report(character_counts)

    print(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in character_report:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()


