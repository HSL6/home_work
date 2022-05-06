def mean_allgrades_stud(students: list, course):
    tmp = []
    for st in students:
        tmp += st.grades[course]
    return round(sum(tmp)/len(tmp), 3)


def mean_allgrades_lectors(lectors: list, course):
    tmp = []
    for lec in lectors:
        tmp += lec.grades[course]
    return round(sum(tmp) / len(tmp), 3)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mean_grades = -1

    def set_mean_grades(self):
        all_grades = []
        for i in self.grades.values():
            all_grades += i

        self.mean_grades = round(sum(all_grades) / len(all_grades), 3)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        lecturer.set_mean_grades()

    def __str__(self):
        print(f'Имя: {self.name}', f'Фамилия: {self.surname}', sep='\n')
        if self.mean_grades != -1:
            print('Средняя оценка за домашнее задание:', self.mean_grades)
        print('Курсы в процессе изучения:', *self.courses_in_progress)
        if self.finished_courses:
            print('Завершенные курсы:', *self.finished_courses)
        return ''

    def __lt__(self, other):
        if self.mean_grades < other.mean_grades:
            return True
        return False

    def __eq__(self, other):
        if self.mean_grades == other.mean_grades:
            return True
        return False

    def __gt__(self, other):
        if self.mean_grades > other.mean_grades:
            return True
        return False


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.mean_grades = -1

    def set_mean_grades(self):
        all_grades = []
        for i in self.grades.values():
            all_grades += i
        self.mean_grades = round(sum(all_grades) / len(all_grades), 3)

    def __str__(self):
        print(f'Имя: {self.name}', f'Фамилия: {self.surname}', sep='\n')
        print('Средняя оценка за лекции:', self.mean_grades)
        return ''

    def __lt__(self, other):
        if self.mean_grades < other.mean_grades:
            return True
        return False

    def __eq__(self, other):
        if self.mean_grades == other.mean_grades:
            return True
        return False

    def __gt__(self, other):
        if self.mean_grades > other.mean_grades:
            return True
        return False


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        student.set_mean_grades()

    def __str__(self):
        info = f'Имя: {self.name}' + '\n' + f'Фамилия: {self.surname}'
        return info


best_lector = Lecturer('Timofey', 'Hiryanov')
best_lector.courses_attached += ['Python']

normal_lector = Lecturer('Vasya', 'Pupkin')
normal_lector.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['C++']

normal_student = Student('Ivan', 'Sidorov', 'm')
normal_student.courses_in_progress += ['Python']
normal_student.finished_courses += ['C++']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

angry_mentor = Reviewer('Petr', 'Ivanov')
angry_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)

cool_mentor.rate_hw(normal_student, 'Python', 5)
cool_mentor.rate_hw(normal_student, 'Python', 4)
cool_mentor.rate_hw(normal_student, 'Python', 2)

normal_student.rate_hw(best_lector, 'Python', 8)
best_student.rate_hw(best_lector, 'Python', 10)
normal_student.rate_hw(normal_lector, 'Python', 6)
best_student.rate_hw(normal_lector, 'Python', 8)

print(best_student)
print(normal_student)
print(best_lector)

print('normal_student учится хуже чем best_student?-', normal_student < best_student)

print('Средняя оценка лекторов по курсу Python:', mean_allgrades_lectors([best_lector, normal_lector], 'Python'))

print('Средняя оценка студентов по курсу Python:', mean_allgrades_lectors([best_student, normal_student], 'Python'))