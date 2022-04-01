class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_score = 0

    def total_average_score(self):
        total = []
        count = 0
        for i in list(self.grades.values()):
            for k in i:
                total.append(k)
        for i in total:
            count += i
        self.average_score = round((count / len(total)), 2)

    def __verify_data(cls, other):
        if not isinstance(other, (float, Lecturer)):
            raise TypeError('float or Lecturer')
        return other if isinstance(other, float) else other.average_score

    def __le__(self, other):
        average_score = self.__verify_data(other)
        return self.average_score <= average_score

    def __lt__(self, other):
        average_score = self.__verify_data(other)
        return self.average_score < average_score

    def __eq__(self, other):
        average_score = self.__verify_data(other)
        return self.average_score == average_score

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_score}
'''



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if 0 <= grade <= 10:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Error'
        else:
            return 'From 0 to 10'

        student.total_average_score()

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
'''

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_score = 0

    def total_average_score(self):
        total = []
        count = 0
        for i in list(self.grades.values()):
            for k in i:
                total.append(k)
        for i in total:
            count += i
        self.average_score = round((count / len(total)), 2)


    def lecturer_rating(self, lecturer, course, grade):
        if 0 <= grade <= 10:
            if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Error'
        else:
            return 'From 0 to 10'

        lecturer.total_average_score()

    def __verify_data(cls, other):
        if not isinstance(other, (float, Student)):
            raise TypeError('float or Student')
        return other if isinstance(other, float) else other.average_score

    def __le__(self, other):
        average_score = self.__verify_data(other)
        return self.average_score <= average_score

    def __lt__(self, other):
        average_score = self.__verify_data(other)
        return self.average_score < average_score

    def __eq__(self, other):
        average_score = self.__verify_data(other)
        return self.average_score == average_score

    def __str__(self):
        courses_in_progress_list = ''
        for i in self.courses_in_progress:
            courses_in_progress_list += f'{i}, '

        finished_courses_list = ''
        for i in self.finished_courses:
            finished_courses_list += f'{i}, '

        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашнее задание: {self.average_score}
Курсы в процессе изучения: {courses_in_progress_list}
Завершенные курсы: {finished_courses_list}
'''








best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python-developer']
best_student.finished_courses += ['GIT']

fedor = Student('Fedor', 'Dostoyevskii', 'male')
fedor.courses_in_progress += ['Python-developer']
fedor.finished_courses += ['GIT']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python-developer']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 7)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)

kirill = Lecturer('Kirill', 'Nemolyaev')
kirill.courses_attached += ['Python-developer']
marina = Lecturer('Marina', 'Tsvetaeva')
marina.courses_attached += ['Python-developer']

best_student.lecturer_rating(kirill, 'Python', 10)
best_student.lecturer_rating(kirill, 'Python', 9)
best_student.lecturer_rating(marina, 'Python', 9)
best_student.lecturer_rating(marina, 'Python', 7)

fedor.lecturer_rating(kirill, 'Python', 9)
fedor.lecturer_rating(kirill, 'Python', 9)
fedor.lecturer_rating(marina, 'Python', 6)
fedor.lecturer_rating(marina, 'Python', 7)


print(best_student.grades)
print(best_student)
print(kirill)
print(cool_mentor)
print(best_student)
print(best_student == fedor)
print(best_student < fedor)
print(kirill != marina)
print(kirill > marina)