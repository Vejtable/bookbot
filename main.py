import sys
from char_count import get_character_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main(book_path):
    text = get_book_text(book_path)
    character_counts = get_character_count(book_path)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{sum(character_counts.values())} characters found in the document\n")
    for char, count in sorted(character_counts.items(), key=lambda item: -item[1]):
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    main(book_path)