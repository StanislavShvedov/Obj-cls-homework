from typing import Any

class Person:
    """
    Person - базовый класс
    name, suername - члены клсса (имя, фамилия)
    """
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

class Student(Person):
    """
    Student - наследуемый класс от класса Person
    name, suername - атрибут клсса, наследуемые от Person (имя, фамилия)
    finished_courses - атрибут класса (список, законченные курсы)
    courses_in_progress - атрибут класса (список, текущие курсы)
    grades - атрибут класса (словарь, ключ(название курса): значение (оценка)
    """
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_raiting(self, lector, course: str, grade: int) -> Any:
        """
        Метод класса выставляет оценку лектору по нащванию круса
        :param lector: экземпдяр класса Lecturer
        :param course: строка, название кукрса
        :param grade: число, оценка
        :return: записывает полученные параметры в словарь
        """
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if 0 < grade <= 10:
                if course in lector.rating:
                    lector.rating[course] += [grade]
                else:
                    lector.rating[course] = [grade]
            else:
                print('Ошибка ввода: Оценка должа быть по шкале от 0 до 10')
        else:
            print(f'Выне можете лектора. Он не читал на курсе {course}')

    def info(self):
        """
        Метод выводит информацию о экземпляре класса Student
        :return:
        """
        print(f'Студент. Имя: {self.name}, Фамилия: {self.surname}, Курс: {self.courses_in_progress}'
              f'Оценнки: {self.grades} Окончены курсы: {self.finished_courses}')

    def __average_rating(self) -> int:
        """
        Метод высчитывает средний бал экземпляра класса Student
        :return: число (средний балл)
        """
        result = 0
        for grades in self.grades.values():
            result = sum(grades) / 2
        return result

    def __str__(self) -> str:
        """
        Метод выводит информацию о экземпляре класса Student
        :return: строка
        """
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.__average_rating()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}')

    def __lt__(self, student):
        """
        Метод сравнения среднего балла экземпляра класса Student
        :param student: экземпляр класса Student
        :return: булевое значение
        """
        return self.__average_rating() == student.__average_rating()

