# isinstancex
isinstancex library is used to prevent type errors in a simple way.  
## Install
`pip install isinstancex`  
## Documentation
[isinstancex wiki](https://github.com/DuelitDev/isinstancex/wiki)  
## Example
```python
import isinstancex


obj = "3"


if isinstancex.isinstancex(obj, int):
    print("obj type is int.")
# an int is required (got type str)
```   
## Copyright
Copyright 2023. DuelitDev all rights reserved.  
## License
[MIT License](https://github.com/DuelitDev/isinstancex/blob/main/LICENSE)   

