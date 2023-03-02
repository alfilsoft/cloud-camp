class Server:
    def __init__(self, name, ip, os):
        self.name=name
        self.ip=ip
        self.os=os
        
    def __str__(self):
        return f"{self.name} {self.ip} {self.os}"
        

def get_servers():
    return [
            Server("java-rest-api","10.0.1.10","amazon-linux"),
            Server("python-rest-api","10.0.1.11","debian"),
            Server("nodejs-rest-api","10.0.1.12","ubuntu")
        ]
        
#for server in get_servers():
 #   print(server)