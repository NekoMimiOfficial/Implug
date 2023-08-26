# Template start
from importlib import import_module
from os.path import isdir
import shutil
import os

"""
     Auto generated by in-built template generator
     Implug plugin system template v1
"""
# Template end

_builtin_init_ret = []

class Plugin:

    @staticmethod
    def Initialize() -> None:
        """Plugin initialization component"""

class Loader:
    def __init__(self) -> None:
        self.ddir = "plugins"

    def _load2plugin(self, module) -> Plugin:
        try:
            shutil.rmtree(f"{self.ddir}__pycache__/")
        except Exception as e:
            print(str(e))
            pass

        plugin = import_module(f"{self.ddir}{module}")
        return plugin #type: ignore

    def load(self, module):
        if not self.ddir.endswith("/"):
            self.ddir += "/"
        
        cwp = self._load2plugin(module)
        cwp.Initialize()

    def loadall(self):
        if not self.ddir.endswith("/"):
            self.ddir += "/"

        ls = os.listdir(self.ddir)
        i = 0
        for val in ls:
            if isdir(f"{self.ddir}{val}"):
                ls.pop(i)

            if val.startswith("_"):
                ls.pop(i)

            if not val.endswith(".py"):
                ls.pop(i)

            i += 1
        
        for plugin in ls:
            cwp = self._load2plugin(f"{self.ddir}{plugin}")
            cwp.Initialize()

def builtin_init(pluginclass):
    _builtin_init_ret.append(pluginclass)
