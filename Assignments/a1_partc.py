#    Main Author(s): Hanbi Gong
#    Main Reviewer(s):



class Stack:

	def __init__(self, cap=10):
		self.cap = cap
		self.stack = [None] * cap
		self.size = 0

	def capacity(self):
		return self.cap

	def push(self, data):
		if self.size == self.cap:
			new_cap = self.cap * 2
			new_stack = [None] * new_cap
			for i in range(self.size):
				new_stack[i] = self.stack[i]
			self.stack = new_stack
			self.cap = new_cap
		self.stack[self.size] = data
		self.size += 1

	def pop(self):
		if self.is_empty():
			raise IndexError('pop() used on empty stack')
		self.size -= 1
		return self.stack[self.size]

	def get_top(self):
		if self.is_empty():
			return None
		return self.stack[self.size - 1]

	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size


class Queue:


	def __init__(self, cap=10):
		self.cap = cap
		self.queue = [None] * cap
		self.front = 0
		self.rear = 0
		self.size = 0

	def capacity(self):
		return self.cap

	def enqueue(self, data):
		if self.size == self.cap:
			self.cap *= 2
			new_queue = [None] * self.cap
			for i in range(self.size):
				new_queue[i] = self.queue[(self.front + i) % self.size]
			self.queue = new_queue
			self.front = 0
			self.rear = self.size
		self.queue[self.rear] = data
		self.rear = (self.rear + 1) % self.cap
		self.size += 1

	def dequeue(self):
		if self.is_empty():
			raise IndexError('dequeue() used on empty queue')
		data = self.queue[self.front]
		self.front = (self.front + 1) % self.cap
		self.size -= 1
		return data

	def get_front(self):
		if self.is_empty():
			return None
		return self.queue[self.front]


	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size



class Deque:

	def __init__(self, cap=10):
		self.cap = cap
		self.deque = [None] * cap
		self.front = 0
		self.rear = 0
		self.size = 0

	def capacity(self):
		return self.cap

	def push_front(self, data):
		if self.size == self.cap:
			new_cap = self.cap * 2
			new_deque = [None] * new_cap
			for i in range(self.size):
				new_deque[i] = self.deque[(self.front + i) % self.size]
			self.deque = new_deque
			self.front = 0
			self.rear = self.size
			self.cap = new_cap
		self.front = (self.front - 1) % self.cap
		self.deque[self.front] = data
		self.size += 1

	def push_back(self, data):
		if self.size == self.cap:
			new_cap = self.cap * 2
			new_deque = [None] * new_cap
			for i in range(self.size):
				new_deque[i] = self.deque[(self.front + i) % self.size]
			self.deque = new_deque
			self.front = 0
			self.rear = self.size
			self.cap = new_cap
		self.deque[self.rear] = data
		self.rear = (self.rear + 1) % self.cap
		self.size += 1  

	def pop_front(self):
		if self.is_empty():
			raise IndexError('pop_front() used on empty deque')
		data = self.deque[self.front]
		self.front = (self.front + 1) % self.cap
		self.size -= 1
		return data  

	def pop_back(self):
		if self.is_empty():
			raise IndexError('pop_back() used on empty deque')
		self.rear = (self.rear - 1) % self.cap
		data = self.deque[self.rear]
		self.size -= 1
		return data  

	def get_front(self):
		if self.is_empty():
			return None
		return self.deque[self.front]

	def get_back(self):
		if self.is_empty():
			return None
		return self.deque[(self.rear - 1) % self.cap]

	def is_empty(self):
		return self.size == 0

	def __len__(self):
		return self.size

	def __getitem__(self, k):
		if k < 0 or k >= self.size:
			raise IndexError('Index out of range')
		return self.deque[(self.front + k) % self.cap]
