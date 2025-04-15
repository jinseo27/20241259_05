import csv

class BidirectNode:
    def __init__(self, item, prev, next):
        self.item = item
        self.prev = prev
        self.next = next


class Friend:
    def __init__(self, name, birth):  # birth: yyyymmdd 형식
        self.name = name
        self.birth = birth

    def __repr__(self):
        return f"{self.name} ({self.birth})"


same_team = {
    "김수련", "오다현", "주영", "김다연", "김민영", "김여원", "김채린", "조예진",
    "허재희", "김도경", "안소형", "윤서영", "홍지연"
}


class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0

    def append(self, newItem) -> None:
        prev = self.__head.prev
        newNode = BidirectNode(newItem, prev, self.__head)
        prev.next = newNode
        self.__head.prev = newNode
        self.__numItems += 1

    def __iter__(self):
        return CircularDoublyLinkedListIterator(self)

    def getNode(self, i: int) -> BidirectNode:
        curr = self.__head
        for _ in range(i + 1):
            curr = curr.next
        return curr

class CircularDoublyLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next

    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item

    def __iter__(self):
        return self


friend_list = CircularDoublyLinkedList()


with open("C:/Users/2leej/Downloads/DS_Birthdaydata - 시트1.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['이름'].strip()
        birth = row['생년월일8자리(예.20040101)'].strip()

        if not birth.isdigit():
            continue  

        friend = Friend(name, birth)
        friend_list.append(friend)


print("같은 조 친구들의 이름 - 생일:")
for friend in friend_list:
    if friend.name in same_team:
        print(f"{friend.name} - {friend.birth}")
