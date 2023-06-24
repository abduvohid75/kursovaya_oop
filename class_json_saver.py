# coding: utf8
import json
import os
from abc import ABC, abstractmethod


class Saver(ABC):

    @staticmethod
    @abstractmethod
    def save_vacancies(objects):
        pass

    @staticmethod
    @abstractmethod
    def add_vacancies(sorted_vacancies: list, top_vacancies: int):
        pass

    @staticmethod
    @abstractmethod
    def get_vacancies_by_salary(salary_from: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_vacancies():
        pass


class JSONSaver(Saver):
    """
    Сохранение информации о вакансиях в файл

    """

    @staticmethod
    def save_vacancies_hh(objects):
        """
        Сохранение информации о вакансиях сайта HH в файл hh_jobs.json

        """
        file_write_jobs = 'hh_jobs.json'
        with open(file_write_jobs, 'a', encoding="utf-8") as add_file:
            if os.stat(file_write_jobs).st_size == 0:
                json.dump(objects["items"], add_file, indent=4)
                add_file.close()

            else:
                with open(file_write_jobs, encoding="utf-8") as json_file_read:
                    content = json.load(json_file_read)
                    json_file_read.close()
                    for vacancy in objects["items"]:
                        content.append(vacancy)

                with open(file_write_jobs, "w", encoding="utf-8") as json_file_write:
                    json.dump(content, json_file_write, indent=4)
                    json_file_write.close()

            print(f"LOADING: 50 %")

    def save_vacancies_sj(objects):
        """
        Сохранение информации о вакансиях сайта SJ в файл sj_jobs.json
        """
        file_write_jobs = 'sj_jobs.json'
        with open(file_write_jobs, 'a', encoding="utf-8") as add_file:
            if os.stat(file_write_jobs).st_size == 0:
                json.dump(objects["objects"], add_file, indent=4)
                add_file.close()

            else:
                with open(file_write_jobs, encoding="utf-8") as json_file_read:
                    content = json.load(json_file_read)
                    json_file_read.close()
                    for vacancy in objects["objects"]:
                        content.append(vacancy)

                with open(file_write_jobs, "w", encoding="utf-8") as json_file_write:
                    json.dump(content, json_file_write, indent=4)
                    json_file_write.close()

            print(f"LOADING: 100 %")

    @staticmethod
    def add_vacancies(sorted_vacancies: list, top_vacancies: int):

        """
            Добавление записей в файл. Если в файле имеются записи, старые не удаляются

        """
        itaration = 0

        for vacancy_sample in sorted_vacancies:
            vacancy_to_json = {"items": {
                "name": vacancy_sample.name,
                "url": vacancy_sample.url,
                "salary_from": vacancy_sample.salary_from,
                "salary_to": vacancy_sample.salary_to,
                "currency": vacancy_sample.currency,
                "requirement": vacancy_sample.requirement,
                "responsibility": vacancy_sample.responsibility,
                "professional_roles": vacancy_sample.professional_roles,
                "experience": vacancy_sample.experience,
                "employment": vacancy_sample.employment
            }
            }

            with open("vacancies.json", "a") as json_file:
                if os.stat("vacancies.json").st_size == 0:
                    json.dump([vacancy_to_json], json_file, indent=4)
                    json_file.close()
                else:
                    with open("vacancies.json") as json_file_read:
                        content = json.load(json_file_read)
                        json_file_read.close()

                    with open("vacancies.json", "w") as json_file_write:
                        content.append(vacancy_to_json)
                        json.dump(content, json_file_write, indent=4)
                        json_file_write.close()
            itaration += 1
            if itaration == top_vacancies:
                break

    @staticmethod
    def get_vacancies_by_salary(salary_from: int):

        vacancies_sorted_by_salary = []
        try:
            with open("vacancies.json") as json_file_read:
                content = json.load(json_file_read)
                json_file_read.close()
                os.remove("vacancies.json")
        except FileNotFoundError:
            print('')
        else:

            for vacancy in content:
                if vacancy["items"]["salary_from"] >= salary_from:
                    vacancies_sorted_by_salary.append(vacancy)

            with open("vacancies.json") as json_file_write:
                content = vacancies_sorted_by_salary
                json.dump(content, json_file_write, indent=4)
                json_file_write.close()

    @staticmethod
    def delete_vacancies():

        try:
            os.remove("vacancies.json")
        except FileNotFoundError:
            print('')
