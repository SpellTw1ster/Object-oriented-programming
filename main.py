class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avarage_score = 0

    def add_course_to_attached(self, course):
        if course.name not in self.courses_attached:
            self.courses_attached.append(course.name)
            course.lecturers[self.name] = []
        else:
            return 'Error'

    def total_avarage_score(self):
        total = []
        count = 0
        for i in list(self.grades.values()):
            for k in i:
                total.append(k)
        for i in total:
            count += i
        self.avarage_score = round((count / len(total)), 2)


    def __verify_data(cls, other):
        if not isinstance(other, (float, Lecturer)):
            raise TypeError

        return other if isinstance(other, float) else other.avarage_score

    def __eq__(self, other):
        avarage_score = self.__verify_data(other)
        return self.avarage_score == avarage_score

    def __lt__(self, other):
        avarage_score = self.__verify_data(other)
        return self.avarage_score < avarage_score

    def __le__(self, other):
        avarage_score = self.__verify_data(other)
        return self.avarage_score <= avarage_score

    def __str__(self):
        return f'''Name: {self.name}
Surname: {self.surname}
Avarage score: {self.avarage_score}
'''


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if 0 <= grade <= 10:
            if isinstance(student, Student) and course.name in self.courses_attached and course.name in student.courses_in_progress:
                if course.name in student.grades:
                    student.grades[course.name] += [grade]
                    course.students[student.name] += [grade]
                else:
                    student.grades[course.name] = [grade]
                    course.students[student.name] = [grade]
            else:
                return 'Error'
        else:
            return 'From 0 to 10'
        student.total_avarage_score()
        course.students_avarage_score()

    def __str__(self):
        return f'''Name: {self.name}
Surname: {self.surname}
'''


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avarage_score = 0

    def add_courses_in_progress(self, course):
        if course.name not in self.courses_in_progress:
            self.courses_in_progress.append(course.name)
            course.students[self.name] = []
        else:
            return 'Error'

    def total_avarage_score(self):
        total = []
        count = 0
        for i in list(self.grades.values()):
            for k in i:
                total.append(k)
        for i in total:
            count += i
        self.avarage_score = round((count / len(total)), 2)

    def lecturer_rating(self, lecturer, course, grade):
        if 0 <= grade <= 10:
            if isinstance(lecturer,
                          Lecturer) and course.name in self.courses_in_progress and course.name in lecturer.courses_attached:
                if course.name in lecturer.grades:
                    lecturer.grades[course.name] += [grade]
                    course.lecturers[lecturer.name] += [grade]
                else:
                    lecturer.grades[course.name] = [grade]
                    course.lecturers[lecturer.name] = [grade]
            else:
                return 'Error'
        else:
            return 'From 0 to 10'
        lecturer.total_avarage_score()
        course.lecturers_avarage_score()


    def __verify_data(cls, other):
        if not isinstance(other, (float, Student)):
            raise TypeError

        return other if isinstance(other, float) else other.avarage_score

    def __eq__(self, other):
        avarage_score = self.__verify_data(other)
        return self.avarage_score == avarage_score

    def __lt__(self, other):
        avarage_score = self.__verify_data(other)
        return self.avarage_score < avarage_score

    def __le__(self, other):
        avarage_score = self.__verify_data(other)
        return self.avarage_score <= avarage_score

    def __str__(self):
        list_courses_in_progress = ''
        for i in self.courses_in_progress:
            list_courses_in_progress += f'{i}, '

        list_finished_courses = ''
        for i in self.finished_courses:
            list_finished_courses += f'{i}, '

        return f'''Name: {self.name}
Surname: {self.surname}
Homework avarage score: {self.avarage_score}
Courses in progress: {list_courses_in_progress}
Completed courses: {list_finished_courses}
'''


class Course:
    def __init__(self, name):
        self.name = name
        self.students = {}
        self.lecturers = {}
        self.st_avarage_score = 0
        self.lec_avarage_score = 0

    def students_avarage_score(self):
        total = []
        count = 0
        for i in list(self.students.values()):
            for k in i:
                total.append(k)
        for i in total:
            count += i
        self.st_avarage_score = round((count / len(total)), 2)

    def lecturers_avarage_score(self):
        total = []
        count = 0
        for i in list(self.lecturers.values()):
            for k in i:
                total.append(k)
        for i in total:
            count += i
        self.lec_avarage_score = round((count / len(total)), 2)

    def __str__(self):
        return f'''Course name: {self.name}
Average score of students: {self.st_avarage_score}
Average score of lecturers: {self.lec_avarage_score}
'''


python = Course('Python')
git = Course('Git')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.add_courses_in_progress(python)
best_student.finished_courses += ['Git']

fedor = Student('Fedor', 'Dostoyevskii', 'male')
fedor.add_courses_in_progress(python)
fedor.finished_courses += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, python, 9)
cool_mentor.rate_hw(best_student, python, 10)
cool_mentor.rate_hw(best_student, python, 10)

cool_mentor.rate_hw(fedor, python, 10)
cool_mentor.rate_hw(fedor, python, 8)
cool_mentor.rate_hw(fedor, python, 10)

frodo = Lecturer('Frodo', 'Baggins')
frodo.add_course_to_attached(python)
gendalf = Lecturer('Gendalf', 'Grey')
gendalf.add_course_to_attached(python)

best_student.lecturer_rating(frodo, python, 10)
best_student.lecturer_rating(frodo, python, 8)
best_student.lecturer_rating(gendalf, python, 8)
best_student.lecturer_rating(gendalf, python, 6)

fedor.lecturer_rating(frodo, python, 9)
fedor.lecturer_rating(frodo, python, 9)
fedor.lecturer_rating(gendalf, python, 6)
fedor.lecturer_rating(gendalf, python, 7)

print(best_student.grades)
print(best_student)
print(frodo)
print(cool_mentor)
print(best_student == fedor)
print(best_student < fedor)
print(frodo != gendalf)
print(frodo > gendalf)
print(python)