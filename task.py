class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        grades_all = []
        for i in self.grades:
            grades_all.extend(self.grades.get(i))
        return sum(grades_all) / len(grades_all) if len(grades_all) != 0 else 'нет оценок'

    def __str__(self):
        courses_in_progress = ','.join(self.courses_in_progress)
        finished_courses = ','.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.average_rating()} \n' \
               f'Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'

    def __gt__(self, other):
        if isinstance(other, Student):
            if self.average_rating() > other.average_rating():
                return f'{self.name} лучше {other.name}'
            else:
                return f'{other.name} лучше {self.name}'
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        grades_all = []
        for i in self.grades:
            grades_all.extend(self.grades.get(i))
        return sum(grades_all) / len(grades_all) if len(grades_all) != 0 else 'нет оценок'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            if self.average_rating() > other.average_rating():
                return f'{self.name} лучше {other.name}'
            else:
                return f'{other.name} лучше {self.name}'
        else:
            return 'Ошибка'



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_rating_student(course, students=[]):
    grades_all = []
    for student in students:
        grades_all.extend(student.grades[course])
    return print(sum(grades_all) / len(grades_all))


def average_rating_lecturer(course, lecturers=[]):
    grades_all = []
    for lecturer in lecturers:
        grades_all.extend(lecturer.grades[course])
    return print(sum(grades_all) / len(grades_all))


# Студенты
first_student = Student('Ruoy', 'Eman', 'your_gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Physics']

second_student = Student('Bin', 'Cross', 'your_gender')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Physics']

# Лекторы
first_lecturer = Lecturer('Dew', 'Fort')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Physics']

second_lecturer = Lecturer('Some', 'Buddy')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Physics']

# Ревьюэры
first_reviewer = Reviewer('Mat', 'Grin')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Physics']

second_reviewer = Reviewer('Sara', 'Old')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Physics']

# Студенты выставляют оценки лекторам
first_student.rate_hw(first_lecturer, 'Python', 5)
first_student.rate_hw(first_lecturer, 'Physics', 7)
first_student.rate_hw(second_lecturer, 'Python', 8)
first_student.rate_hw(second_lecturer, 'Physics', 3)

second_student.rate_hw(first_lecturer, 'Python', 8)
second_student.rate_hw(first_lecturer, 'Physics', 6)
second_student.rate_hw(second_lecturer, 'Python', 7)
second_student.rate_hw(second_lecturer, 'Physics', 4)

# Ревьюэры выставляют оценки студентам
first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Physics', 7)
first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Physics', 6)

second_reviewer.rate_hw(first_student, 'Python', 8)
second_reviewer.rate_hw(first_student, 'Physics', 9)
second_reviewer.rate_hw(second_student, 'Python', 5)
second_reviewer.rate_hw(second_student, 'Physics', 6)

# Оценки
print(first_student.grades)
print(second_student.grades)
print(first_lecturer.grades)
print(second_lecturer.grades)

# Вызов метода __str__
print(first_student)
print(second_student)
print(first_lecturer)
print(second_lecturer)
print(first_reviewer)
print(second_reviewer)

# Сравнение
print(first_lecturer > second_lecturer)
print(first_student > second_student)

average_rating_student('Physics', [first_student, second_student])
average_rating_lecturer('Physics', [first_lecturer, second_lecturer])
