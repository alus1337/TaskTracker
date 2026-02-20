from version import get_python_version
from appdirs import user_data_dir

PYTHON_INSTANCE_VERSION = get_python_version()
APP_NAME = "TaskTracker"
APP_AUTHOR = "Alus"
USER_DATA_DIRECTORY = user_data_dir(APP_NAME, APP_AUTHOR)

