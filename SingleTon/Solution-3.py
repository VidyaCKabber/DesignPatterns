class SingletonDecorator(object):
    def __init__(self, kclass):
        self.kclass = kclass
        self.instance = None
        
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.kclass( *args, **kwargs)
        return self.instance
    
@SingletonDecorator
class Logger(object):
    def __init__(self):
        self.start = None
        
    def write(self, msg):
        if self.start:
            print(self.start, msg)
        else:
            print(msg)
        
logger1 = Logger()
logger1.start = "# >"
print("Logger 1", logger1)
logger1.write("Logger1 object is created.")

logger2 = Logger()
logger2.start = "$ >"
print("Logger 2", logger2)
logger1.write("Logger2 object is created.")
