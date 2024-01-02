from abc import ABC, abstractmethod


class InterfaceApi(ABC):
    """ Абстрактный класс"""

    @abstractmethod
    def get_request(self):
        pass

    def get_vacancies(self):
        pass
