# isinstancex (version: 2.0.0a)
#
# Copyright 2023. DuelitDev all rights reserved.
#
# This Library is distributed under the MIT License.

import typing
from isinstancex._version import *


def is_union(expr) -> bool:
    name = type(expr).__name__
    module = expr.__module__ if "__module__" in dir(expr) else None
    return ((py_ver >= 3.10 and name == "UnionType" and module == "types") or
            (name == "_UnionGenericAlias" and module == "typing"))


def get_union_args(expr) -> typing.List[type]:
    if not is_union(expr):
        raise ValueError(f"'{type(expr).__name__}' is not Union.")
    return expr.__args__
