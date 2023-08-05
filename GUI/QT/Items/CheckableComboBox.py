import sys

from PySide6.QtCore import QEvent, Qt
from PySide6.QtGui import QStandardItem, QFontMetrics, QPalette, QStandardItemModel
from PySide6.QtWidgets import QStyledItemDelegate, QComboBox, QApplication


class CheckableComboBox(QComboBox):
    # Subclass Delegate to increase item height
    class Delegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(20)
            return size

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.task_gui = None

        self.setEditable(True)
        self.lineEdit().setReadOnly(True)

        palette = QApplication.palette()
        palette.setBrush(QPalette.Base, palette.button())
        self.lineEdit().setPalette(palette)
        self.lineEdit().setText("")

        self.setItemDelegate(CheckableComboBox.Delegate())

        self.model().dataChanged.connect(self.updateText)
        self.model().dataChanged.connect(self.on_change_option)




        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

    def set_task_gui(self, task_gui):
        self.task_gui = task_gui

    def on_change_option(self):
        if self.task_gui and self.task_gui.current_Qdate:
            self.task_gui.on_date_clicked(self.task_gui.current_Qdate)

    def eventFilter(self, the_object, event):
        if the_object == self.lineEdit():
            if event.type() == QEvent.MouseButtonRelease:
                if self.closeOnLineEditClick:
                    self.hidePopup()
                else:
                    self.showPopup()
                return True
            return False
        if the_object == self.view().viewport():
            if event.type() == QEvent.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())
                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)
                return True
        return False

    def getOptionIndexByName(self, option_name):
        for row in range(self.model().rowCount()):
            item = self.model().item(row)
            if item is not None and item.text() == option_name:
                return row



    def updateText(self):
        texts = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                texts.append(self.model().item(i).text())
        text = ", ".join(texts)

        # Compute elided text (with "...")
        metrics = QFontMetrics(self.lineEdit().font())
        elided_text = metrics.elidedText(text, Qt.ElideRight, self.lineEdit().width())
        self.lineEdit().setText(elided_text)




    def set_item_checked(self, index, checked=True):
        self.model().item(index).setCheckState(Qt.Checked if checked else Qt.Unchecked)
        self.model().item(index).setData(Qt.Checked if checked else Qt.Unchecked)
        print(self.model().item(index))


    def addItem(self, text, data=None):
        item = QStandardItem()
        item.setText(text)
        if data is None:
            item.setData(text)
        else:
            item.setData(data)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setData(Qt.Checked, Qt.CheckStateRole)
        item.setCheckState(Qt.Checked)

        self.model().appendRow(item)


    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            try:
                data = datalist[i]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def get_current_chosen_options(self):
        options = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                options.append(self.model().item(i))


        return options