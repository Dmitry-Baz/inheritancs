class Mentor:
    def __init__(self, name, surname, courses=None):
        self.name = name
        self.surname = surname
        self.courses = courses if courses is not None else []

    def __str__(self):
        return f"{self.name} {self.surname}, Courses: {', '.join(self.courses)}"


class Lecturer(Mentor):
    def __init__(self, name, surname, courses=None, salary=0):
        super().__init__(name, surname, courses)
        self.salary = salary

    def __str__(self):
        return f"Learner: {super().__str__()}, Salary: {self.salary}"


class Reviewer(Mentor):
    def __init__(self, name, surname, courses=None):
        super().__init__(name, surname, courses)

    def __str__(self):
        return f"Reviewer: {super().__str__()}"


# Пример использования
lecturer1 = Lecturer("Alice", "Johnson", ["Python", "Data Science"], 5000)
reviewer1 = Reviewer("Bob", "Smith", ["Python", "Machine Learning"])

print(lecturer1)  # Вывод информации о лекторе
print(reviewer1)  # Вывод информации о рецензенте