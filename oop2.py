class Student:


    def __init__(self, name, last_name, sex):
        self.name = name
        self.last_name = last_name
        self.sex = sex
        self.end_courses = []  # законченный курс
        self.courses_now = []  # не законченный курс
        self.grades = {}
        self._grades_list = []

    def _avg_rate(self):


        grades_list = []
        for grades in self.grades.values():
            for grade in grades:
                grades_list.append(grade)
                if len(grades_list) == 0:
                    self.avg_rate = 0
                else:
                    self.avg_rate = sum(grades_list) / len(grades_list)
                return self.avg_rate

    def __str__(self):

        return f'Имя: {self.name}' \
               f'\nФамилия: {self.last_name}' \
               f'\nСредняя оценка за Д/З: {self._avg_rate()}' \
               f'\nКурсы в процессе обучения: {", ".join(self.courses_now)}' \
               f'\nЗавершённые курсы: {", ".join(self.end_courses)}'

    def __gt__(self, other):


        if isinstance(other, Student):
            return self.avg_rate < other.avg_rate
        else:
            return "error"

    def lector_rate(self, lector, course, grade):
        if (isinstance(lector, Lector)
                and course in self.courses_now
                and course in lector.courses):
            if course in lector.rate_lector:
                lector.rate_lector[course] += [grade]
            else:
                lector.rate_lector[course] = [grade]
        else:
            return "error"


class Mentor:


    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.courses_attached = []  # закреплённый курс


class Lector(Mentor):


    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.courses = []
        self.rate_lector = {}

    def _avg_rate(self):

        rates_list = []
        for rates in self.rate_lector.values():
            for rate in rates:
                rates_list.append(rate)
        if len(rates_list) == 0:
            self.avg_lector = 0
        else:
            self.avg_lector = sum(rates_list) / len(rates_list)
        return self.avg_lector

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.last_name}" \
               f"\nСредняя оценка за лекции: {self._avg_rate()}"

    def __gt__(self, other):

        if isinstance(other, Lector):
            return self.avg_lector < other.avg_lector
        else:
            return "error"


class Reviewer(Mentor):


    def __init__(self, name, last_name):
        super().__init__(name, last_name)

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.last_name}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_now:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "error"


# Студенты
student1 = Student("Alex", "Efimchik", "man")
student1.courses_now = ['Stepik', 'Python', 'English']
student1.end_courses = ['SQL']

student2 = Student("Mikha", "Egorof", "man")
student2.courses_now = ['Python', 'English', 'Stepik']
student2.end_courses = ['SQL']

# Лекторы
lector1 = Lector("Vitaly", "Veselof")
lector1.courses = ['SQL', 'Python', 'English', 'Stepik']

lector2 = Lector("Oleg", "Batka")
lector2.courses = ['English', 'Python', 'SQL', 'Stepik']

# Проверяющие Д/З
reviewer1 = Reviewer("Naruto", "Yzumaki")
reviewer1.courses_attached = ['Stepik', 'Python']
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 3)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student1, 'Stepik', 7)
reviewer1.rate_hw(student1, 'Stepik', 4)
reviewer1.rate_hw(student1, 'Stepik', 6)

reviewer2 = Reviewer("Mikhail", "Gorshenef")
reviewer2.courses_attached = ['Python', 'SQL']

student1.lector_rate(lector1, 'Python', 7)
student1.lector_rate(lector2, 'English', 5)
student2.lector_rate(lector1, 'SQL', 3)
student2.lector_rate(lector2, 'English', 10)

print(student1, "\n")
print(student2, "\n")
print(lector1, "\n")
print(lector2, "\n")
print(reviewer1, "\n")
print(reviewer2, "\n")

print(student1 > student2)
print(lector1 > lector2)

students_list = [student1, student2]
lectores_list = [lector1, lector2]
all_courses = ['Stepik', 'Python', 'English', 'SQL']


def avg_students_rates(students, course):
    '''вычисляем средний бал студентов по курсам'''
    all_courses_rates = []
    for student in students:
        if course in student.grades.keys():
            for rate in student.grades.get(course):
                all_courses_rates += [rate]
        else:
            continue
    if len(all_courses_rates) == 0:
        avg_all_rate = "Студент не записан на этот курс"
    else:
        avg_all_rate = sum(all_courses_rates) / len(all_courses_rates)
    print(f'Средняя оценка студентов за курс {course}: {avg_all_rate}')



def avg_lectors_rates(lectores, course):
    '''вычисляем средний бал лекторов по курсам'''
    all_courses_rates = []
    for lector in lectores:
        if course in lector.grades.keys():
            for rate in lector.grades.get(course):
                all_courses_rates += [rate]

            else:
                continue
    if len(all_courses_rates) == 0:
        avg_all_rate_lec = "Лектор не записан на этот курс"
    else:
        avg_all_rate_lec = sum(all_courses_rates) / len(all_courses_rates)
    print(f'Средняя оценка за курс лекторов {course}: {avg_all_rate_lec}')


avg_students_rates(students_list, all_courses[1])
avg_lectors_rates(students_list, all_courses[2])