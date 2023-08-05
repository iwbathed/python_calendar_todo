
from Enums.TagEnum import TagEnum


class Tag:
    def __init__(self):
        self.tag = {
            TagEnum.NAME.value: "Default id",
            TagEnum.USED_IN_FILES.value: [],
        }

    def set_tag_attribute(self, **kwargs):
        for key, value in kwargs.items():
            self.tag[key] = value

    def get_tag_attribute(self, attr):
        return self.tag[attr]
