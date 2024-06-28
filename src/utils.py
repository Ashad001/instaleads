from typing import Any
from datetime import datetime
from instagrapi.types import User, Media, UserShort

def convert_to_serializable(obj: Any) -> Any:
        if isinstance(obj, datetime):
            return obj.isoformat()
        # elif isinstance(obj, UserShort):
        #     return {
        #         "id": obj.pk,
        #         "full_name": obj.full_name,
        #         "username": obj.username,
        #     }
        elif isinstance(obj, User) or isinstance(obj, Media) or isinstance(obj, UserShort):
            return obj.dict()
        else:
            print(f"Type {type(obj)} not serializable")
            return str(obj)