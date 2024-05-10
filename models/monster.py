from pydantic import BaseModel, validator

class Monster(BaseModel):
    name: str
    url: str
    cr: str
    _type: str
    size: str
    ac: str
    hp: str
    speed: str
    align: str
    legendary: bool
    source: str
    _str: int
    _dex: int
    _con: int
    _int: int
    _wis: int
    _cha: int

    # TODO: probs overkill, we'll likely never re-upload these
    @validator("legendary", pre=True)
    def legendary_bool(cls, value) -> bool:
        if isinstance(value, str):
            if value == "Legendary":
                return True
            elif value == "":
                return False
            else:
                raise ValueError(f"Unable to convert {value} to bool")
        return value