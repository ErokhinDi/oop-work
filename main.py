class Student:
    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()


    def __str__(self):

        print(some_student)



        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return

    def rate_hw(self, lecturer, course, grade):


        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):

        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.courses_attached = []


        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):

        self.average_rating = float()
        self.grades = {}

        self.name = name
        self.surname = surname
        self.courses_attached = []


        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):

        print(some_reviewer)

        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):

        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):


        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):

        print(some_lecturer)



        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
# 4 задача
def student_rating(student_list, course_name):

sum_all = 0
count_all = 0
for stud in student_list:
   if stud.courses_in_progress == [course_name]:
        sum_all += stud.average_rating
        count_all += 1
average_for_all = sum_all / count_all
return average_for_all
def lecturer_rating(lecturer_list, course_name):

sum_all = 0
count_all = 0
for lect in lecturer_list:
    if lect.courses_attached == [course_name]:
        sum_all += lect.average_rating
        count_all += 1
average_for_all = sum_all / count_all
return average_for_all
# Создаем лекторов и закрепляем их за курсом
best_lecturer_1 = Lecturer('Ivan', 'Ivanov')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Petr', 'Petrov')
best_lecturer_2.courses_attached += ['Java']

best_lecturer_3 = Lecturer('Sidr', 'Sidorov')
best_lecturer_3.courses_attached += ['Python']


cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Jon', 'Carter')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']


student_1 = Student('Dmitry', 'Erokhin')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Semen', 'Malikov')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Elena', 'Petrova')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']


student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 4)
student_1.rate_hw(best_lecturer_2, 'Python', 6)
student_1.rate_hw(best_lecturer_2, 'Python', 8)

student_1.rate_hw(best_lecturer_1, 'Python', 6)
student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 5)

student_2.rate_hw(best_lecturer_2, 'Java', 10)
student_2.rate_hw(best_lecturer_2, 'Java', 7)
student_2.rate_hw(best_lecturer_2, 'Java', 10)

student_3.rate_hw(best_lecturer_3, 'Python', 4)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)
