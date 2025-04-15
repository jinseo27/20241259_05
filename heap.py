import csv


class Friend:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.birth_value = int(birth)

    def __repr__(self):
        return f"{self.name} ({self.birth})"


class Heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]
        else:
            self.__A = []

    def insert(self, x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A)-1)

    def __percolateUp(self, i: int):
        parent = (i - 1) // 2
        if i > 0 and self.__A[i][0] > self.__A[parent][0]:  
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateUp(parent)

    def deleteMax(self):
        if not self.isEmpty():
            max = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.__percolateDown(0)
            return max
        return None

    def __percolateDown(self, i: int):
        child = 2 * i + 1
        right = 2 * i + 2
        if child <= len(self.__A) - 1:
            if right <= len(self.__A) - 1 and self.__A[child][0] < self.__A[right][0]:
                child = right
            if self.__A[i][0] < self.__A[child][0]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)

    def isEmpty(self):
        return len(self.__A) == 0

heap = Heap()

with open("birthday.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['이름'].strip()
        birth = row['생년월일8자리(예.20040101)'].strip()

        if not birth.isdigit():
            print(f"비어있음: {name} - '{birth}'") 
            continue

        friend = Friend(name, birth)
        heap.insert((friend.birth_value, friend))  



print("생일이 가장 늦은 10명의 친구:")
for _ in range(10):
    if not heap.isEmpty():
        _, friend = heap.deleteMax()
        print(friend)
