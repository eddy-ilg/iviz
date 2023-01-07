#!/usr/bin/env python3

### --------------------------------------------- ###
### Part of iViz                                  ###
### (C) 2022 Eddy ilg (me@eddy-ilg.net)           ###
### Creative Commons                              ###
### Attribution-NonCommercial-NoDerivatives       ###
### 4.0 International License.                    ###
### Commercial use an redistribution prohibited.  ###
### See https://github.com/eddy-ilg/iviz          ###
### --------------------------------------------- ###

import importlib


class Factory:
    def new(self, name, *args, **kwargs):
        class_ = self.classref(name)
        inst = class_(*args, **kwargs)
        return inst

    def classref(self, name):
        parts = name.split('.')
        module_name = 'iviz.' + '.'.join(parts[:-1])
        class_name = parts[-1]
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        return class_


factory = Factory()

def set_factory(f):
    global factory
    factory = f
