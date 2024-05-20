# logger
from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self.next = None
    @abstractmethod
    def handle(self,Log):
        pass
class Levels:
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    ERROR = 'ERROR'

class Log:
    def __init__(self,s,m):
        self.message = m
        self.severity = s
class InfoHandler(Handler):
    def __init__(self,next):
        self.next = next

    def handle(self,Log):
        if Log.severity == Levels.INFO:
            print(f'Info:{Log.message}')
        else:
            if self.next:
                self.next.handle(Log)


class DebugHandler(Handler):
    def __init__(self, next):
        self.next = next

    def handle(self, Log):
        if Log.severity == Levels.DEBUG:
            print(f'Debug:{Log.message}')
        else:
            if self.next:
                self.next.handle(Log)


class ErrorHandler(Handler):
    def __init__(self, next):
        self.next = next

    def handle(self, Log):
        if Log.severity == Levels.ERROR:
            print(f'Error:{Log.message}')
        else:
            if self.next:
                self.next.handle(Log)

# DEFINING LOGGER
class Main:
    def __init__(self):
        self.logger = InfoHandler(DebugHandler(ErrorHandler(None)))
        self.logger.handle(Log(Levels.ERROR,'this is error msg'))
        self.logger.handle(Log(Levels.DEBUG,'this is debug msg'))
        self.logger.handle(Log(Levels.INFO,'THIS IS INFO MSG'))
Main()
