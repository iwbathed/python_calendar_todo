import os

from Settings import ID_FILE, PROJECT_FOLDER, TASKS_FOLDER, SERVICE_FOLDER


class Id:
    @staticmethod
    def id_generate():
        id_file_path = os.path.join(PROJECT_FOLDER, SERVICE_FOLDER, ID_FILE)
        if not os.path.exists(os.path.join(PROJECT_FOLDER, SERVICE_FOLDER)):
            os.mkdir(os.path.join(PROJECT_FOLDER, SERVICE_FOLDER))

        if os.path.exists(id_file_path):
            with open(id_file_path, "r") as id_file:
                current_id = id_file.readline()
            current_id = str(int(current_id)+1)
        else:
            current_id = '0'
        with open(id_file_path, "w") as id_file:
            id_file.write(current_id)
        return current_id
