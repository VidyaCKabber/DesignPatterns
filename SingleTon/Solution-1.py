class SingleTon:
    # __new__ dandor method called during object creation process. 
    #__init__method is invoked after the object being created
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    
obj1 = SingleTon()
print(f"Object obj1 {obj1}")
obj1.data = 10

obj2 = SingleTon()
print(f"Object obj2 {obj2}")
print(f"Object obj2.data {obj2.data}")
obj2.data = 5
print(f"Object obj1.data {obj1.data}")
