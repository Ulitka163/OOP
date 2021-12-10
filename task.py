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
        sum_grades = 0
        for i in grades_all:
            sum_grades += i
        return sum_grades / len(grades_all) if len(grades_all) != 0 else 'нет оценок'

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
        sum_grades = 0
        for i in grades_all:
            sum_grades += i
        return sum_grades / len(grades_all) if len(grades_all) != 0 else 'нет оценок'

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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

best_student.rate_hw(cool_mentor, 'Python', 10)
best_student.rate_hw(cool_mentor, 'Python', 10)
best_student.rate_hw(cool_mentor, 'Python', 10)

first_mentor = Lecturer('dew', 'fort')
first_mentor.courses_attached += ['Python']

best_student.rate_hw(first_mentor, 'Python', 12)
best_student.rate_hw(first_mentor, 'Python', 12)
best_student.rate_hw(first_mentor, 'Python', 9)

# print(first_mentor.grades)
# print(best_student)
# print(cool_mentor)
# print(first_mentor)
# print(cool_mentor > first_mentor)