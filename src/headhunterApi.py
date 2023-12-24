import requests

from src.abs_class import InterfaceApi
from src.class_ParsingError import ParsingError


class HeadHunterAPI(InterfaceApi):
    def __init__(self, keyword):
        self.keyword = keyword
        self.__header = {"User-Agent": "2001dflbv@gmail.com"}
        self.__params = {
            "text": keyword,
            "page": 0,
            "per_page": 100,
        }
        self.__vacancies = []  # список вакансий, который заполняется  по мерере получения данных по api

    @property
    def vacancies(self):
        return self.__vacancies

    def get_request(self):
        """
        Получение значений через API
        :return:
        """
        response = requests.get("https://api.hh.ru/vacancies", headers=self.__header, params=self.__params)
        if response.status_code != 200:
            raise ParsingError
        return response.json()["items"]

    def get_vacancies(self, pages_count=1):
        while self.__params["page"] < pages_count:
            print(f"HeadHanter, Парсинг страницы {self.__params['page'] + 1}", end=": ")
            try:
                values = self.get_request()
            except ParsingError:
                print("Ошибка при получении данных")
                break
            print(f"Найдено ({len(values)}) вакансий")
            self.__vacancies.extend(values)
            self.__params["page"] += 1

    @staticmethod
    def get_salary(salary):
        formated_salary = [None, None]
        if salary and salary["from"] and salary["from"] != 0:
            formated_salary[0] = salary["from"] if salary["currency"].lower == "rur" else salary["from"]
        if salary and salary["to"] and salary["to"] != 0:
            formated_salary[1] = salary["to"] if salary["currency"].lower == "rur" else salary["to"]
        return formated_salary

    def get_formatted_vacancies(self):
        formatted_vacancies = []
        for vacancy in self.__vacancies:
            salary_from, salary_to = self.get_salary(vacancy["salary"])
            formatted_vacancies.append({
                "id": vacancy["id"],
                "title": vacancy["name"],
                "url": vacancy["alternate_url"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "employer": vacancy["employer"]["name"],
                "api": "HeadHunter",
            })
        return formatted_vacancies


if __name__ == '__main__':
    hh_api = HeadHunterAPI('Python')
    hh_api.get_vacancies()
    print(hh_api.vacancies)
