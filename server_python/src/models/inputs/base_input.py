# -*- coding: utf-8 -*-

class BaseInput(object):
    def __str__(self):
        return str(self.__dict__)
