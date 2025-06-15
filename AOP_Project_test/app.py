class Service:
    def call_Service1(self):
        print("Call Service1...")
        print("Call Service1...")
        print("Call Service1...")
        print("Call Service1...")
        print("Call Service1...")
        return "This is Call Service 1...."

    def call_Service2(self):
        print("Call Service2...")
        print("Call Service2...")
        print("Call Service2...")
        print("Call Service2...")
        print("Call Service2...")
        return "This is Call Service 2...."

service = Service()
print(service.call_Service1())
print(service.call_Service2())
