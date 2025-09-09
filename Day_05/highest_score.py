student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# easy way I found through documentation
max_score = max(student_scores)
print(max_score)

# the code I came up with
for score in student_scores:
    if score == max(student_scores):
        print(score)

# instructor example
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
