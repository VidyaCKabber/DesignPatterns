# Pattern name - SingleTon(Mono state pattern)

class Borg:
    _shared = {}
    
    def __init__(self):
        self.__dict__ = self._shared
        
class SingleTon(Borg):
    def __init__(self, val):
        Borg.__init__(self) # or super().__init__()
        self.data = val
        self.data1 = "val"
        
obj1 = SingleTon("Vidya")
print(f"Object obj1 {obj1}")

obj2 = SingleTon("Suma")
print(f"Object obj2 {obj2}")
print(f"Object obj2.data {obj2.data}")
obj2.data = "Nilima"
print(f"Object obj1.data {obj1.data}")
print(f"{obj1.__dict__}")