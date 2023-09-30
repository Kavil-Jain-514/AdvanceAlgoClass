def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    for i in range(n - m + 1):
        if text[i: i + m] == pattern:
            positions.append(i)

    return positions


def main():
    text = str(input("Enter the text: "))
    pattern = str(input("Enter the pattern: "))
    matches = naive_string_match(text, pattern)
    if len(matches) > 0:
        print(f"Pattern found at positions: {', '.join(map(str, matches))}")
    else:
        print("Pattern not found in the text.")


# Example usage:
if __name__ == '__main__':
    main()



