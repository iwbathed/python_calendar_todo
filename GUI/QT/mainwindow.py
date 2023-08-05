# This Python file uses the following encoding: utf-8
import sys

from datetime import datetime

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QMainWindow


from BasicFunctional.TagCrud import TagCrud
from BasicFunctional.TaskCrud import TaskCrud
from GUI.QT.Functional.RepeatOptionsGUI import RepeatOptionsGUI
from GUI.QT.Functional.StatusOptionsGUI import StatusOptionsGUI
from GUI.QT.Functional.TagGUI import TagGUI
from GUI.QT.Functional.TaskGUI import TaskGUI
from Tag import Tag
from Task import Task

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.task = Task()
        self.tag = Tag()

        TaskCrud.update_tasks_status_according_to_the_date()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.task_gui = TaskGUI(self.ui, self.task)
        self.ui.comboBox_tags_view.set_task_gui(self.task_gui)
        self.ui.comboBox_repeat_task_view.set_task_gui(self.task_gui)
        self.tag_gui = TagGUI(self.ui, self.tag)
        self.repeat_options_gui = RepeatOptionsGUI(self.ui)
        self.status_options_gui = StatusOptionsGUI(self.ui)

        self.ui.label_todays_date.setText(str(datetime.today().date()))

        self.calendar = self.ui.calendarWidget
        self.calendar.clicked.connect(self.task_gui.on_date_clicked)

        self.task_list = self.ui.listWidget_tasks
        self.task_list.itemClicked.connect(self.task_gui.on_task_item_clicked)

        self.ui.listWidget_tags.itemClicked.connect(self.tag_gui.on_tag_item_clicked)

        self.ui.pushButton_new_task.clicked.connect(self.task_gui.on_new_task_clicked)
        self.ui.pushButton_task_edit_cancel.clicked.connect(self.task_gui.on_task_edit_cancel_clicked)
        self.ui.pushButton_edit_task.clicked.connect(self.task_gui.on_edit_task_clicked)

        self.ui.pushButton_save_tag.clicked.connect(self.tag_gui.on_save_tag_clicked)
        self.ui.pushButton_mananege_tags.clicked.connect(self.tag_gui.on_tag_manage_clicked)
        self.ui.pushButton_edit_tag.clicked.connect(self.tag_gui.on_tag_edit_clicked)
        self.ui.pushButton_tag_edit_cancel.clicked.connect(self.tag_gui.on_tag_edit_cancel_clicked)
        self.ui.pushButton_save_edited_tag.clicked.connect(self.tag_gui.on_edited_tag_save_clicked)
        self.ui.pushButton_task_save.clicked.connect(self.task_gui.on_save_task_clicked)
        self.ui.pushButton_delete_tag.clicked.connect(self.tag_gui.on_tag_delete_clicked)
        self.ui.pushButton_mark_as_done.clicked.connect(self.task_gui.on_task_mark_as_done_undone_clicked)
        self.ui.pushButton_delete_task.clicked.connect(self.task_gui.on_delete_clicked)
        self.ui.pushButton_date_period_ok.clicked.connect(self.task_gui.on_period_ok_clicked)
        self.ui.pushButton_for_all_period.clicked.connect(self.task_gui.on_tasks_for_all_time_clicked)

        # function after start
        TagCrud.create_default_tag()
        self.tag_gui.load_tag_names_to_all_combo_boxes()
        self.repeat_options_gui.load_repeat_options_to_all_combo_boxes()
        self.status_options_gui.load_status_options_to_all_combo_boxes()
        self.ui.dateEdit_task_edit.setDisplayFormat("yyyy-MM-dd")
        self.ui.dateEdit_from.setDisplayFormat("yyyy-MM-dd")
        self.ui.dateEdit_to.setDisplayFormat("yyyy-MM-dd")
        self.ui.dateEdit_task_edit.setDate(datetime.today().date())
        self.ui.dateEdit_from.setDate(datetime.today().date())
        self.ui.dateEdit_to.setDate(datetime.today().date())
        self.task_gui.on_date_clicked(
            QDate.fromString(
                datetime.today().date().strftime('%Y-%m-%d'),
                'yyyy-MM-dd'
            )
        )

    # todo: add line for user information

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
