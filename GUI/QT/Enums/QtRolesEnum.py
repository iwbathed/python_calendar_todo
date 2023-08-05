from enum import Enum
from PySide6.QtGui import Qt


class QtRolesEnum(Enum):
    ID = Qt.UserRole + 1
    NAME = Qt.UserRole + 2
    DESCRIPTION = Qt.UserRole + 3
    STATUS = Qt.UserRole + 4
    TAG = Qt.UserRole + 5
    CREATION_DATE = Qt.UserRole + 6
    DEADLINE_DATE = Qt.UserRole + 7
    REPEAT = Qt.UserRole + 8
