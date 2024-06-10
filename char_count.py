def get_character_count(path):
    with open(path) as f:
        lower_case = f.read().lower()
    
    char_count = {}
    
    for char in lower_case:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 char_count.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = get_character_count(file_path)
    print(result)