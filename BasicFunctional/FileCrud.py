import os
import json

from Enums.TaskEnum import TaskEnum
from Settings import PROJECT_FOLDER, TASKS_FOLDER


class FileCrud:
    @staticmethod
    def file_name_to_json(file_name):
        if file_name[-5:] != ".json":
            return file_name + ".json"
        return file_name

    @staticmethod
    def upload_task(file_name, task):
        file_name = FileCrud.file_name_to_json(file_name)
        task_file_path = os.path.join(PROJECT_FOLDER, TASKS_FOLDER, file_name)
        if not os.path.exists(os.path.join(PROJECT_FOLDER, TASKS_FOLDER)):
            os.mkdir(os.path.join(PROJECT_FOLDER, TASKS_FOLDER))
        if not os.path.exists(task_file_path):
            FileCrud.create_file(task_file_path, task)
        else:
            FileCrud.update_file(file_name, task)

    @staticmethod
    def create_file(file_name, task):
        file_name = FileCrud.file_name_to_json(file_name)
        task_file_path = os.path.join(PROJECT_FOLDER, TASKS_FOLDER, file_name)
        with open(task_file_path, "w") as write_file:
            if not isinstance(task, list):
                task = [task]
            json.dump(task, write_file, indent=4)

    @staticmethod
    def read_file(file_name):
        file_name = FileCrud.file_name_to_json(file_name)
        task_file_path = os.path.join(PROJECT_FOLDER, TASKS_FOLDER, file_name)
        if os.path.exists(task_file_path):
            with open(task_file_path, "r") as read_file:
                return json.load(read_file)
        else:
            print("No such file or directory")

    @staticmethod
    def update_file(file_name, task):
        current_json = FileCrud.read_file(file_name)
        current_json.append(task)
        FileCrud.create_file(file_name, current_json)

    @staticmethod
    def delete_file(file_name):
        file_name = FileCrud.file_name_to_json(file_name)
        task_file_path = os.path.join(PROJECT_FOLDER, TASKS_FOLDER, file_name)
        if os.path.exists(task_file_path):
            os.remove(task_file_path)
        else:
            print("No such file or directory")

    @staticmethod
    def update_task_in_file(file_name, updated_task):
        tasks_from_file = FileCrud.read_file(file_name)
        for i in range(len(tasks_from_file)):
            if tasks_from_file[i][TaskEnum.ID.value] == updated_task[TaskEnum.ID.value]:
                tasks_from_file[i] = updated_task
                break
        FileCrud.create_file(file_name, tasks_from_file)

    @staticmethod
    def delete_task_in_file_by_id(file_name, task_id):
        tasks_from_file = FileCrud.read_file(file_name)
        for i in range(len(tasks_from_file)):
            if tasks_from_file[i][TaskEnum.ID.value] == str(task_id):
                tasks_from_file.pop(i)
                break
        FileCrud.create_file(file_name, tasks_from_file)




