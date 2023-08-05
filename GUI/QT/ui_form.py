# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDateEdit,
                               QFrame, QGridLayout, QHBoxLayout, QLabel,
                               QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
                               QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
                               QStatusBar, QTextBrowser, QTextEdit, QVBoxLayout,
                               QWidget)

from GUI.QT.Items.CheckableComboBox import CheckableComboBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1057, 795)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_18 = QGridLayout(self.centralwidget)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_todays_date = QLabel(self.frame_3)
        self.label_todays_date.setObjectName(u"label_todays_date")

        self.gridLayout_15.addWidget(self.label_todays_date, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.calendarWidget = QCalendarWidget(self.frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMaximumSize(QSize(371, 201))

        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.verticalLayout_date_periods = QVBoxLayout()
        self.verticalLayout_date_periods.setObjectName(u"verticalLayout_date_periods")


        self.pushButton_for_all_period = QPushButton(self.frame)
        self.pushButton_for_all_period.setObjectName(u"pushButton_for_all_period")

        self.verticalLayout_date_periods.addWidget(self.pushButton_for_all_period)

        self.horizontalLayout_dateEdit_period = QHBoxLayout()
        self.horizontalLayout_dateEdit_period.setObjectName(u"horizontalLayout_dateEdit_period")
        self.dateEdit_from = QDateEdit(self.frame)
        self.dateEdit_from.setObjectName(u"dateEdit")

        self.horizontalLayout_dateEdit_period.addWidget(self.dateEdit_from)

        self.dateEdit_to = QDateEdit(self.frame)
        self.dateEdit_to.setObjectName(u"dateEdit_2")

        self.pushButton_date_period_ok = QPushButton(self.frame)
        self.pushButton_date_period_ok.setObjectName(u"pushButton_date_period_ok")
        self.horizontalLayout_dateEdit_period.addWidget(self.dateEdit_to)
        self.horizontalLayout_dateEdit_period.addWidget(self.pushButton_date_period_ok)
        self.horizontalLayout_dateEdit_period.addWidget(self.pushButton_for_all_period)


        self.label_period = QLabel()
        self.dateEdit_to.setObjectName(u"label_period")
        self.label_period.setText("Period")
        self.verticalLayout_6.addWidget(self.label_period)
        self.verticalLayout_6.addLayout(self.horizontalLayout_dateEdit_period)

        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalLayout_tasks_filter = QHBoxLayout()
        self.horizontalLayout_tasks_filter.setObjectName(u"horizontalLayout_tasks_filter")
        self.comboBox_tags_view = CheckableComboBox(self.frame)

        self.comboBox_tags_view.addItem("")
        self.comboBox_tags_view.setObjectName(u"comboBox_tags_view")

        self.horizontalLayout_tasks_filter.addWidget(self.comboBox_tags_view)



        self.comboBox_repeat_task_view = CheckableComboBox(self.frame)

        self.comboBox_repeat_task_view.addItem("")
        self.comboBox_repeat_task_view.setObjectName(u"comboBox_repeat_task_view")

        self.horizontalLayout_tasks_filter.addWidget(self.comboBox_repeat_task_view)

        self.comboBox_status_task_view = CheckableComboBox(self.frame)

        self.comboBox_status_task_view.addItem("")
        self.comboBox_status_task_view.setObjectName(u"comboBox_repeat_task_view")

        self.horizontalLayout_tasks_filter.addWidget(self.comboBox_status_task_view)

        self.verticalLayout_2.addLayout(self.horizontalLayout_tasks_filter)

        self.listWidget_tasks = QListWidget(self.frame)
        self.listWidget_tasks.setObjectName(u"listWidget_tasks")

        self.verticalLayout_2.addWidget(self.listWidget_tasks)

        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.gridLayout_11.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget_main = QStackedWidget(self.frame_2)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.page_task_view = QWidget()
        self.page_task_view.setObjectName(u"page_task_view")
        self.gridLayout_7 = QGridLayout(self.page_task_view)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_mark_as_done = QPushButton(self.page_task_view)
        self.pushButton_mark_as_done.setObjectName(u"pushButton_mark_as_done")

        self.horizontalLayout_6.addWidget(self.pushButton_mark_as_done)

        self.pushButton_edit_task = QPushButton(self.page_task_view)
        self.pushButton_edit_task.setObjectName(u"pushButton_edit_task")

        self.horizontalLayout_6.addWidget(self.pushButton_edit_task)

        self.pushButton_delete_task = QPushButton(self.page_task_view)
        self.pushButton_delete_task.setObjectName(u"pushButton_delete_task")

        self.horizontalLayout_6.addWidget(self.pushButton_delete_task)

        self.gridLayout_6.addLayout(self.horizontalLayout_6, 9, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_tag_sign = QLabel(self.page_task_view)
        self.label_tag_sign.setObjectName(u"label_tag_sign")
        self.label_tag_sign.setMinimumSize(QSize(50, 0))
        self.label_tag_sign.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.label_tag_sign)

        self.label_task_tag = QLabel(self.page_task_view)
        self.label_task_tag.setObjectName(u"label_task_tag")

        self.horizontalLayout_7.addWidget(self.label_task_tag)

        self.label_status_sign = QLabel(self.page_task_view)
        self.label_status_sign.setObjectName(u"label_status_sign")
        self.label_status_sign.setMinimumSize(QSize(50, 0))
        self.label_status_sign.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.label_status_sign)

        self.label_task_status = QLabel(self.page_task_view)
        self.label_task_status.setObjectName(u"label_task_status")

        self.horizontalLayout_7.addWidget(self.label_task_status)

        self.gridLayout_6.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_created_sign = QLabel(self.page_task_view)
        self.label_created_sign.setObjectName(u"label_created_sign")
        self.label_created_sign.setMinimumSize(QSize(50, 0))
        self.label_created_sign.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.label_created_sign)

        self.label_task_created_date = QLabel(self.page_task_view)
        self.label_task_created_date.setObjectName(u"label_task_created_date")

        self.horizontalLayout_11.addWidget(self.label_task_created_date)

        self.label_deadline_sign = QLabel(self.page_task_view)
        self.label_deadline_sign.setObjectName(u"label_deadline_sign")
        self.label_deadline_sign.setMinimumSize(QSize(50, 0))
        self.label_deadline_sign.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.label_deadline_sign)

        self.label_task_deadline_date = QLabel(self.page_task_view)
        self.label_task_deadline_date.setObjectName(u"label_task_deadline_date")

        self.horizontalLayout_11.addWidget(self.label_task_deadline_date)

        self.gridLayout_6.addLayout(self.horizontalLayout_11, 2, 0, 1, 1)

        self.textBrowser_task_name = QTextBrowser(self.page_task_view)
        self.textBrowser_task_name.setObjectName(u"textBrowser_task_name")
        self.textBrowser_task_name.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.textBrowser_task_name, 0, 0, 1, 1)

        self.textBrowser_task_dscription = QTextBrowser(self.page_task_view)
        self.textBrowser_task_dscription.setObjectName(u"textBrowser_task_dscription")

        self.gridLayout_6.addWidget(self.textBrowser_task_dscription, 8, 0, 1, 1)

        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 2, 1)

        self.stackedWidget_main.addWidget(self.page_task_view)
        self.page_tag_manage = QWidget()
        self.page_tag_manage.setObjectName(u"page_tag_manage")
        self.gridLayout_4 = QGridLayout(self.page_tag_manage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.listWidget_tags = QListWidget(self.page_tag_manage)
        self.listWidget_tags.setObjectName(u"listWidget_tags")

        self.gridLayout_4.addWidget(self.listWidget_tags, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.page_tag_manage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 150))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget_tag = QStackedWidget(self.frame_5)
        self.stackedWidget_tag.setObjectName(u"stackedWidget_tag")
        self.stackedWidget_tag.setMaximumSize(QSize(16777215, 150))
        self.page_tag_create = QWidget()
        self.page_tag_create.setObjectName(u"page_tag_create")
        self.gridLayout_14 = QGridLayout(self.page_tag_create)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_6 = QFrame(self.page_tag_create)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lineEdit_tag = QLineEdit(self.frame_6)
        self.lineEdit_tag.setObjectName(u"lineEdit_tag")
        self.lineEdit_tag.setMinimumSize(QSize(0, 50))

        self.verticalLayout_4.addWidget(self.lineEdit_tag)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.pushButton_save_tag = QPushButton(self.frame_6)
        self.pushButton_save_tag.setObjectName(u"pushButton_save_tag")

        self.horizontalLayout_12.addWidget(self.pushButton_save_tag)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.gridLayout_13.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.gridLayout_14.addWidget(self.frame_6, 0, 0, 1, 1)

        self.stackedWidget_tag.addWidget(self.page_tag_create)
        self.page_tag_edit = QWidget()
        self.page_tag_edit.setObjectName(u"page_tag_edit")
        self.gridLayout_10 = QGridLayout(self.page_tag_edit)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_7 = QFrame(self.page_tag_edit)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 250))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_old_tag = QLabel(self.frame_7)
        self.label_old_tag.setObjectName(u"label_old_tag")

        self.verticalLayout_3.addWidget(self.label_old_tag)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.lineEdit_tag_edit = QLineEdit(self.frame_7)
        self.lineEdit_tag_edit.setObjectName(u"lineEdit_tag_edit")
        self.lineEdit_tag_edit.setMinimumSize(QSize(0, 0))

        self.verticalLayout_5.addWidget(self.lineEdit_tag_edit)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.pushButton_tag_edit_cancel = QPushButton(self.frame_7)
        self.pushButton_tag_edit_cancel.setObjectName(u"pushButton_tag_edit_cancel")

        self.horizontalLayout_13.addWidget(self.pushButton_tag_edit_cancel)

        self.pushButton_save_edited_tag = QPushButton(self.frame_7)
        self.pushButton_save_edited_tag.setObjectName(u"pushButton_save_edited_tag")

        self.horizontalLayout_13.addWidget(self.pushButton_save_edited_tag)

        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.gridLayout_9.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.gridLayout_10.addWidget(self.frame_7, 0, 0, 1, 1)

        self.stackedWidget_tag.addWidget(self.page_tag_edit)

        self.gridLayout_3.addWidget(self.stackedWidget_tag, 1, 0, 1, 1)

        self.gridLayout_4.addWidget(self.frame_5, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_edit_tag = QPushButton(self.page_tag_manage)
        self.pushButton_edit_tag.setObjectName(u"pushButton_edit_tag")

        self.horizontalLayout_10.addWidget(self.pushButton_edit_tag)

        self.pushButton_delete_tag = QPushButton(self.page_tag_manage)
        self.pushButton_delete_tag.setObjectName(u"pushButton_delete_tag")

        self.horizontalLayout_10.addWidget(self.pushButton_delete_tag)

        self.gridLayout_4.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.stackedWidget_main.addWidget(self.page_tag_manage)
        self.page_task_edit = QWidget()
        self.page_task_edit.setObjectName(u"page_task_edit")
        self.gridLayout_8 = QGridLayout(self.page_task_edit)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit_task_name = QTextEdit(self.page_task_edit)
        self.textEdit_task_name.setObjectName(u"textEdit_task_name")
        self.textEdit_task_name.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.textEdit_task_name)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.comboBox_task_edit_tags = QComboBox(self.page_task_edit)
        self.comboBox_task_edit_tags.addItem("")
        self.comboBox_task_edit_tags.setObjectName(u"comboBox_task_edit_tags")

        self.horizontalLayout_5.addWidget(self.comboBox_task_edit_tags)

        self.comboBox_repeat_task_edit = QComboBox(self.page_task_edit)
        self.comboBox_repeat_task_edit.addItem("")
        self.comboBox_repeat_task_edit.addItem("")
        self.comboBox_repeat_task_edit.addItem("")
        self.comboBox_repeat_task_edit.setObjectName(u"comboBox_repeat_task_edit")

        self.horizontalLayout_5.addWidget(self.comboBox_repeat_task_edit)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.page_task_edit)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.dateEdit_task_edit = QDateEdit(self.page_task_edit)
        self.dateEdit_task_edit.setObjectName(u"dateEdit_task_edit")

        self.horizontalLayout_2.addWidget(self.dateEdit_task_edit)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit_task_description = QTextEdit(self.page_task_edit)
        self.textEdit_task_description.setObjectName(u"textEdit_task_description")

        self.verticalLayout.addWidget(self.textEdit_task_description)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_task_edit_cancel = QPushButton(self.page_task_edit)
        self.pushButton_task_edit_cancel.setObjectName(u"pushButton_task_edit_cancel")

        self.horizontalLayout_8.addWidget(self.pushButton_task_edit_cancel)

        self.pushButton_task_save = QPushButton(self.page_task_edit)
        self.pushButton_task_save.setObjectName(u"pushButton_task_save")

        self.horizontalLayout_8.addWidget(self.pushButton_task_save)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.gridLayout_8.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.stackedWidget_main.addWidget(self.page_task_edit)

        self.gridLayout_5.addWidget(self.stackedWidget_main, 1, 1, 1, 1)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_8)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalSpacer = QSpacerItem(209, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.pushButton_new_task = QPushButton(self.frame_8)
        self.pushButton_new_task.setObjectName(u"pushButton_new_task")

        self.gridLayout_16.addWidget(self.pushButton_new_task, 0, 1, 1, 1)

        self.pushButton_mananege_tags = QPushButton(self.frame_8)
        self.pushButton_mananege_tags.setObjectName(u"pushButton_mananege_tags")

        self.gridLayout_16.addWidget(self.pushButton_mananege_tags, 0, 2, 1, 1)

        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.frame_8, 0, 1, 1, 1)

        self.gridLayout_11.addWidget(self.frame_2, 0, 1, 1, 1)

        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.gridLayout_15.addWidget(self.frame_4, 1, 0, 1, 1)

        self.gridLayout_18.addWidget(self.frame_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget_main.setCurrentIndex(2)
        self.stackedWidget_tag.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_todays_date.setText(QCoreApplication.translate("MainWindow", u"todays date", None))
        self.pushButton_for_all_period.setText(QCoreApplication.translate("MainWindow", u"For all time", None))
        self.pushButton_date_period_ok.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.comboBox_tags_view.setItemText(0, QCoreApplication.translate("MainWindow",
                                                                          u"\u043e\u0431\u0440\u0430\u0442\u0438 \u0442\u0435\u0433",
                                                                          None))

        self.comboBox_repeat_task_view.setItemText(0, QCoreApplication.translate("MainWindow", u"once", None))

        self.pushButton_mark_as_done.setText(QCoreApplication.translate("MainWindow", u"mark as done/undone", None))
        self.pushButton_edit_task.setText(QCoreApplication.translate("MainWindow", u"edit", None))
        self.pushButton_delete_task.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.label_tag_sign.setText(QCoreApplication.translate("MainWindow", u"Tag:", None))
        self.label_task_tag.setText(QCoreApplication.translate("MainWindow", u"the tag", None))
        self.label_status_sign.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.label_task_status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_created_sign.setText(QCoreApplication.translate("MainWindow", u"Created:", None))
        self.label_task_created_date.setText(QCoreApplication.translate("MainWindow", u"15-07-2023", None))
        self.label_deadline_sign.setText(QCoreApplication.translate("MainWindow", u"Deadline:", None))
        self.label_task_deadline_date.setText(QCoreApplication.translate("MainWindow", u"15-07-2023", None))
        self.pushButton_save_tag.setText(QCoreApplication.translate("MainWindow", u"Save tag", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Old tag:", None))
        self.label_old_tag.setText(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.pushButton_tag_edit_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_save_edited_tag.setText(QCoreApplication.translate("MainWindow", u"Save tag", None))
        self.pushButton_edit_tag.setText(QCoreApplication.translate("MainWindow", u"Edit tag", None))
        self.pushButton_delete_tag.setText(QCoreApplication.translate("MainWindow", u"Delete tag", None))
        self.comboBox_task_edit_tags.setItemText(0,
                                                 QCoreApplication.translate("MainWindow", u"\u0442\u0435\u0433", None))

        self.comboBox_repeat_task_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"once", None))
        self.comboBox_repeat_task_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"daily", None))
        self.comboBox_repeat_task_edit.setItemText(2, QCoreApplication.translate("MainWindow", u".....", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Deadline", None))
        self.pushButton_task_edit_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_task_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_new_task.setText(QCoreApplication.translate("MainWindow", u"New task", None))
        self.pushButton_mananege_tags.setText(QCoreApplication.translate("MainWindow", u"Manage tags", None))
    # retranslateUi
