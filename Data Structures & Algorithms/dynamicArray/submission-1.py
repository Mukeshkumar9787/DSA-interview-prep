class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity;
        self.length = 0;
        self.arr = [];
        for i in range(capacity):
            self.arr.append(0);

    def get(self, i: int) -> int:
        return self.arr[i];

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n;

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize();
        self.arr[self.length] = n;
        self.length += 1;

    def popback(self) -> int:
        self.length -= 1;
        return self.arr[self.length];

    def resize(self) -> None:
        self.capacity *= 2;
        new_arr = [];
        for i in range(self.capacity):
            if i < self.length:
                new_arr.append(self.arr[i]);
            else:
                new_arr.append(0);
        self.arr = new_arr;

    def getSize(self) -> int:
        return self.length;
    
    def getCapacity(self) -> int:
        return self.capacity;