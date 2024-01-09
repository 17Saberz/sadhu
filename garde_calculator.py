def converting_grade(grades):
    total_grade = 0

    for member in grades:

        if member == 'A':
            total_grade += 4
        elif member == 'B+':
            total_grade += 3.5
        elif member == 'B':
            total_grade += 3
        elif member == 'C+':
            total_grade += 2.5
        elif member == 'C':
            total_grade += 2
        elif member == 'D+':
            total_grade += 1.5
        elif member == 'D':
            total_grade += 1
        elif member == 'E':
            total_grade += 0
    return total_grade, len(grades)

def get_average_grade(grades, lenght):
    final_grade = grades / lenght

    if final_grade >= 3.75:
        return 'A'
    elif 3.75 > final_grade >= 3.25:
        return 'B+'
    elif 3.25 > final_grade >= 2.75:
        return 'B'
    elif 2.75 > final_grade >= 2.25:
        return 'C+'
    elif 2.25 > final_grade >= 1.75:
        return 'C'
    elif 1.75 > final_grade >= 1.25:
        return 'D+'
    elif 1.25 > final_grade >= 0.75:
        return 'D'
    elif 0.75 > final_grade:
        return 'E'
    
grades = input("Input: ").split(', ')
total, lenght = converting_grade(grades)
print("Output: {}".format(get_average_grade(total, lenght)))

print('-'*47)