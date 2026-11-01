from typing import Optional
def get_nickname(name:str)->Optional[str]:
    if name == "admin":
        return None
    return name
print(get_nickname("admin"))
print(get_nickname("Alice"))