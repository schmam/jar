class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError ("too many cookies!")
        self.size += n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError ("invalid operation")
        self.size -= n

    # getter
    @property
    def capacity(self):
        return self.capacity

    # setter
    @property
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError ("invalid capacity")
        self.capacity = capacity

    # getter
    @property
    def size(self):
        return self.size

    # setter
    @property
    def size(self, size):
        self.size = size


def main():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(5)
    print(jar)
