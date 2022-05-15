# pifields
pifields library is used to define fields in a simple way.  
## Install
`pip install pifields`  
## Documentation
[py-fields wiki](https://github.com/DuelitDev/pifields/wiki)  
## Example
```python
from pifields import *


class Human(metaclass=FieldMeta):
    _age = 19
    
    @fields
    def age(self):
        return Human._age

    @age.setter
    def age(self, value):
        Human._age = value


# get
print(Human.age)  # 19

# set
Human.age = 29
print(Human.age)  # 29
```   
## Copyright
Copyright 2022. Kim Jae-yun all rights reserved.  
## License
[MIT License](https://github.com/DuelitDev/pifields/blob/main/LICENSE)   

