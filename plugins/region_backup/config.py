from mcdreforged.api.utils.serializer import Serializable
from typing import Dict
import os

class rb_info(Serializable):
    time: str = ""
    backup_dimension: str = ""
    user_dimension: str = ""
    user: str = ""
    user_pos: float = ""
    command: str = ""
    comment: str = ""


class rb_config(Serializable):
    backup_path: str = "./rb_multi"
    world_path: str = "./server/world"
    minimum_permission_level: Dict[str, int] = {
        "make": 1,
        "pos_make": 1,
        "back": 2,
        "del": 2,
        "confirm": 1,
        "abort": 1,
        "reload": 2,
        "list": 0
    }
    slot: int = 5


def get_file_size(folder_list):
    total_size = 0
    for directory in folder_list:

        for dirpath, dirnames, filenames in os.walk(directory):

            for filename in filenames:

                file_path = os.path.join(dirpath, filename)
                # 确保文件存在
                if os.path.exists(file_path):
                    total_size += os.path.getsize(file_path)

    return total_size

print(3//2)