

class Resource():

    def __init__(self, vcpu, disk, ram):
        self.vcpu = 0
        self.disk = 0
        self.ram = 0

    def set_resource(self, vcpu, disk, ram):
        self.vcpu = vcpu
        self.disk = disk
        self.ram = ram