quantity = int(input())
correct_quantity = 0
unique_students = set()

students_answers = [input() for _ in range(quantity)]

for student_answer in students_answers:
    student = student_answer.split(": ")[0]
    answer = student_answer.split(": ")[1]
    if answer == "Correct":
        correct_quantity += 1
        if student not in unique_students:
            unique_students.add(student)
if correct_quantity == 0:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    print(f"Верно решили {len(unique_students)} учащихся")
    print(f"Из всех попыток {int(correct_quantity / quantity * 100 + 0.5)}% верных")
