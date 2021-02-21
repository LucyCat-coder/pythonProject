# class ListOne():
#     def __init__(self):
#
#         self.lst = []
#
#
# def add(self, x):
#
#
#     self.lst.append(x)
#
#
# def delete(self):
#
#
#     self.lst.pop()
#
#
# def show(self):
#
#
#     print(self.lst)
#
#
# def check(self, x):
#
#
#     return x in self.lst
#
#
# def replace(self, x, y):
#
#
#     if x in self.lst:
#         for i in range(len(self.lst)):
#             if self.lst[i] == x:
#             self.lst[i] = y
# lists = ListOne()
# lists.add(8)
# lists.add(9)
# lists.add(5)
# lists.show()
# lists.delete()
# lists.show()
# print(lists.check(8))
# lists.replace(9, 10)
# lists.show()
# ​[Вчера(12: 10)] Лютина
# Екатерина
# Владимировна
#
# lists = ListOne()
# lists.add(8)
# lists.add(9)
# lists.add(5)
# lists.show()
# lists.delete()
# lists.show()
# print(lists.check(8))
# lists.replace(9, 10)
# lists.show()

#
# class Node():
#     def __init__(self, value, nextValue):
#         self.value = value
#         self.nextValue = nextValue
#
#
# class ListLinked():
#     def __init__(self):
#         self.first = None
#         self.last = None
#         self.length = 0
#
#
#     def add(self, x):
#         self.length += 1
#         if self.first == None:
#             self.last = self.first = Node(x, None)
#         else:
#             self.last.nextValue = self.last = Node(x, None)
#
#     def show(self):
#         if self.length != 0:
#             tmp = self.first
#         while tmp.nextValue != None:
#             print(tmp.value, end=', ')
#             tmp = tmp.nextValue
#             print(tmp.value)
#
#     def addStart(self, x):
#         self.length += 1
#         if self.first == None:
#             self.last = self.first = Node(x, None)
#         else:
#             self.first = Node(x, self.first)
#
#     def insert(self, x, index):
#         self.length += 1
#         if self.first == None:
#             self.last = self.first = Node(x, None)
#         return
#         elif index == 0:
#         self.addStart(x)
#         else:
#             tmp = self.first
#             count = 0
#         while tmp != None:
#             tmp = tmp.nextValue
#             count += 1
#         if index == count:
#             tmp.nextValue = Node(x, tmp.nextValue)
#
#
#     def pop(self):  # удаление последнего элемента списка
#
#
#         if self.length != 0:
#             self.length -= 1
#     tmp = self.first
#     while tmp.nextValue.nextValue != None:
#         tmp = tmp.nextValue
#     # print(tmp.value)
#     tmp.nextValue = None
#     self.last = tmp
#
#
#     def popFirst(self):
#
#
        # if self.first != None:
        #     self.length -= 1
#     self.first = self.first.nextValue
#
#
#     def check(self, x):
#
#
#         tmp = self.first
#     while tmp != None:
#         if tmp.value == x:
#             return True
#     tmp = tmp.nextValue
#     return False
# listLink = ListLinked()
# listLink.add(35)
# listLink.add(5)
# listLink.add(3)
# listLink.add(67)
# listLink.add(4)
# listLink.add(23)
# listLink.show()
# listLink.addStart(77)
# listLink.show()
# listLink.insert(86, 2)
# listLink.show()
# listLink.pop()
# listLink.show()
# listLink.popFirst()
# listLink.show()
# print(listLink.check(5))
