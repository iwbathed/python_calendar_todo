import os

from Enums.RepeatEnum import RepeatEnum
from Enums.StatusEnum import StatusEnum
from Enums.TaskEnum import TaskEnum
from datetime import datetime, timedelta

from BasicFunctional.FileCrud import FileCrud
from IdCreation.Id import Id
from Settings import DATE_FORMAT, TASKS_PATH


class TaskCrud:
    @classmethod
    def _date_input(cls):
        while True:
            date_input = input(f"Input date for task (format: {DATE_FORMAT}, example: {str(datetime.today().date())}): ")
            try:
                datetime.strptime(date_input, DATE_FORMAT)
                if len(date_input) != 10:
                    raise ValueError
                return date_input
            except ValueError:
                print("Incorrect format")

    @staticmethod
    def create_task(task):
        task.set_task_attribute(
            **{TaskEnum.ID.value: Id.id_generate()},
            **{TaskEnum.NAME.value: input("Task name : ")},
            **{TaskEnum.DESCRIPTION.value: input("Task details (description) : ")},
            **{TaskEnum.TAG.value: input("Task tag : ")},
            **{TaskEnum.STATUS.value: StatusEnum.NOT_DONE.value},
            **{TaskEnum.CREATION_DATE.value: str(datetime.today().date())},
            **{TaskEnum.DEADLINE_DATE.value: TaskCrud._date_input()},
            **{TaskEnum.REPEAT.value: input(
                "Task repeat (" + ", ".join([member.value for member in RepeatEnum]) + ") : ")},
        )

    @staticmethod
    def create_task_from_parameters(task, name, description, tag, repeat, deadline_date):
        task.set_task_attribute(
            **{TaskEnum.ID.value: Id.id_generate()},
            **{TaskEnum.NAME.value: name},
            **{TaskEnum.DESCRIPTION.value: description},
            **{TaskEnum.TAG.value: tag},
            **{TaskEnum.STATUS.value: StatusEnum.NOT_DONE.value},
            **{TaskEnum.CREATION_DATE.value: str(datetime.today().date())},
            **{TaskEnum.DEADLINE_DATE.value: str(deadline_date)},
            **{TaskEnum.REPEAT.value: repeat},
        )
    @staticmethod
    def update_task(task, task_id, name, description, tag, status, creation_date, deadline_date, repeat):

        task.set_task_attribute(
            **{TaskEnum.ID.value: task_id},
            **{TaskEnum.NAME.value: name},
            **{TaskEnum.DESCRIPTION.value: description},
            **{TaskEnum.TAG.value: tag},
            **{TaskEnum.STATUS.value: status},
            **{TaskEnum.CREATION_DATE.value: creation_date},
            **{TaskEnum.DEADLINE_DATE.value: deadline_date},
            **{TaskEnum.REPEAT.value: repeat},
        )



    @staticmethod
    def get_all_task():
        all_tasks = []
        dir_list = os.listdir(TASKS_PATH)
        for filename in dir_list:
            if len(filename) > 5 and filename[-5:] == ".json":
                tasks = FileCrud.read_file(filename)
                all_tasks.extend(tasks)
        return all_tasks




    @staticmethod
    def get_tasks_for_today():
        today_date = datetime.today().date()
        file_name = str(today_date.year)+".json"
        tasks_json = FileCrud.read_file(file_name)
        tasks_for_today = []
        for task in tasks_json:
            if task[TaskEnum.DEADLINE_DATE.value] == str(today_date):
                tasks_for_today.append(task)
        return tasks_for_today

    @staticmethod
    def get_tasks_by_date(chosen_date):

        chosen_date = datetime.strptime(chosen_date, DATE_FORMAT).date()

        file_name = str(chosen_date.year) + ".json"
        tasks_json = FileCrud.read_file(file_name)
        tasks_for_chosen_date = []
        if tasks_json:
            for task in tasks_json:
                if task[TaskEnum.DEADLINE_DATE.value] == str(chosen_date):
                    tasks_for_chosen_date.append(task)
        return tasks_for_chosen_date

    @staticmethod
    def update_tasks_status_according_to_the_date():
        current_date = datetime.today().date()
        dir_list = os.listdir(TASKS_PATH)
        for filename in dir_list:
            if len(filename) > 5 and filename[-5:] == ".json":

                tasks = FileCrud.read_file(filename)

                for task in tasks:

                    if datetime.strptime(task[TaskEnum.DEADLINE_DATE.value], DATE_FORMAT).date() < current_date and\
                            task[TaskEnum.STATUS.value] == StatusEnum.NOT_DONE.value:
                        print(task)
                        task[TaskEnum.STATUS.value] = StatusEnum.OVERDUE.value
                FileCrud.create_file(filename, tasks)



    @staticmethod
    def get_tasks_for_next_seven_days():
        today_date = datetime.today().date()
        tasks_for_next_seven_days = []
        if today_date.month == 12 and today_date.day > 24:
            file_name = str(today_date.year) + ".json"
            tasks_json = FileCrud.read_file(file_name)
            file_name = str(today_date.year + timedelta(years=1)) + ".json"
            tasks_json.extend(FileCrud.read_file(file_name))
        else:
            file_name = str(today_date.year) + ".json"
            tasks_json = FileCrud.read_file(file_name)

        for task in tasks_json:
            task_date = datetime.strptime(
                task[TaskEnum.DEADLINE_DATE.value], DATE_FORMAT).date()
            if today_date <= task_date <= today_date + timedelta(days=6):
                         tasks_for_next_seven_days.append(task)
        return tasks_for_next_seven_days





    @staticmethod
    def get_task_by_id(file_name, task_id):
        file_name = FileCrud.file_name_to_json(file_name)
        tasks_json = FileCrud.read_file(file_name)
        for task in tasks_json:
            if task[TaskEnum.ID.value] == task_id:
                return task
        return None



