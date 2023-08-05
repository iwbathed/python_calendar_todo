from Enums.StatusEnum import StatusEnum


class StatusOptionsGUI:
    def __init__(self, ui):
        self.ui = ui

    def load_status_options_to_all_combo_boxes(self):
        all_status_options = [member.value for member in StatusEnum]
        self.ui.comboBox_status_task_view.clear()

        for status in all_status_options:
            self.ui.comboBox_status_task_view.addItem(status)


