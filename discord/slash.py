from __future__ import annotations

import inspect
import traceback
from typing import List, Optional, TypeVar, Dict, Any, TYPE_CHECKING, Union, Type, Literal

from .utils import MISSING
from .enums import ApplicationCommandType
from .interactions import Interaction
from .member import Member
from .user import User
from .abc import GuildChannel
from .channel import DMChannel
from .role import Role

__all__ = ("Command", "Option")

application_option_type_lookup = {
    str: 3,
    int: 4,
    bool: 5,
    Member: 6,
    User: 6,
    GuildChannel: 7,
    DMChannel: 7,
    Role: 8,
    float: 10,
}


def _option_to_dict(option: _OptionData) -> dict:
    origin = getattr(option.type, "__origin__", None)
    arg = option.type

    payload = {"name": option.name, "description": option.description or "none provided", "required": True}

    if origin is Union:
        if arg.__args__[1] is None:  # type: ignore
            payload["required"] = False
            arg = arg.__args__[0]  # type: ignore

        if arg == Union[Member, Role]:
            payload["type"] = 9

    elif origin is Literal:
        values = arg.__args__  # type: ignore
        python_type = type(values[0])
        if all(type(value) == python_type for value in values) and python_type in application_option_type_lookup.keys():
            payload["type"] = application_option_type_lookup[python_type]
            payload["choices"] = [{"name": literal_value, "value": literal_value} for literal_value in values]

    return payload


class CommandMeta(type):
    def __new__(
        mcs,
        classname: str,
        bases: tuple,
        attrs: Dict[str, Any],
        *,
        type: ApplicationCommandType = ApplicationCommandType.slash_command,
        name: str = MISSING,
        description: str = MISSING,
        parent: Command = MISSING
    ):
        attrs["_arguments"] = arguments = []
        attrs["_type"] = type
        attrs["_children"] = []

        if name is not MISSING:
            attrs["_name"] = name
        else:
            attrs["_name"] = classname

        if description:
            attrs["_description"] = description
        elif attrs.get("__doc__") is not None:
            attrs["_description"] = inspect.cleandoc(attrs["__doc__"])
        else:
            attrs["_description"] = MISSING

        attrs["_parent"] = parent

        ann = attrs.get("__annotations__", {})

        for k, v in ann.items():
            attr = attrs.get(k, MISSING)
            default = description = MISSING
            if isinstance(attr, Option):
                default = attr.default
                description = attr.description

            elif attr is not MISSING:
                default = attr

            arguments.append(_OptionData(k, v, description, default))

        t = super().__new__(mcs, classname, bases, attrs)

        if parent is not MISSING:
            parent._children.append(t)  # type: ignore

        return t


class Command(metaclass=CommandMeta):
    if TYPE_CHECKING:
        _arguments: List[_OptionData]
        _name: str
        _type: ApplicationCommandType
        _description: Union[str, MISSING]
        _parent: Optional[Type[Command]]
        _children: List[Type[Command]]
        interaction: Interaction

    @property
    def type(self) -> ApplicationCommandType:
        return self._type

    @classmethod
    def to_dict(cls) -> dict:
        if cls._type is ApplicationCommandType.slash_command and cls._children:
            return {
                "name": cls._name,
                "description": cls._description or "no description",
                "options": [x.to_dict() for x in cls._children],
            }

        options = []
        payload = {
            "name": cls._name,
            "description": cls._description or "no description",
            "type": cls._type.value,
            "options": options,
        }
        for option in cls._arguments:
            options.append(_option_to_dict(option))

        return payload

    async def callback(self) -> None:
        ...

    async def error(self, exception: Exception) -> None:
        traceback.print_exception(type(exception), exception, exception.__traceback__)


T = TypeVar("T")


class Option:
    __slots__ = ("description", "default")

    def __init__(self, description: str = MISSING, *, default: T = MISSING) -> None:
        self.description = description
        self.default = default


class _OptionData:
    __slots__ = ("name", "type", "description", "default")

    def __init__(
        self,
        name: str,
        type_: Type[Any],
        description: Optional[str] = MISSING,
        default: T = MISSING,
    ):
        self.name = name
        self.type = type_
        self.description = description
        self.default = default
