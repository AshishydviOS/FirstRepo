class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SlinkedList:
	def __init__(self):
		self.head = None

	def insertTop(self,value):
		self.temp = Node(value)
		self.temp.next = self.head
		self.head = self.temp

	def insertBottom(self,value):
		self.temp = Node(value)

		if self.head == None:
			self.head = self.temp
			return

		self.current = self.head
		while (self.current.next != None):
			self.current = self.current.next

		self.current.next = self.temp

	def printList(self):
		self.current = self.head
		while (self.current != None):
			print(self.current.data)
			self.current = self.current.next
# -------------------------------------------------------------------------------
# Option1 : Normat Method to create linked List
# -------------------------------------------------------------------------------
list1 = SlinkedList()
list1.insertTop(20)
list1.insertTop(5)
list1.insertTop(10)

# list1.printList()
# print(list1.head.next.data)
# print(list1.head.next.next.data)

# -------------------------------------------------------------------------------
# Option2 : create linked List using method and new node will added at the begining
# -------------------------------------------------------------------------------
list2 = SlinkedList()
list2.head = Node(10)
e2 = Node(20)
e3 = Node(30)

list2.head.next = e2
e2.next = e3

# print("------------")
# list2.printList()

# -------------------------------------------------------------------------------
# Option3 : create linked List using method and new node will added at the end
# -------------------------------------------------------------------------------
list3 = SlinkedList()
list3.insertBottom(10)
list3.insertBottom(20)
list3.insertBottom(30)

print("------------")
list3.printList()



