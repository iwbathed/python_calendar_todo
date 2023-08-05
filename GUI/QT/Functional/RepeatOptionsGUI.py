from Enums.RepeatEnum import RepeatEnum


class RepeatOptionsGUI:
    def __init__(self, ui):
        self.ui = ui

    def load_repeat_options_to_all_combo_boxes(self):
        all_repeat_option_names = [member.value for member in RepeatEnum]
        self.ui.comboBox_repeat_task_edit.clear()
        self.ui.comboBox_repeat_task_view.clear()
        for tag_name in all_repeat_option_names:
            self.ui.comboBox_repeat_task_edit.addItem(tag_name)
            self.ui.comboBox_repeat_task_view.addItem(tag_name)

