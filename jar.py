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
        return self._capacity

    # setter
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError ("invalid capacity")
        self._capacity = capacity

    # getter
    @property
    def size(self):
        return self._size

    # setter
    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(5)
    print(jar)

if __name__ == "__main__":
    main()
