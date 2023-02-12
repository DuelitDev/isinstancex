# isinstancex (version: 2.0.0a)
#
# Copyright 2023. DuelitDev all rights reserved.
#
# This Library is distributed under the MIT License.


from isinstancex._version import python_version
if python_version >= 3.7:
    from isinstancex.isinstancex import *
else:
    raise OSError("Python version must be higher or equal to 3.7.")
