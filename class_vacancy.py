# import classes_api

class Vacancy:

    def __init__(self, name, url, salary_from, salary_to, requirement, responsibility, professional_roles, experience,
                 employment):
        """

        :param name: name vacancy
        :param url:  adress vacancy
        :param salary_from: oklad nachalo c ....
        :param salary_to: oklad do ....
        :param requirement:  obrazovanie
        :param responsibility: obzannosti
        :param professional_roles: doljnost
        :param experience: opit raboti
        :param employment: zanyatist
        """

        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = 'rub.'
        self.salary = f"{self.salary_from} - {self.salary_to}"
        self.requirement = requirement
        self.responsibility = responsibility
        self.professional_roles = professional_roles
        self.experience = experience
        self.employment = employment

    def __gt__(self, other):
        if isinstance(other, (int, Vacancy)):
            raise TypeError("not int")

        sc = other if isinstance(other, int) else other.salary_from
        return self.salary_from > sc

    @staticmethod
    def sorted_by_salary(not_sorted_vacancies: list):
        count_of_vacancies = len(not_sorted_vacancies)
        sorted_vacancies = []
        highest_salary_from_value = 0
        highest_salary_from_sample = None

        while len(sorted_vacancies) != count_of_vacancies:

            for vacancy in not_sorted_vacancies:

                if vacancy.salary_from >= highest_salary_from_value:
                    highest_salary_from_value = vacancy.salary_from
                    highest_salary_from_sample = vacancy
            sorted_vacancies.append(highest_salary_from_sample)
            not_sorted_vacancies.remove(highest_salary_from_sample)

            highest_salary_from_value = 0

        return sorted_vacancies
