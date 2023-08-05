import pprint
from datetime import datetime, timedelta

from PySide6 import QtCore
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QListWidgetItem

from Enums.StatusEnum import StatusEnum
from Enums.TagEnum import TagEnum
from Enums.TaskEnum import TaskEnum
from BasicFunctional.FileCrud import FileCrud
from GUI.QT.Enums.QtRolesEnum import QtRolesEnum
from Settings import DATE_FORMAT
from BasicFunctional.TagCrud import TagCrud
from BasicFunctional.TaskCrud import TaskCrud
from PySide6.QtGui import Qt


class TaskGUI:
    def __init__(self, ui, task):
        self.ui = ui
        self.task_create_edit = True
        self.task = task
        self.current_task_item = None
        self.current_Qdate = None

    def on_period_ok_clicked(self):
        from_date = self.ui.dateEdit_from.date()
        to_date = self.ui.dateEdit_to.date()
        start_date = min(from_date, to_date)
        end_date = max(from_date, to_date)
        all_tasks = []
        current_date = start_date
        while current_date <= end_date:
            all_tasks.extend(TaskCrud.get_tasks_by_date(current_date.toString("yyyy-MM-dd")))
            current_date = current_date.addDays(1)

        all_tasks = self.get_tasks_by_chosen_options(all_tasks, TaskEnum.TAG.value)
        all_tasks = self.get_tasks_by_chosen_options(all_tasks, TaskEnum.REPEAT.value)
        all_tasks = self.get_tasks_by_chosen_options(all_tasks, TaskEnum.STATUS.value)
        self.show_tasks(all_tasks)

    def on_tasks_for_all_time_clicked(self):

        all_tasks = TaskCrud.get_all_task()
        all_tasks = self.get_tasks_by_chosen_options(all_tasks, TaskEnum.TAG.value)
        all_tasks = self.get_tasks_by_chosen_options(all_tasks, TaskEnum.REPEAT.value)
        all_tasks = self.get_tasks_by_chosen_options(all_tasks, TaskEnum.STATUS.value)
        self.show_tasks(all_tasks)

    def on_new_task_clicked(self):
        self.ui.textEdit_task_name.clear()
        self.ui.textEdit_task_description.clear()
        if self.ui.comboBox_task_edit_tags.count() > 0:
            self.ui.comboBox_task_edit_tags.setCurrentIndex(0)
        if self.ui.comboBox_repeat_task_edit.count() > 0:
            self.ui.comboBox_repeat_task_edit.setCurrentIndex(0)

        self.ui.dateEdit_task_edit.setDate(datetime.today().date())
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_task_edit)
        self.task_create_edit = True

    def on_edit_task_clicked(self):
        if self.current_task_item:
            self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_task_edit)

            index = self.ui.comboBox_task_edit_tags.findText(
                self.current_task_item.data(QtRolesEnum.TAG.value),
                QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.ui.comboBox_task_edit_tags.setCurrentIndex(index)

            index = self.ui.comboBox_repeat_task_edit.findText(
                self.current_task_item.data(QtRolesEnum.REPEAT.value),
                QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.ui.comboBox_repeat_task_edit.setCurrentIndex(index)

            self.ui.textEdit_task_name.setText(self.current_task_item.data(QtRolesEnum.NAME.value))
            self.ui.textEdit_task_description.setText(
                self.current_task_item.data(QtRolesEnum.DESCRIPTION.value))
            self.task_create_edit = False

    def on_task_mark_as_done_undone_clicked(self):
        current_status = self.current_task_item.data(QtRolesEnum.STATUS.value)
        if current_status == StatusEnum.DONE.value:
            current_status = StatusEnum.NOT_DONE.value
        elif current_status == StatusEnum.NOT_DONE.value or \
                current_status == StatusEnum.OVERDUE.value:
            current_status = StatusEnum.DONE.value


        TaskCrud.update_task(
            self.task, self.current_task_item.data(QtRolesEnum.ID.value),
            self.current_task_item.data(QtRolesEnum.NAME.value), self.current_task_item.data(QtRolesEnum.DESCRIPTION.value),
            self.current_task_item.data(QtRolesEnum.TAG.value),
            current_status,
            self.current_task_item.data(QtRolesEnum.CREATION_DATE.value),
            self.current_task_item.data(QtRolesEnum.DEADLINE_DATE.value),
            self.current_task_item.data(QtRolesEnum.REPEAT.value)
        )
        self.current_task_item.data(QtRolesEnum.DEADLINE_DATE.value)

        filename = str(
            datetime.strptime(
                self.current_task_item.data(QtRolesEnum.DEADLINE_DATE.value),
                DATE_FORMAT
            ).year
        ) + ".json"
        FileCrud.update_task_in_file(filename, self.task.task)



        # self.on_date_clicked(
        #     QDate.fromString(self.current_task_item.data(QtRolesEnum.DEADLINE_DATE.value), 'yyyy-MM-dd')
        # )

        self.refresh_task_item()
        # current_item = self.get_task_item_from_listWidget_by_id(
        #     self.current_task_item.data(QtRolesEnum.ID.value)
        # )
        self.on_task_item_clicked(self.current_task_item)


    def get_tasks_by_chosen_options(self, tasks, enum_option_value):
        chosen_options = []
        if enum_option_value == TaskEnum.TAG.value:
            chosen_options = self.ui.comboBox_tags_view.get_current_chosen_options()

        elif enum_option_value == TaskEnum.REPEAT.value:
            chosen_options = self.ui.comboBox_repeat_task_view.get_current_chosen_options()
        elif enum_option_value == TaskEnum.STATUS.value:
            chosen_options = self.ui.comboBox_status_task_view.get_current_chosen_options()

        chosen_options = [option.text() for option in chosen_options]

        print("chosen_options")
        print(chosen_options)
        tasks_filtred = []
        for task in tasks:
            if task[enum_option_value] in chosen_options:
                tasks_filtred.append(task)
        return tasks_filtred


    def get_task_item_from_listWidget_by_id(self, task_id):
        item_count = self.ui.listWidget_tasks.count()
        for i in range(item_count):
            current_item = self.ui.listWidget_tasks.item(i)
            if current_item.data(QtRolesEnum.ID.value) == task_id:
                return current_item

    def on_save_task_clicked(self):
        task_name = self.ui.textEdit_task_name.toPlainText()
        if task_name != "":
            task_description = self.ui.textEdit_task_description.toPlainText()
            task_tag = self.ui.comboBox_task_edit_tags.currentText()
            task_repeat = self.ui.comboBox_repeat_task_edit.currentText()
            task_deadline = self.ui.dateEdit_task_edit.date()
            if self.task_create_edit:
                TaskCrud.create_task_from_parameters(self.task, task_name,
                                                     task_description, task_tag,
                                                     task_repeat, task_deadline.toString("yyyy-MM-dd"))
                filename = str(task_deadline.year()) + ".json"
                FileCrud.upload_task(filename, self.task.task)

                tag = TagCrud.get_tag_by_tag_name(task_tag)
                if filename not in tag[TagEnum.USED_IN_FILES.value]:
                    tag[TagEnum.USED_IN_FILES.value].append(filename)
                    TagCrud.update_tag_used_filenames(task_tag,
                                                      tag[TagEnum.USED_IN_FILES.value])

            # todo: on edited save pressed reaction
            else:
                TaskCrud.update_task(
                    self.task, self.current_task_item.data(QtRolesEnum.ID.value),
                    task_name, task_description,
                    task_tag, self.current_task_item.data(QtRolesEnum.STATUS.value),
                    self.current_task_item.data(QtRolesEnum.CREATION_DATE.value),
                    task_deadline.toString("yyyy-MM-dd"),
                    task_repeat
                )

                if datetime.strptime(
                        self.current_task_item.data(QtRolesEnum.DEADLINE_DATE.value),
                        DATE_FORMAT).year == task_deadline.year():
                    FileCrud.update_task_in_file(str(task_deadline.year()), self.task.task)

                    filename = str(task_deadline.year()) + ".json"
                    tag = TagCrud.get_tag_by_tag_name(self.task.get_task_attribute(TaskEnum.TAG.value))
                    if filename not in tag[TagEnum.USED_IN_FILES.value]:
                        tag[TagEnum.USED_IN_FILES.value].append(filename)

                    TagCrud.update_tag_used_filenames(tag[TagEnum.NAME.value],
                                                      tag[TagEnum.USED_IN_FILES.value])
                else:
                    old_filename = str(
                        datetime.strptime(
                            self.current_task_item.data(QtRolesEnum.DEADLINE_DATE.value),
                            DATE_FORMAT).year
                    ) + ".json"

                    FileCrud.delete_task_in_file_by_id(
                        old_filename,
                        self.current_task_item.data(QtRolesEnum.ID.value)
                    )

                    new_file_name = str(
                        datetime.strptime(
                            self.task.get_task_attribute(TaskEnum.DEADLINE_DATE.value), "%Y-%m-%d").year
                    ) + ".json"
                    FileCrud.upload_task(new_file_name, self.task.task)

                    all_tags_from_old_file = TagCrud.get_all_tags_from_tasks_in_file(old_filename)

                    tag = TagCrud.get_tag_by_tag_name(self.task.get_task_attribute(TaskEnum.TAG.value))
                    if self.task.get_task_attribute(TaskEnum.TAG.value) not in all_tags_from_old_file:
                        tag[TagEnum.USED_IN_FILES.value].remove(old_filename)

                    if new_file_name not in tag[TagEnum.USED_IN_FILES.value]:
                        tag[TagEnum.USED_IN_FILES.value].append(new_file_name)

                    TagCrud.update_tag_used_filenames(tag[TagEnum.NAME.value],
                                                      tag[TagEnum.USED_IN_FILES.value])

                start_filename_of_edited_tasks = str(
                    datetime.strptime(
                        self.current_task_item.data(QtRolesEnum.DEADLINE_DATE.value), "%Y-%m-%d").year
                ) + ".json"

                tags_from_file = TagCrud.get_all_tags_from_tasks_in_file(start_filename_of_edited_tasks)
                if self.current_task_item.data(QtRolesEnum.TAG.value) not in tags_from_file:
                    tag = TagCrud.get_tag_by_tag_name(self.current_task_item.data(QtRolesEnum.TAG.value))
                    tag[TagEnum.USED_IN_FILES.value].remove(start_filename_of_edited_tasks)
                    TagCrud.update_tag_used_filenames(tag[TagEnum.NAME.value],
                                                      tag[TagEnum.USED_IN_FILES.value])

            print(f"self.ui.comboBox_tags_view.getOptionIndexByName(task_tag) "
                  f"{self.ui.comboBox_tags_view.getOptionIndexByName(task_tag)}")
            self.ui.comboBox_tags_view.set_item_checked(
                self.ui.comboBox_tags_view.getOptionIndexByName(task_tag)
            )
            self.ui.comboBox_repeat_task_view.set_item_checked(
                self.ui.comboBox_repeat_task_view.getOptionIndexByName(task_repeat)
            )

            self.ui.comboBox_status_task_view.set_item_checked(
                self.ui.comboBox_status_task_view.getOptionIndexByName(StatusEnum.NOT_DONE.value)
            )
            self.ui.comboBox_status_task_view.set_item_checked(
                self.ui.comboBox_status_task_view.getOptionIndexByName(StatusEnum.DONE.value)
            )
            self.ui.comboBox_status_task_view.set_item_checked(
                self.ui.comboBox_status_task_view.getOptionIndexByName(StatusEnum.OVERDUE.value)
            )




            self.on_date_clicked(task_deadline)
            self.current_task_item = self.get_task_item_from_listWidget_by_id(
                self.task.get_task_attribute(TaskEnum.ID.value))



            self.on_task_item_clicked(self.current_task_item)

    def on_delete_clicked(self):
        task_deadline = QDate.fromString(
                self.current_task_item.data(QtRolesEnum.DEADLINE_DATE.value),
                'yyyy-MM-dd'
            )
        filename = str(
                datetime.strptime(
                    self.current_task_item.data(QtRolesEnum.DEADLINE_DATE.value), "%Y-%m-%d").year
            ) + ".json"


        FileCrud.delete_task_in_file_by_id(filename,
                                           self.current_task_item.data(QtRolesEnum.ID.value))
        all_tags_from_current_file = TagCrud.get_all_tags_from_tasks_in_file(filename)

        print(filename)
        print(self.current_task_item.data(QtRolesEnum.TAG.value))
        print(f"all_tags_from_current_file <{all_tags_from_current_file}>")

        if self.current_task_item.data(QtRolesEnum.TAG.value) not in all_tags_from_current_file:
            print("if")
            tag = TagCrud.get_tag_by_tag_name(self.current_task_item.data(QtRolesEnum.TAG.value))
            tag[TagEnum.USED_IN_FILES.value].remove(filename)

            TagCrud.update_tag_used_filenames(tag[TagEnum.NAME.value],
                                              tag[TagEnum.USED_IN_FILES.value])

        self.on_date_clicked(task_deadline)
        # current_item = self.get_task_item_from_listWidget_by_id(
        #     self.task.get_task_attribute(TaskEnum.ID.value))
        self.on_new_task_clicked()



    def on_task_edit_cancel_clicked(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_task_view)
        # self.ui.textBrowser_task_name.clear()
        self.ui.textEdit_task_description.clear()

    def show_tasks(self, tasks):
        self.ui.listWidget_tasks.clear()
        for task in tasks:
            text_for_item = f"{task[TaskEnum.NAME.value]} "
            task_item = QListWidgetItem(text_for_item)

            task_item.setData(QtRolesEnum.ID.value, task[TaskEnum.ID.value])
            task_item.setData(QtRolesEnum.NAME.value, task[TaskEnum.NAME.value])
            task_item.setData(QtRolesEnum.DESCRIPTION.value, task[TaskEnum.DESCRIPTION.value])
            task_item.setData(QtRolesEnum.STATUS.value, task[TaskEnum.STATUS.value])
            task_item.setData(QtRolesEnum.TAG.value, task[TaskEnum.TAG.value])
            task_item.setData(QtRolesEnum.CREATION_DATE.value, task[TaskEnum.CREATION_DATE.value])
            task_item.setData(QtRolesEnum.DEADLINE_DATE.value, task[TaskEnum.DEADLINE_DATE.value])
            task_item.setData(QtRolesEnum.REPEAT.value, task[TaskEnum.REPEAT.value])
            self.ui.listWidget_tasks.addItem(task_item)

    def on_date_clicked(self, date):
        self.current_Qdate = date
        print(f"on_date_clicked <{date.toString('yyyy-MM-dd')}>")
        tasks = TaskCrud.get_tasks_by_date(date.toString('yyyy-MM-dd'))
        print(tasks)
        tasks = self.get_tasks_by_chosen_options(tasks, TaskEnum.TAG.value)
        tasks = self.get_tasks_by_chosen_options(tasks, TaskEnum.REPEAT.value)
        tasks = self.get_tasks_by_chosen_options(tasks, TaskEnum.STATUS.value)
        print(tasks)
        self.show_tasks(tasks)

        self.ui.dateEdit_task_edit.setDate(date)
        pprint.pprint(tasks)

    def refresh_task_item(self):
        task_id = self.current_task_item.data(QtRolesEnum.ID.value)
        filename = str(datetime.strptime(
            self.current_task_item.data(QtRolesEnum.DEADLINE_DATE.value), DATE_FORMAT).year)
        task = TaskCrud.get_task_by_id(filename, task_id)

        self.current_task_item.setData(
            QtRolesEnum.NAME.value, task[TaskEnum.NAME.value])
        self.current_task_item.setData(
            QtRolesEnum.DESCRIPTION.value, task[TaskEnum.DESCRIPTION.value])
        self.current_task_item.setData(
            QtRolesEnum.STATUS.value, task[TaskEnum.STATUS.value])
        self.current_task_item.setData(
            QtRolesEnum.TAG.value, task[TaskEnum.TAG.value])
        self.current_task_item.setData(
            QtRolesEnum.CREATION_DATE.value, task[TaskEnum.CREATION_DATE.value])
        self.current_task_item.setData(
            QtRolesEnum.DEADLINE_DATE.value, task[TaskEnum.DEADLINE_DATE.value])
        self.current_task_item.setData(
            QtRolesEnum.REPEAT.value, task[TaskEnum.REPEAT.value])

    def on_task_item_clicked(self, item):
        if item.flags() & Qt.ItemIsEnabled:
            self.current_task_item = item
            self.refresh_task_item()
            self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_task_view)
            self.ui.textBrowser_task_name.setText(
                self.current_task_item.data(QtRolesEnum.NAME.value))
            self.ui.label_task_created_date.setText(
                self.current_task_item.data(QtRolesEnum.CREATION_DATE.value))
            self.ui.label_task_deadline_date.setText(
                self.current_task_item.data(QtRolesEnum.DEADLINE_DATE.value))

            self.ui.label_task_tag.setText(self.current_task_item.data(QtRolesEnum.TAG.value))
            self.ui.label_task_status.setText(self.current_task_item.data(QtRolesEnum.STATUS.value))

            self.ui.textBrowser_task_dscription.setText(
                self.current_task_item.data(QtRolesEnum.DESCRIPTION.value))


