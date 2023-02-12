# isinstancex (version: 2.0.0a)
#
# Copyright 2023. DuelitDev all rights reserved.
#
# This Library is distributed under the MIT License.

import typing
from isinstancex._version import *


def is_tuple(expr) -> bool:
    name = type(expr).__name__
    module = expr.__module__ if "__module__" in dir(expr) else None
    return ((py_ver >= 3.9 and name == "GenericAlias" and module == "builtins")
            or (name == "_GenericAlias" and module == "typing"))


def parse_tuple(expr) -> typing.Tuple:
    if not is_tuple(expr):
        raise ValueError(f"'{type(expr).__name__}' is not Tuple.")
    return expr.__args__


def is_union(expr) -> bool:
    name = type(expr).__name__
    module = expr.__module__ if "__module__" in dir(expr) else None
    return ((py_ver >= 3.10 and name == "UnionType" and module == "types")
            or (name == "_UnionGenericAlias" and module == "typing"))


def parse_union(expr) -> typing.List[type]:
    if not is_union(expr):
        raise ValueError(f"'{type(expr).__name__}' is not Union.")
    return expr.__args__


def is_optional(expr) -> bool:
    if is_union(expr):
        args = parse_union(expr)
        return len(args) == 2 and None in args
    return False


def parse_optional(expr) -> typing.Tuple[typing.Any, None]:
    if not is_optional(expr):
        raise ValueError(f"'{type(expr).__name__}' is not Optional.")
    args: tuple = expr.__args__
    if args.index(None) == 0:
        return tuple(reversed(args))
    return args
