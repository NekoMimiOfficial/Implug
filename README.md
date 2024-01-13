# Implug modularized plugins for python3  

Implug aims to add hot-swappable plugin support to python by treating a python file as a module which has a type of `Plugin`  

-> Plugin structure:  
* Main class  
* initialize() method  

-> Host structure:  
* loader  
* return  

-> Host example:  
```python
from Implug import framework

fw = framework.Loader()
fw.loadall()

loaded = fw._builtin_init_ret

for module in loaded:
    module.run_method
```
* it is recommended to write your own loader as `loadall` is a general loader, you may write your loader using the `load` method or the builtin `_load2plugin`  

-> plugin example:
```python
from Implug import framework

class Module:
    def run_method(self):
        pass

def Initialize() -> None:
    framework.builtin_init(Module())
```
* since the `loadall` calls the Initialize() method you can create a different initializer than `builtin_init()`

# building  
This project is built using `Bob`  
you can find it on my GitHub  

# Links  
All contact links can be found on [my website](http://nekomimi.tilde.team)  
Quick access:  
-> Discord: `nekomimiofficial`  
-> Telegram: `NekoMimiOfficial`  
-> Email: `nekomimi@tilde.team`  
