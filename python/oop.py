
class Server:
    _brand = "Dell"
    
    def __init__(self, operating_system, ip):
        self.operating_system = operating_system
        self.ip = ip
        self.programs=[]
        
    def method(self):
        print(self._brand)
        print(self.operating_system)
        print(self.ip)
        return True
    
    def __str__(self):
        return f"The server has the {self.operating_system} SO and the IP: {self.ip} - programs{self.programs}"
        
    def install(self,program):
        self.programs.append(program)
        
        
s1 = Server("Ubuntu","10.0.0.23")
s2 = Server("Debian","10.0.0.15")
s1._brand= "HP"
s1.install("nano")
print(s1.operating_system)
print(s1.ip)
print(s1._brand)
print(s1.programs)

print(s2.method())
#print(s1.description())
#print(s2.description())
#print(s1.method())

print(s1)