class Mentor(Person):
    """
    Mentor - наследуемый класс от класса Person
    name, suername - атрибут клсса, наследуемые от Person (имя, фамилия)
    courses_attached - атрибут класса (список, прикрепленные курсы)
    """
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course: str, grade: int) -> Any:
        """
        Метод для выставления оценки экземпляру класса Student
        :param student: экземпляр класса Student
        :param course: срока, название круса
        :param grade: число, оценка
        :return: записывает полученные параметры в словарь
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def info(self) -> None:
        """
        Метод выводит информацию о экземпляре класса Student
        :return: строка
        """
        print(f'Преподаватель. Имя: {self.name}, Фамилия: {self.surname}, Учебный поток: {self.courses_attached}')

class Lecturer(Mentor):
    """
    Lecturer - множественное наследование от классов Mentor, Person
    name, suername - атрибут клсса, наследуемые от Person (имя, фамилия)
    courses_attached - атрибут класса (список, прикрепленные курсы)
    метод класса Mentor rate_hw - pass, не может использовать
    """
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)
        self.rating = {}


    def info(self) -> None:
        """
        Метод выводит информацию о экземпляре класса Student
        :return:
        """
        print(f'Лектор. Имя: {self.name}, Фамилия: {self.surname}, Учебный поток: {self.courses_attached} '
              f'Рейтинг: {self.rating}')

    def rate_hw(self, student, course: list, grade: list) -> None:
        pass

    def __average_rating(self) -> int:
        """
        Метод высчитывает средний бал экземпляра класса Lector
        :return: число (средний балл)
        """
        result = 0
        for rating in self.rating.values():
            result = sum(rating) / 2
        return result

    def __lt__(self, lector):
        """
        Метод сравнения среднего балла экземпляра класса Student
        :param student: экземпляр класса Lector
        :return: булевое
        """
        return self.__average_rating() == lector.__average_rating()

    def __str__(self) -> str:
        """
        Метод выводит информацию о экземпляре класса Student
        :return: строка
        """
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.__average_rating()}'

class Reviewer(Mentor):
    """
    Reviewer - множественное наследование от классов Mentor, Person
    name, suername - атрибут клсса, наследуемые от Person (имя, фамилия)
    courses_attached - атрибут класса (список, прикрепленные курсы)
    """
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)

    def info(self) -> None:
        """
        Метод выводит информацию о экземпляре класса Student
        :return:
        """
        print(f'Эксперт. Имя: {self.name}, Фамилия: {self.surname}, Учебный поток: {self.courses_attached}')

    def __str__(self) -> str:
        """
        Метод выводит информацию о экземпляре класса Student
        :return: строка
        """
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student1 = Student('Иван', 'Иванов')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['JS']
student2 = Student('Артем', 'Артемов')
student2.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']


mentor1 = Mentor('Петр', 'Петров')
mentor1.courses_attached += ['Python']
mentor1.courses_attached += ['JS']

mentor1.rate_hw(student1, 'Python', 5)
mentor1.rate_hw(student1, 'Python', 7)
mentor1.rate_hw(student1, 'JS', 8)
mentor1.rate_hw(student1, 'JS', 2)
mentor1.rate_hw(student2, 'Python', 9)
lector = Lecturer('Михайлов', 'Михаил')
lector.courses_attached += ['Python']
lector2 = Lecturer('Павел', 'Павлов')
lector2.courses_attached += ['Python']
student1.grade_raiting(lector, 'Python', 10)
student2.grade_raiting(lector, 'Python', 7)
student2.grade_raiting(lector, 'Python', 11)
student1.grade_raiting(lector2, 'Python', 6)
student2.grade_raiting(lector2, 'Python', 7)
student2.grade_raiting(lector2, 'Python', 8)
student2.grade_raiting(lector, 'JS', 11)

reviewer = Reviewer('Степан', 'Степанов')
reviewer.courses_attached += ['FPD-100']

print()
print(lector)
print()
print(reviewer)

if (student1 < student2):
    print(f'Средний бал студента "{student1.name} {student1.surname}" меньше '
          f'чем у студента "{student2.name} {student2.surname}"')
else:
    print(f'Средний бал студента "{student1.name} {student1.surname}" больше '
          f'чем у студента "{student2.name} {student2.surname}"')

if (lector < lector2):
    print(f'Средняя оценка лектора "{lector.name} {lector.surname}" меньше '
          f'чем у лектора "{lector2.name} {lector2.surname}"')
else:
    print(f'Средняя оценка лектора "{lector.name} {lector.surname}" больше '
          f'чем у лектора "{lector2.name} {lector2.surname}"')

def course_average_grade(students: list, course: str) -> dict:
    course_grade_dict = {}
    grade_sum =[]
    for student in students:
        grade_sum += student.grades[course]
        course_grade_dict[course] = sum(grade_sum) / len(grade_sum)
    return course_grade_dict

def course_average_rating(lectors: list, course: str) -> dict:
    course_raiting_dict = {}
    rating_sum =[]
    for lector in lectors:
        rating_sum += lector.rating[course]
        course_raiting_dict[course] = sum(rating_sum) / len(rating_sum)
    return course_raiting_dict

students = []
students.append(student1)
students.append(student2)

lectors = []
lectors.append(lector)
lectors.append(lector2)


print()
print(student1)
print()
print(student2)
print()
print(lector)
print(lector2)
print()

for course, grade in course_average_grade(students, 'Python').items():
    print(f'По курсу {course} средний балл среди всех студентов: {grade}')

for course, rating in course_average_rating(lectors, 'Python').items():
    print(f'По курсу {course} средний рейтинг среди всех лекторов: {rating}')