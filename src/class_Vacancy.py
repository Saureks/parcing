
class Vacancy:
    __slots__ = ("vacancy_id", "title", "url", "salary_from", "salary_to", "employer", "api")

    def __init__(self, vacancy_id, title, url, salary_from, salary_to, employer, api):
        self.vacancy_id = vacancy_id
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employer = employer
        self.api = api

    """ Сортировка вакансий """

    def __gt__(self, other):
        if not other.salary_from:
            return True
        elif not self.salary_from:
            return False
        return self.salary_from >= other.salary_from

    def __str__(self):
        salary_from = f"От {self.salary_from}" if self.salary_from else ''
        salary_to = f"до {self.salary_to}" if self.salary_to else ""
        if self.salary_from is None and salary_to is None:
            salary_from = "Не указано"
        return f'Вакансия: \"{self.title}"\nКомпания: \"{self.employer}"\nЗарплата: {salary_from} {salary_to} \nURL: {self.url}'