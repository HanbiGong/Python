#    Main Author(s): Hanbi Gong
#    Main Reviewer(s):




class SortedList:

	class Node:
		def __init__(self, data, next = None, prev = None):
			# pass
			self.data = data
			self.next = None
			self.prev = None

		def get_data(self):
			# pass
			return self.data

		def get_next(self):
			# pass
			return self.next

		def get_previous(self):
			# pass
			return self.prev

	def __init__(self):
		# pass
		self.front = None
		self.back = None

	def get_front(self):
		# pass
		if self.front is None:
			return None
		else:
			return self.front


	def get_back(self):
		# pass
		if self.back is None:
			return None
		else:
			return self.back

	def is_empty(self):
		# pass
		return self.back is None and self.front is None

	def __len__(self):
		# pass
		counter = 0
		curr = self.front
		while curr is not None:
			counter += 1
			curr = curr.next
		return counter

	def insert(self,data):
		# pass
		newNode = self.Node(data)

		if self.front is None:
			self.front = newNode
			self.back = newNode
			return newNode
		
		curr = self.front
		prev = None

		while curr is not None and curr.data < data:
			prev = curr
			curr = curr.next

		if prev is None:
			newNode.next = self.front
			self.front.prev = newNode
			self.front = newNode
		else:
			prev.next = newNode
			newNode.prev = prev
			if curr is not None:
				newNode.next = curr
				curr.prev = newNode
			else:
				self.back = newNode
		return newNode
			
		
	def erase(self,node):
		# pass
		if node is None:
			raise ValueError('Cannot erase node referred to by None')

		if node == self.front:
			self.front = node.next
			if self.front is not None:
				self.front.prev = None
			else:
				self.back = None

		elif node == self.back:
			self.back = node.prev
			if self.back is not None:
				self.back.next = None
			else:
				self.front = None

		else:
			if node.prev is not None:
				node.prev.next = node.next
			if node.next is not None:
				node.next.prev = node.prev

		node.prev = None
		node.next = None
			

	def search(self, data):
		# pass
		curr = self.front
		while curr is not None:
			if curr.data == data:
				return curr
			curr = curr.next
		return None
