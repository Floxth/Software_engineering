def average_grade(grades):
    total_grade = 0
    num_subjects = len(grades)

    for subject, grade in grades:
        total_grade += grade

    return total_grade / num_subjects

grades1 = [("математика", 85), ("английский", 90), ("история", 75)]
grades2 = [("химия", 95), ("искусство", 88), ("музыка", 92)]
grades3 = [("биология", 80), ("география", 85), ("физика", 88)]

print("Средняя оценка за все предметы (Первый):", average_grade(grades1))
print("Средняя оценка за все предметы (Второй):", average_grade(grades2))
print("Средняя оценка за все предметы (Третий):", average_grade(grades3))