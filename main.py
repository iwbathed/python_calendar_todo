# This is a sample Python script.
from FileCrud import FileCrud
from Enums.RepeatEnum import RepeatEnum
from Enums.TaskEnum import TaskEnum
from Enums.StatusEnum import StatusEnum
from Task import Task
from datetime import datetime

from Terminal.TaskCrud import TaskCrud
import pprint

def main():
    task = Task()

    while True:
        choice = input("Create task - 1\nRead - 2\n"
                       "Tasks for today - 3\nGet task by id - 4\n"
                       "Update task by id - 5\nDelete task by id - 6\n"
                       "Tasks for next 7 days - 7\n"
                       "Exit - q\n")
        if choice == "1":
            TaskCrud.create_task(task)
            file_name = str(datetime.strptime(task.get_task_attribute(TaskEnum.DEADLINE_DATE.value), "%Y-%m-%d").year)

            FileCrud.upload_task(file_name, task.task)
        elif choice == "2":
            file_name = input("Filename: ")
            pprint.pprint(FileCrud.read_file(file_name))
        elif choice == "3":
            pprint.pprint(TaskCrud.get_tasks_for_today())
        elif choice == "4":
            file_name = input("Filename (year): ")
            task_id = input("Task id: ")
            current_task = TaskCrud.get_task_by_id(file_name, task_id)
            if current_task:
                print(current_task)
            else:
                print(f"No task with id {task_id} in {file_name}")
        elif choice == "5":
            file_name = input("Filename (year): ")
            task_id = input("Task id: ")
            current_task = TaskCrud.get_task_by_id(file_name, task_id)
            if current_task:
                print(current_task)
                print("To leave unchanged input empty")
                for member in TaskEnum:
                    if member != TaskEnum.ID and member != TaskEnum.REPEAT:
                        user_input = input(f"{member.value} : ")
                        if user_input != "":
                            current_task[member.value] = user_input
                FileCrud.update_task_in_file(file_name, current_task)
            else:
                print(f"No task with id {task_id} in {file_name}")

        elif choice == "6":
            file_name = input("Filename (year): ")
            task_id = input("Task id: ")
            current_task = TaskCrud.get_task_by_id(file_name, task_id)
            if current_task:
                FileCrud.delete_task_in_file_by_id(file_name, task_id)
                print(f"Task with id {task_id} successfully deleted.")
            else:
                print(f"No task with id {task_id} in {file_name}")
        elif choice == "7":
            pprint.pprint(TaskCrud.get_tasks_for_next_seven_days())
        elif choice == "q":
            break

if __name__ == '__main__':
    main()

