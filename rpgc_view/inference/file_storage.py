import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class TemporaryFileStorage(FileSystemStorage):
    """_summary_

    Args:
        FileSystemStorage (_type_): _description_

    Returns:
        _type_: _description_
    """
    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.TEMP_FILE_UPLOAD_DIR
        super().__init__(*args, **kwargs)

class CustomFileStorage(FileSystemStorage):
    """_summary_

    Args:
        FileSystemStorage (_type_): _description_
    """
    def get_available_name(self, name: str, max_length: int | None = None) -> str:
        if self.exists(name):
            base, extension = os.path.splitext(name)
            counter = 1
            while self.exists(name):
                name = f"{base}_{counter}{extension}"
                counter += 1
        return name
    