import math

def gradingStudents(grades):
    rounded_grades_arr = []
    for i in grades:
        temp_round_to_next5 = math.ceil(i/5.0) * 5
        difference = temp_round_to_next5 - i
        if temp_round_to_next5 == 40 and difference < 3:
            rounded_grades_arr = rounded_grades_arr + [temp_round_to_next5]
        elif i > 40:
            if difference < 3:
                rounded_grades_arr = rounded_grades_arr + [temp_round_to_next5]
            else:
                rounded_grades_arr = rounded_grades_arr + [i]
        else:
            rounded_grades_arr = rounded_grades_arr + [i]

    return rounded_grades_arr
    

if __name__ == '__main__':

    grades_count = int(input("\n\nEnter number of grades: ").strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input("\nEnter a garde: ").strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)