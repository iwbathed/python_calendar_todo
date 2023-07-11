
from Enums.TaskEnum import TaskEnum


class Task:
    def __init__(self):
        self.task = {

            TaskEnum.ID.value: "Default id",
            TaskEnum.NAME.value: "Default Name",
            TaskEnum.DESCRIPTION.value: "Default description",
            TaskEnum.STATUS.value: "Default status",
            TaskEnum.TAG.value: "Default tag",
            TaskEnum.CREATION_DATE.value: "Default date",
            TaskEnum.DEADLINE_DATE.value: "Default date",
            TaskEnum.REPEAT.value: "Default repeat",
        }

    def set_task_attribute(self, **kwargs):
        for key, value in kwargs.items():
            self.task[key] = value

    def get_task_attribute(self, attr):
        return self.task[attr]
