
from enum import Enum


class StatusEnum(Enum):
    NOT_DONE = "not done"
    DONE = "done"
    OVERDUE = "overdue"
    DONE_WITH_OVERDUE = "done_with_overdue"

