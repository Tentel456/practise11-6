import csv


class Student:
    def __init__(self, surname, name, marks):
        self.surname = surname
        self.name = name
        self.marks = marks

def read_data(filename):
    students = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            surname = row[0]
            name = row[1]
            marks = list(map(int, row[2:]))  
            students.append(Student(surname, name, marks))
    return students

def calculate_statistics(students):
    total_marks = [0, 0, 0, 0]  
    max_sum = 0
    max_students = []
    count_twos = 0

    for student in students:
        sum_marks = sum(student.marks)
        
        for i in range(4):
            total_marks[i] += student.marks[i]

        
        if sum_marks > max_sum:
            max_sum = sum_marks
            max_students = [(student.surname, student.name)]
        elif sum_marks == max_sum:
            max_students.append((student.surname, student.name))

        
        if 2 in student.marks:
            count_twos += 1

    
    average_marks = [total / len(students) for total in total_marks]

    return average_marks, max_sum, max_students, count_twos

def main():
    filename = 'marks.csv'
    students = read_data(filename)
    average_marks, max_sum, max_students, count_twos = calculate_statistics(students)

    
    subjects = ['Алгебра', 'Русский язык', 'Физика', 'История']
    print("Средний балл по предметам:")
    for subject, avg in zip(subjects, average_marks):
        print(f"{subject}: {avg:.2f}")

    print(f"\nМаксимальная сумма баллов: {max_sum}")

    max_students.sort()  
    print("Учащиеся с максимальной суммой баллов:")
    for surname, name in max_students:
        print(f"{surname} {name}")

    print(f"\nКоличество учащихся, получивших хотя бы одну отметку «2»: {count_twos}")

if __name__ == "__main__":
    main()
