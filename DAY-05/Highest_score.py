import random
student_scores = []
for _ in range(50):
    student_scores.append(random.randint(0, 100))

print(student_scores)

total_exam_score = sum(student_scores)
print(f"total_exam_Score IS:{total_exam_score}")

sum = 0
for score in student_scores:
    sum += score
print(sum)

max = 0
for score in student_scores:
    print(score)
    if (score > max):
        max = score

print(f"max_number {max}")

