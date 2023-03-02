
class Server:
    _brand = "Dell"
    
    def __init__(self, operating_system, ip):
        self.operating_system = operating_system
        self.ip = ip
        
    def method(self):
        print(self._brand)
        print(self.operating_system)
        print(self.ip)
        return True
        
s1 = Server("Ubuntu","10.0.0.23")
s2 = Server("Debian","10.0.0.15")
s1._brand= "HP"

print(s1.operating_system)
print(s1.ip)
print(s1._brand)

print(s2.method())
#print(s1.method())