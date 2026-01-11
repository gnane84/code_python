

student_score = [150, 160, 172, 185, 190, 195, 200, 199, 201, 204, 210, 250, 280, 300, 250]

max_score = 0

for score in student_score:
    if score > max_score:
        print(score)
        max_score = score
print(f"The max score in the list is: {max_score}")

