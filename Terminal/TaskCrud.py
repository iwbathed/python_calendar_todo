from Enums.RepeatEnum import RepeatEnum
from Enums.StatusEnum import StatusEnum
from Enums.TaskEnum import TaskEnum
from datetime import datetime, timedelta

from FileCrud import FileCrud
from IdCreation.Id import Id
from Settings import DATE_FORMAT, DATE_EXAMPLE


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
    def get_tasks_for_next_seven_days():
        today_date = datetime.today().date()
        tasks_for_next_seven_days = []
        if today_date.month==12 and today_date.day > 24:
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

    # @staticmethod
    # def update_task(task, task_id):
    #
    #     task.set_task_attribute(
    #         **{TaskEnum.ID.value: task_id},
    #         **{TaskEnum.NAME.value: input("Task name : ")},
    #         **{TaskEnum.DESCRIPTION.value: input("Task details (description) : ")},
    #         **{TaskEnum.TAG.value: input("Task tag : ")},
    #         **{TaskEnum.STATUS.value: StatusEnum.NOT_DONE.value},
    #         **{TaskEnum.DEADLINE_DATE.value: TaskCrud._date_input()},
    #         **{TaskEnum.REPEAT.value: input(
    #             "Task repeat (" + ", ".join([member.value for member in RepeatEnum]) + ") : ")},
    #     )

