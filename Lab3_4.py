def count_vowels(sentence):
    vowels = 'aeiou'
    count = 0
    for char in sentence:
        if char.lower() in vowels:
            count += 1
    return count
sentence = input("Введите предложение на английском: ")
print("Длина предложения:", len(sentence))
lower_case_sentence = sentence.lower()
print("Предложение в нижнем регистре:", lower_case_sentence)
vowel_count = count_vowels(sentence)
print("Количество гласных в предложении:", vowel_count)
replaced_sentence = lower_case_sentence.replace("ugly", "beauty")
print("Предложение с заменой слова 'ugly' на 'beauty':", replaced_sentence)
if lower_case_sentence.startswith("the") and lower_case_sentence.endswith("end"):
    print("Предложение начинается с 'The' и заканчивается на 'end'.")
else:
    print("Предложение не соответствует условиям.")