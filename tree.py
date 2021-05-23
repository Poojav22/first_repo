

class Tree:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def print_node(self):
		if self.data:
			print(self.data)
		if self.left:
			print("Printing left of ", self.data)
			self.left.print_node()
		if self.right:
			print("Printing right of", self.data)
			self.right.print_node()

	def insert_node(self, data):
		if data < self.data:
			if self.left == None:
				self.left = Tree(data)
			else:
				self.left.insert_node(data)
		elif data > self.data:
			if self.right == None:
				self.right = Tree(data)
			else:
				self.right.insert_node(data)


if __name__ == "__main__":
	obj = Tree(5)
	obj.print_node()
	obj.insert_node(2)
	print(obj)
	obj.print_node()
	obj.insert_node(3)
	obj.print_node()
	obj.insert_node(6)
	obj.print_node()
