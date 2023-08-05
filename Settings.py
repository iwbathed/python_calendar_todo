import os


PROJECT_FOLDER = os.path.dirname(os.path.realpath(__file__))
SERVICE_FOLDER = "ServiceFiles"
SERVICE_FOLDER_PATH = os.path.join(PROJECT_FOLDER, SERVICE_FOLDER)

TASKS_FOLDER = "tasks"
TASKS_PATH = os.path.join(PROJECT_FOLDER, TASKS_FOLDER)


ID_FILE = "id.txt"

TAGS_FILE = "tags.json"
TAGS_FILE_PATH = os.path.join(PROJECT_FOLDER, SERVICE_FOLDER, TAGS_FILE)

DATE_FORMAT = "%Y-%m-%d"
DATE_EXAMPLE = "2023-01-30"

DEFAULT_TAG_NAME = "Unassigned"



