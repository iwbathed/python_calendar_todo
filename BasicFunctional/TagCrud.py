import json
import os

from Enums.TagEnum import TagEnum
from Enums.TaskEnum import TaskEnum
from BasicFunctional.FileCrud import FileCrud
from Settings import TAGS_FILE_PATH, DEFAULT_TAG_NAME
from Tag import Tag


class TagCrud:
    # @staticmethod
    # def create_tag(tag, tag_name):
    #     tag.set_task_attribute(
    #         **{TagEnum.NAME.value: tag_name},
    #     )

    @staticmethod
    def create_default_tag():
        all_tag_names = TagCrud.get_all_tag_names()
        if DEFAULT_TAG_NAME not in all_tag_names:
            tag = Tag()
            tag.set_tag_attribute(
                **{TagEnum.NAME.value: DEFAULT_TAG_NAME},
                **{TagEnum.USED_IN_FILES.value: []}
            )
            TagCrud.write_tag_to_file(tag.tag)

    @staticmethod
    def write_tag_to_file(tag):
        all_tags = TagCrud.get_all_tags()
        print(tag)
        if not isinstance(tag, list):
            tag = [tag]
        all_tags.extend(tag)
        with open(TAGS_FILE_PATH, "w") as tags_file:
            json.dump(all_tags, tags_file, indent=4)

    @staticmethod
    def rewrite_tags_to_file(tags):
        if not isinstance(tags, list):
            tags = [tags]
        with open(TAGS_FILE_PATH, "w") as tags_file:
            json.dump(tags, tags_file, indent=4)

    @staticmethod
    def get_all_tags():
        if os.path.exists(TAGS_FILE_PATH):
            with open(TAGS_FILE_PATH, "r") as tags_file:
                return json.load(tags_file)
        else:
            return []

    @staticmethod
    def get_all_tag_names():
        all_tags = TagCrud.get_all_tags()
        if all_tags:
            return [tag[TagEnum.NAME.value] for tag in all_tags]
        else:
            return []


    @staticmethod
    def get_tag_by_tag_name(tag_name):
        all_tags = TagCrud.get_all_tags()
        for i in range(len(all_tags)):
            if all_tags[i][TagEnum.NAME.value] == tag_name:
                return all_tags[i]

    @staticmethod
    def update_tag_name(old_tag_name, new_tag_name):
        all_tags = TagCrud.get_all_tags()
        if new_tag_name in [tag[TagEnum.NAME.value] for tag in all_tags]:
            print(f"Tag with name <{new_tag_name}> already exist")
            return

        for i in range(len(all_tags)):
            if all_tags[i][TagEnum.NAME.value] == old_tag_name:
                all_tags[i][TagEnum.NAME.value] = new_tag_name
                for filename in all_tags[i][TagEnum.USED_IN_FILES.value]:
                    tasks_from_file = FileCrud.read_file(filename)
                    for j in range(len(tasks_from_file)):
                        if tasks_from_file[j][TaskEnum.TAG.value] == old_tag_name:
                            tasks_from_file[j][TaskEnum.TAG.value] = new_tag_name

                    FileCrud.create_file(filename, tasks_from_file)

        TagCrud.rewrite_tags_to_file(all_tags)

    @staticmethod
    def get_all_tags_from_tasks_in_file(filename):
        tasks = FileCrud.read_file(filename)
        all_tags = []
        for task in tasks:
            tag = task[TaskEnum.TAG.value]
            if tag not in all_tags:
                all_tags.append(tag)
        return all_tags

    @staticmethod
    def update_tag_used_filenames(tag_name, new_tag_filenames):
        if not isinstance(new_tag_filenames, list):
            new_tag_filenames = [new_tag_filenames]
        all_tags = TagCrud.get_all_tags()
        for i in range(len(all_tags)):
            if all_tags[i][TagEnum.NAME.value] == tag_name:
                all_tags[i][TagEnum.USED_IN_FILES.value] = new_tag_filenames
        TagCrud.rewrite_tags_to_file(all_tags)


    @staticmethod
    def delete_tag_from_file(tag_name):
        all_tags = TagCrud.get_all_tags()
        for i in range(len(all_tags)):
            if all_tags[i][TagEnum.NAME.value] == tag_name:
                all_tags.pop(i)
                break
        TagCrud.rewrite_tags_to_file(all_tags)



    # @staticmethod
    # def write_tags_to_file(tags, mode):
    #     with open(TAGS_FILE_PATH, mode) as tags_file:
    #         for tag in tags:
    #             tags_file.write(tag + "\n")
    #
    #
    # @staticmethod
    # def create_tag(tag_name):
    #
    #     if not os.path.exists(SERVICE_FOLDER_PATH):
    #         os.mkdir(SERVICE_FOLDER_PATH)
    #
    #     if not os.path.exists(TAGS_FILE_PATH):
    #         TagCrud.write_tags_to_file(tag_name, "a")
    #     else:
    #         tags = TagCrud.read_tags()
    #
    #         if tag_name not in tags:
    #             tags.append(tag_name)
    #             TagCrud.write_tags_to_file(tag_name, "a")
    #         else:
    #             print("Already exist")
    #
    # @staticmethod
    # def read_tags():
    #     if os.path.exists(TAGS_FILE_PATH):
    #         with open(TAGS_FILE_PATH, "r") as tags_file:
    #             return tags_file.read().split("\n")[:-1]
    #
    #
    # @staticmethod
    # def delete_tag_from_file(tag_name):
    #     tags = TagCrud.read_tags()
    #     if tag_name in tags:
    #         tags.remove(tag_name)
    #         TagCrud.write_tags_to_file(tags, "w")
    #
    # # all tasks with this tag will be changed
    # @staticmethod
    # def edit_tag(old_tag_name, new_tag_name):
    #     all_tasks = TaskCrud.get_all_task()
    #     for task in all_tasks:
    #         if task[TaskEnum.TAG.value] == old_tag_name:
    #
    #     pass


