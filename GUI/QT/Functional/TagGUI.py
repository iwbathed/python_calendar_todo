import PySide6
from PySide6.QtWidgets import QListWidgetItem

from Enums.TagEnum import TagEnum
from Enums.TaskEnum import TaskEnum
from BasicFunctional.FileCrud import FileCrud
from BasicFunctional.TagCrud import TagCrud
from PySide6.QtGui import Qt

from Settings import DEFAULT_TAG_NAME


class TagGUI:
    def __init__(self, ui, tag):
        self.ui = ui
        self.tag = tag
        self.current_tag_item = None


    def on_save_tag_clicked(self):

        tag_name = self.ui.lineEdit_tag.text()
        if tag_name != "" and tag_name not in TagCrud.get_all_tag_names():
            self.tag.set_tag_attribute(
                **{TagEnum.NAME.value: tag_name},
                **{TagEnum.USED_IN_FILES.value: []}
            )

            TagCrud.write_tag_to_file(self.tag.tag)
        self.show_tags()
        self.ui.lineEdit_tag.clear()
        self.load_tag_names_to_all_combo_boxes()

    def on_tag_item_clicked(self, tag_item):
        self.current_tag_item = tag_item

    def on_tag_edit_clicked(self):
        if self.current_tag_item and self.current_tag_item.flags() & Qt.ItemIsEnabled:
            tag_name = self.current_tag_item.text()
            self.ui.stackedWidget_tag.setCurrentWidget(self.ui.page_tag_edit)
            self.ui.label_old_tag.setText(tag_name)
            self.ui.lineEdit_tag_edit.setText(tag_name)

    def on_tag_edit_cancel_clicked(self):
        self.ui.stackedWidget_tag.setCurrentWidget(self.ui.page_tag_create)

    def on_edited_tag_save_clicked(self):
        old_tag_name = self.ui.label_old_tag.text()
        new_tag_name = self.ui.lineEdit_tag_edit.text()

        TagCrud.update_tag_name(old_tag_name, new_tag_name)
        self.ui.stackedWidget_tag.setCurrentWidget(self.ui.page_tag_create)
        self.show_tags()
        self.load_tag_names_to_all_combo_boxes()

    def on_tag_delete_clicked(self):
        if self.current_tag_item and self.current_tag_item.flags() & Qt.ItemIsEnabled:
            tag_name = self.current_tag_item.text()
            current_tag = TagCrud.get_tag_by_tag_name(tag_name)
            print(current_tag[TagEnum.USED_IN_FILES.value])
            # DEFAULT_TAG_NAME = "Unassigned"
            if current_tag[TagEnum.NAME.value] == DEFAULT_TAG_NAME:
                print("you can not delete default tag <Unassigned>")
            else:

                if not current_tag[TagEnum.USED_IN_FILES.value]:  # IF TAG IS NOT USED
                    print("deleting")
                    TagCrud.delete_tag_from_file(current_tag[TagEnum.NAME.value])
                else:  # IF TAG IS USED
                    # todo: fix default_tag_name Unassigned deleting

                    print(DEFAULT_TAG_NAME)
                    default_tag = TagCrud.get_tag_by_tag_name(DEFAULT_TAG_NAME)
                    if default_tag:  # IF default_tag ALREADY EXIST
                        print(default_tag)
                        current_tag_set_of_files = set(current_tag[TagEnum.USED_IN_FILES.value])
                        default_tag_set_of_files = set(default_tag[TagEnum.USED_IN_FILES.value])
                        unique_elements = current_tag_set_of_files.difference(default_tag_set_of_files)
                        default_tag[TagEnum.USED_IN_FILES.value].extend(list(unique_elements))

                        TagCrud.update_tag_used_filenames(DEFAULT_TAG_NAME,
                                                          default_tag[TagEnum.USED_IN_FILES.value])

                        for filename in default_tag[TagEnum.USED_IN_FILES.value]:
                            tasks_from_file = FileCrud.read_file(filename)
                            for j in range(len(tasks_from_file)):
                                if tasks_from_file[j][TaskEnum.TAG.value] == tag_name:
                                    tasks_from_file[j][TaskEnum.TAG.value] = DEFAULT_TAG_NAME

                            FileCrud.create_file(filename, tasks_from_file)

                        TagCrud.delete_tag_from_file(current_tag[TagEnum.NAME.value])
                    else:
                        TagCrud.update_tag_name(tag_name, DEFAULT_TAG_NAME)

                self.ui.stackedWidget_tag.setCurrentWidget(self.ui.page_tag_create)
                self.show_tags()
                self.load_tag_names_to_all_combo_boxes()

    def on_tag_manage_clicked(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_tag_manage)
        self.show_tags()

    def show_tags(self):
        self.ui.listWidget_tags.clear()
        all_tags = TagCrud.get_all_tags()
        if all_tags:
            for tag in all_tags:
                self.ui.listWidget_tags.addItem(QListWidgetItem(tag[TagEnum.NAME.value]))


    def load_tag_names_to_all_combo_boxes(self):
        all_tag_names = TagCrud.get_all_tag_names()

        self.ui.comboBox_tags_view.clear()
        self.ui.comboBox_task_edit_tags.clear()
        for tag_name in all_tag_names:
            self.ui.comboBox_tags_view.addItem(tag_name)
            self.ui.comboBox_task_edit_tags.addItem(tag_name)

    #     self.set_all_tags_checked()
    # def set_all_tags_checked(self):
    #     all_tag_names = TagCrud.get_all_tag_names()
    #     tag_count = len(all_tag_names)
    #     for i in range(tag_count):
    #         self.ui.comboBox_tags_view.set_item_checked(i+1)



