def find_longest_word(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    words = ''.join(char if char.isalnum() else ' ' for char in text).split()

    longest_word = max(words, key=len)

    return longest_word

file_path = 'input3.txt'

result = find_longest_word(file_path)
print("Самое длинное слово в файле:", result)
