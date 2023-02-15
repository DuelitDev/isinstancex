# isinstancex (version: 2.0.0a)
#
# Copyright 2023. DuelitDev all rights reserved.
#
# This Library is distributed under the MIT License.

import typing
from isinstancex._version import *

__all__ = ["is_any", "is_tuple", "is_union", "is_optional", "is_dict"]


def is_any(expr) -> bool:
    name, module = type(expr).__name__, expr.__module__
    return ((py_ver >= 3.11 and name == "_AnyMeta" and module == "typing") or
            (name == "_SpecialForm" and module == "typing" and
             getattr(expr, "_name") == "Any"))


def is_union(expr) -> bool:
    name, module = type(expr).__name__, expr.__module__
    return ((py_ver >= 3.10 and name == "UnionType" and module == "types") or
            (name == "_UnionGenericAlias" and module == "typing"))


def is_optional(expr) -> bool:
    name, module = type(expr).__name__, expr.__module__
    return ((py_ver >= 3.10 and name == "UnionType" and module == "types" and
             len(expr.__args__) == 2 and None in expr.__args__) or
            (name == "_UnionGenericAlias" and module == "typing" and
             getattr(expr, "_name") == "Optional"))


def is_tuple(expr) -> bool:
    name, module = type(expr).__name__, expr.__module__
    return ((py_ver >= 3.9 and name == "GenericAlias" and
             module == "builtins" and expr() == ()) or
            (name == "_GenericAlias" and module == "typing" and
             getattr(expr, "_name") == "Tuple"))


def is_list(expr) -> bool:
    name, module = type(expr).__name__, expr.__module__
    return ((py_ver >= 3.9 and name == "GenericAlias" and
             module == "builtins" and expr() == []) or
            (name == "_GenericAlias" and module == "typing" and
             getattr(expr, "_name") == "List"))


def is_dict(expr) -> bool:
    name, module = type(expr).__name__, expr.__module__
    return ((py_ver >= 3.9 and name == "GenericAlias" and
             module == "builtins" and expr() == {}) or
            (name == "_GenericAlias" and module == "typing" and
             getattr(expr, "_name") == "Dict"))


def is_set(expr) -> bool:
    name, module = type(expr).__name__, expr.__module__
    return ((py_ver >= 3.9 and name == "GenericAlias" and
             module == "builtins" and expr() == set()) or
            (name == "_GenericAlias" and module == "typing" and
             getattr(expr, "_name") == "Set"))
