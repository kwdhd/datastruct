#-*-coding:UTF-8-*-  
# datastruct.py
'''
	自定义的各种数据结构
'''
import random
import mySort as mysort

''' helper function '''
def print_data(node):
	print node.data,
def print_stack(data):
	print data,
		
def replace_node(node,tag,new):
	if node == None:
		return
	if tag == 0:
		node.left = new
	elif tag == 1:
		node.right = new
	else:
		node = new
''' Stack '''
class Stack():
	_st = []
	def __init__(self):
		_st = []
		print 'build a stack'
	def size(self):
		return len(self._st)
	def is_empty(self):
		if self.size() == 0:
			return True
		return False
	def push(self,data):
		self._st.append(data)
	def pop(self):
		if not self.is_empty():
			return self._st.pop()
		return None
	def top(self):
		if not self.is_empty():
			return self._st[-1]
		return None
	def show(self,visit=print_stack):
		for e in self._st:
			visit(e)
''' mini Stack '''
class miniStack(Stack):
	def __init__(self):
		Stack.__init__(self)
		pass

	def push(self,data):
		if self.is_empty():
			self._st.append((data,data))
		else:
			mini = self.top()[1]
			if mini > data:
				self._st.append((data,data))
			else:
				self._st.append((data,mini))
	def pop(self):
		if self.is_empty():
			return None
		else:
			return self._st.pop()[0]
			
	def mini(self):
		if self.is_empty():
			return None
		return self.top()[1]
	
''' Queue '''
class Queue():
	'''list尾作 Queue 头'''
	_qu = []
	def __init__(self):
		_qu = []
	def size(self):
		return len(self._qu)
	def is_empty(self):
		if self.size() == 0:
			return True
		return False
	def enqueue(self,data):
		self._qu.append(data)
	def dequeue(self):
		if not self.is_empty():
			return self._qu.pop(0)
		return None	
	def head(self):
		if not self.is_empty():
			return self._qu[-1]
		return None	
	def tail(self):
		if not self.is_empty():
			return self._qu[0]
		return None
	def show(self):
		print self._qu

''' Binary search tree '''
class BNode:
	def __init__(self, data, left=None, right=None):
		self.left = left
		self.right = right
		self.data = data
	def height(self):	# 返回子树的高度,从1开始
		def _get_height(node):
			h = 0
			if node:
				h1,h2 = _get_height(node.left),_get_height(node.right)
				if h1 > h2:
					h = h1 + 1
				else:
					h = h2 + 1
			return h
		return _get_height(self)
	def has_child(self):
		if self.left and self.right:
			return True
		return False
	def one_child(self):
		if self.left and self.right:
			return self
		if self.left:
			return self.left
		if self.right:
			return self.right
	def inorder_pre(self):
		p = self.left
		if p == None:
			return None
		while p.right:
			p = p.right
		return p
	def replace_child(self,tag,new):
		if tag == 0:
			self.left = new
		else:
			self.right = new
	def is_leaf(self):
		if self.left == None and self.right == None:
			return True
		return False		
class BTree:
	def __init__(self, root = None):
		self.root = root
		self.size = 0
	# Recursive travel around the binary tree: pre, in, back
	def recur_traverse(self, visit=print_data, t='pre'):	
		def pre_order(node, visit):
			if node:
				visit(node)
				pre_order(node.left,visit)
				pre_order(node.right,visit)
		def in_order(node, visit):
			if node:
				in_order(node.left,visit)
				visit(node)
				in_order(node.right,visit)
		def back_order(node,visit):
			if node:
				back_order(node.left,visit)
				back_order(node.right,visit)
				visit(node)
		def level_order(node,level,i,visit):
			pass
			
		if t == 'in':
			in_order(self.root,visit)
		elif t == 'back':
			back_order(self.root,visit)
		elif t == 'level':
			level_order(self.root,0,0,visit)
		else:
			pre_order(self.root,visit)
	# Non-recursive travel around the binary tree: pre, in, back
	def nonrecur_traverse(self,visit=print_data,t='pre'):
		def pre_order(node, visit):
			''' 访问结点,右孩子压栈,进入左子树 '''
			p = None
			st = Stack()
			st.push(node)
			while p != None or not st.is_empty():
				if p == None:
					p = st.pop()
				visit(p)
				if p.right != None:
					st.push(p.right)
				p = p.left				
		def in_order(node, visit):
			''' 当前借点不为空 入栈, 为空 访问栈顶  进入右树 '''
			p = node
			st = Stack()
			while p != None or not st.is_empty():
				if p:
					st.push(p)
					p = p.left
				else:
					p = st.pop()
					visit(p)
					p = p.right
					
		def back_order(node,visit):
			p = node
			st = Stack()
			#st.push(node)
			while p != None or not st.is_empty():
				if p:
					# 左树入栈
					st.push((p,1))
					p = p.left
				else:
					p,flag = st.pop()
					if flag == 1 and p.right:
						# 有右树且还未访问
						st.push((p,2))
						p = p.right
					else:
						# 无右树或已访问
						visit(p)
						p = None
		def level_order(node,visit):
			if node == None:
				return 
			p = None
			qu = Queue()
			qu.enqueue(node)
			while not qu.is_empty():
				p = qu.dequeue()
				visit(p)
				if p.left:
					qu.enqueue(p.left)
				if p.right:
					qu.enqueue(p.right)					
		if t == 'in':
			in_order(self.root,visit)
		elif t == 'back':
			back_order(self.root,visit)
		elif t == 'level':
			level_order(self.root,visit)
		else:
			pre_order(self.root,visit)
	# 插入数据		
	def insert(self,data):
		node = BNode(data)
		self.insert_node(node)
	# 插入结点
	def insert_node(self, node):
		'''二叉树为空时'''
		if node == None:
			return
		p = self.root
		# 树为空...
		if p == None:
			self.root = node
			self.size += 1
			return
		# 不为空时...
		while True:
			if p.data < node.data:
				if p.right == None:
					p.right = node
					self.size += 1
					return
				else:
					p = p.right
			if p.data > node.data:
				if p.left == None:
					p.left = node
					self.size += 1
					return
				else:
					p = p.left
			if p.data == node.data:
				# 不允许有重复值
				return
	# 删除某数据
	def del_data(self,data):
		node = BNode(data)
		self.del_node(node)
	# 删除某结点
	def del_node(self,node):
		if self.root == None:
			return 
		q,p = self.root,self.root
		data = node.data
		tag = -1
		while p:
			# tag 记录,p 是 q 的左孩子,还是右孩子
			if p.data > data:
				q,p,tag = p,p.left,0
			elif p.data < data:
				q,p,tag = p,p.right,1
			else:
				break
		''' 没有找到要删除的结点 '''
		if p == None:
			return 
		if p == q:
			# p 为根节点
			if p.has_child():
				# 如果只有一个子节点
				child = p.one_child()
				if child != p:
					replace_node(self.root,tag,child)
				else:
					# p 有两子女,选择中序遍历前驱代替p
					pre = p.inorder_pre()
					replace_node(self.root,tag,pre)
			else: # p 是叶节点
				replace_node(self.root,tag,None)
		else:
			if p.has_child():
				# 如果只有一个子节点
				child = p.one_child()
				if child != p:
					q.replace_child(tag,child)
				else:
					# p 有两子女,选择中序遍历前驱代替p
					pre = p.inorder_pre()
					q.replace_child(tag,pre)
			else: # p 是叶节点
				q.replace_child(p,None)
		self.size -= 1
	# 查找
	def find(self,data):
		if self.root == None:
			return False
		p = self.root
		while p:
			#print 'p.data',p.data
			if p.data > data:
				p = p.left
			elif p.data < data:
				p = p.right
			else:
				return p
		return None
	def mini_node(self):
		if self.root == None:
			return None
		p = self.root
		while p.left:
			p = p.left
		return p
	def max_node(self):
		if self.root == None:
			return None
		p = self.root
		while p.right:
			p = p.right
		return p
	def get_height(self):
		return self.root.height()
	# 验证各种操作后还是不是二叉搜索树
	def is_btree(self):
		def __is_btree(node):
			if node.left and node.left.data >= node.data:
				return False
			if node.right and node.right.data <= node.data:
				return False
			return True
		if self.root == None:
			return False
		return __is_btree(self.root)
# find distance between two node.
def GetDistance(bnode,pa,pb,flagA,flagB,level,distance):
	p = -1
	if bnode == pa:
		flagA[0] = level
		p = 1
	elif bnode == pb:
		flagB[0] = level
		p =2
	if bnode.left != None:
		l = GetDistance(bnode.left,pa,pb,flagA,flagB,level+1,distance)
	else:
		l = -1
	if bnode.right != None:
		r = GetDistance(bnode.right,pa,pb,flagA,flagB,level+1,distance)
	else:
		r = -1
	# 已完成
	if l == 0 or r == 0:
		return 0
	# 左右都没找到
	elif l+r+p == -3:
		return -1
	# bnode 为公共祖先,计算距离
	elif l+p+r == 2:
		print 'cflagA[0],flagB[0],level',flagA[0],flagB[0],level
		distance[0] = flagA[0] + flagB[0] - level*2
		return 0
	elif l != -1 and r == -1:
		return l
	elif r != -1 and l == -1:
		return r
	else:
		return p
# find Max Distance in bstree
def MaxDistance(bstree):
	if bstree == None or bstree.root == None:
		return None
	p = bstree.root
	while p.left :
		p = p.left
	maxx,p = p.data,bstree.root
	while p.right:
		p = p.right
	mini = p.data
	pa = bstree.find(mini)
	pb = bstree.find(maxx)
	flagA,flagB,Distance = [0],[0],[0]
	GetDistance(bstree,pa,pb,flagA,flagB,1,Distance)
	
def test_MaxDistance():
	alist = [8,6,5,7,10,9,11]
	#alist.sort()
	#alist = [18, 9, 3, 6, 4, 11, 7, 7, 16, 0]
	#alist = [random.randint(0,20) for i in range(0,10)]
	print alist
	mini = min(alist)
	maxx = max(alist)
	bt = BTree()
	for e in alist:
		bt.insert(e)
	bt.nonrecur_traverse(t='in')
	print ''
	flagA = [0]
	flagB = [0]
	distance = [0]
	pa = bt.find(mini)
	pb = bt.find(maxx)
	print 'pa',pa.data
	print 'pb',pb.data

	res = GetDistance(bt.root,pa,pb,flagA,flagB,1,distance)
	print res,distance
	
		

''' RedBlackTree '''
class RBNode():
	def __init__(self,data,parent=None,color='red'):#插入的结点为红
		self.data = data
		self.color = color
		self.left = None
		self.right = None
		self.parent = parent
class RBTree():
	def __init__(self,root=None):
		if root:
			self.root = root
			self.size = 1
		else:
			self.root = None
			self.size = 0
	def insert(self,data):
		node = RBNode(data)
		self.insert_node(node)
	def insert_node(self,node):
		pass
''' AVL Tree '''
class AVLNode():
	# 左边为负,右边为正
	def __init__(self,data=None):
		self.data = data
		self.left = None
		self.right = None
		self.weight = 0
		self.parent = None
		
	def LL_rotate(self):
		if node.parent == self.root:
			self.root = node
			node.right = node.parent
			node.parent.left = None
			self.parent = None
		else:
			parent = self.parent
			self.parent = parent.parent
			self.parent.left = self
			parent.left = None
			parent.parent = self
			self.right = parent
		node.weight = 0
		node.parent.weight = 0

	def LR_rotate(self):
		# 先转换成LL型
		node.parent.left = node.right
		node.parent = node.right
		
		node.right.parent = node.parent
		node.right.left = node

		node.right = None
		
		self.LLrotate(node.parent)	

		
	def RR_rotate(self):
		if node.parent == self.root:
			self.root = node	
		else:
			pass
		right = node.right
		node.weight = 0
		node.parent.weight = 0
		
		right.parent = node.parent
		right.left = node
		node.parent = right
		node.right = right.left
		right.left.parent = node

	def RL_rotate(self):
		# 转换成 RR
		
		node.left.parent = node.parent
		node.left.right = node
		
		node.parent.right = node.left
		
		node.parent = node.left
		node.left = None
		
		self.RRrotate(node.parent)
		
	def insert(self,node):
		# 插入左树
		if self.data > node.data:
			if self.left == None:
				self.left = node
				node.parent = self
			elif self.left.insert(node)	== 0:
				return 0
			# 检查
			if self.weight == -1:
				if self.left.weight < 0:
					self.LL_rotation()
				else:
					self.LR_rotation()
				return 0
			
			self.weight -= 1
			return self.weight
		# 插入右树
		elif self.data < node.data:
			if self.right == None:
				self.right = node
				node.parent = self
			elif self.right.insert(node) == 0:
				return 0
			
			if self.weight == 1:
				if self.right.weight > 0:
					self.RR_roation()
				else:
					self.RL_rotate()
				return 0
			self.weight += 1
			return self.weight
		# 不允许重复
		else:
			return 0
		
		
class AVLTree():
	def __init__(self,root=None):
		self.root = root
		self.size = 0
	

	def insert(self,data):
		self.insert_node(AVLNode(data))

	def insert_node(self,node):

		#=======================================================================
		# if node == None:
		#	return
		# p = self.root
		# data = node.data
		# # 树为空
		# if p == None:
		#	self.root = node
		#	p = node
		#	self.size += 1
		#	return 
		# while True:
		#	print 'p.data,node.data',p.data,data
		#	if p.data > data:
		#		if p.left:
		#			p = p.left
		#		else:
		#			p.left = node
		#			node.parent = p
		#			p.weight -= 1
		#			break
		#	elif p.data < data:
		#		if p.right:
		#			p = p.right
		#		else:
		#			p.right = node
		#			node.parent = p
		#			p.weight += 1
		#			break
		#	else:
		#		return	# 不允许重复值
		# # 检查...
		# parent = p.parent
		# if parent:
		#	print 'p.data,p.weight',p.data,p.weight
		#	if p.weight == -1:
		#		if parent.weight == -1 and parent.left == p:
		#			self.LLrotate(p)
		#		if parent.weight == 1 and parent.right == p:
		#			self.RLrotate(p)
		#	if p.weight == 1:
		#		if parent.weight == 1 and parent.left == p:
		#			self.RRrotate(p)
		#		if parent.weight == -1 and parent.right == p:
		#			self.LRrotate(p)
		# self.size += 1
		#=======================================================================
		pass
		
	# Recursive travel around the binary tree: pre, in, back
	def recur_traverse(self, visit=print_data, t='pre'):	
		def pre_order(node, visit):
			if node:
				visit(node)
				pre_order(node.left,visit)
				pre_order(node.right,visit)
		def in_order(node, visit):
			if node:
				in_order(node.left,visit)
				visit(node)
				in_order(node.right,visit)
		def back_order(node,visit):
			if node:
				back_order(node.left,visit)
				back_order(node.right,visit)
				visit(node)
		def level_order(node,level,i,visit):
			pass		
		if t == 'in':
			in_order(self.root,visit)
		elif t == 'back':
			back_order(self.root,visit)
		elif t == 'level':
			level_order(self.root,0,0,visit)
		else:
			pre_order(self.root,visit)
	
	# Non-recursive travel around the binary tree: pre, in, back
	def nonrecur_traverse(self,visit=print_data,t='pre'):
		def pre_order(node, visit):
			''' 访问结点,右孩子压栈,进入左子树 '''
			p = None
			st = Stack()
			st.push(node)
			while p != None or not st.is_empty():
				if p == None:
					p = st.pop()
				visit(p)
				if p.right != None:
					st.push(p.right)
				p = p.left				
		def in_order(node, visit):
			''' 当前借点不为空 入栈, 为空 访问栈顶  进入右树 '''
			p = node
			st = Stack()
			while p != None or not st.is_empty():
				if p:
					st.push(p)
					p = p.left
				else:
					p = st.pop()
					visit(p)
					p = p.right
					
		def back_order(node,visit):
			p = node
			st = Stack()
			#st.push(node)
			while p != None or not st.is_empty():
				if p:
					# 左树入栈
					st.push((p,1))
					p = p.left
				else:
					p,flag = st.pop()
					if flag == 1 and p.right:
						# 有右树且还未访问
						st.push((p,2))
						p = p.right
					else:
						# 无右树或已访问
						visit(p)
						p = None
		def level_order(node,visit):
			if node == None:
				return 
			p = None
			qu = Queue()
			qu.enqueue(node)
			while not qu.is_empty():
				p = qu.dequeue()
				visit(p)
				if p.left:
					qu.enqueue(p.left)
				if p.right:
					qu.enqueue(p.right)					
		if t == 'in':
			in_order(self.root,visit)
		elif t == 'back':
			back_order(self.root,visit)
		elif t == 'level':
			level_order(self.root,visit)
		else:
			pre_order(self.root,visit)

'''Graph'''
class Graph(dict):
	def __init__(self, vs=[], es=[]):
		for v in vs:
			self.add_vertex(v)
		for e in es:
			self.add_edge(e)
	
	def add_vertex(self,v):
		self[v] = {}
	
	def add_edge(self,e):
		v,w = e
		'''如果v,e没有先添加到Graph中会出错,应该先添加vertex'''
		if not self.has_key(v):
			self[v] = {}
		if not self.has_key(w):
			self[w] = {}
		self[v][w] = e
		e1 = Edge(e[1],e[0])
		self[w][v] = e1

	def get_edge(self,vs):
		return self.setdefault(vs[0],dict()).setdefault(vs[1],None)

	def del_edge(self,e):
		if self.has_key(e[0]):
			if self.has_key(e[1]):
				del self[e[0]][e[1]]
				del self[e[1]][e[0]]

	def del_vertex(self,vs):
		for v in vs:
			if self.has_key(v):
				del self[v]

	def print_class(self):
		print 'print class'
		for k in Graph.__dict__ :
			print k
	
	def vertices(self):
		return [i for i in self]
	
	def edges(self):
		res = []
		for v in self:
			for w in self[v]:
				#print 'v,w',v,w
				res.append(self[v][w])
		return res

	def out_edges(self, v):
		res = [] 
		if not self.has_key(v):
			print 'graph do not have ',v
		for w in self:
			if self[v].has_key(w):
				res.append(self[v][w])
		return res

	def add_all_edges(self):
		for v in self:
			for w in self:
				if v != w:
					e = Edge(v,w)
					self[v][w] = e

class Vertex(object):
	def __init__(self, label=''):
		self.label = label
	
	def __repr__(self):
		return 'V(%s)' % repr(self.label)
	
	__str__ = __repr__

class Edge(tuple):
	def __new__(cls, *vs):
		return tuple.__new__(cls,vs)

	def __repr__(self):
		return 'E(%s,%s)' % (repr(self[0]), repr(self[1]))
	
	__str__ = __repr__


''' HashTable '''
class HashTable():
	def __init__(self):
		pass
''' Test functions '''
def test_stack():
	round = 5
	size = 20   # stack size
	s,e = 0,99    # num Range 
	st = Stack()
	temp = []
	for i in range(round):	# 测5次
		right = True
		temp[:] = []
		print 'round: ',i+1
		print 'test push()'
		for j in range(size):
			num = random.randint(s,e)
			st.push(num)
			temp.append(num)
		for j in range(size):
			if st._st[j] != temp[j]:
				print 'error:i,st._st[j] != temp[size-j-1]',i,st._st[j],temp[j]
				right = False
		print temp
		st.show()
		if right:
			print 'push right'
		print 'test pop()'
		for j in range(20):
			num = st.pop()
			print num,
			if num != temp[size-j-1]:
				print 'error: j,num != temp[size-j-1]',j,num,temp[size-j-1]
				right = False
		print ''
		if right:
			print 'pop right'
		print ''
		print ''
		print ''

def test_queue():
	round = 5
	size = 20   # stack size
	s,e = 0,99    # num Range 
	qu = Queue()
	temp = []
	for i in range(round):
		print 'round:',i+1
		temp[:] = []
		right = True
		
		print 'test enqueue:'
		for j in range(size):
			num = random.randint(0,99)
			temp.append(num)
			qu.enqueue(num)
		for j in range(size):
			if qu._qu[j] != temp[j]:
				print 'error: j,qu._qu[j] != temp[j]',j,qu._qu[j],temp[j]
				right = False

		print 'temp:',temp
		qu.show()
		if right:
			print 'enqueue right!'
		
		print 'test dequeue'
		right = True
		for j in range(size):
			num = qu.dequeue()
			print num,
			if num != temp[j]:
				print 'error: j,num != temp[j]',j,num,temp[j]
				right = False
		print 'dequeue right'
		print ''
		print ''
		print ''

def test_btree():
	bt = BTree()
	nlist = [81,92, 44 ,39, 51, 72, 72, 8 ,82, 2]
	print 'build BTree'
	for i in range(10):
		t = random.randint(0,100)
		#t = nlist[i]
		#print t,
		if i == 5:
			d = t
		bt.insert(t)
	print ''
	print 'rcursive pre_order:'
	bt.recur_traverse()
	print 'non-rcursive pre_order:'
	bt.nonrecur_traverse()
	print 'rcursive in_order:'
	bt.recur_traverse(t='in')
	print 'non-rcursive in_order:'
	bt.nonrecur_traverse(t='in')
	print 'rcursive back_order:'
	bt.recur_traverse(t='back')
	print 'non-rcursive back_order:'
	bt.nonrecur_traverse(t='back')	
	print 'non-rcursive level_order:'
	bt.nonrecur_traverse(t='level')
	print 'test del:'
	print 'del 81'
	bt.del_data(81)
	print 'non-rcursive pre_order:'
	bt.nonrecur_traverse()
	print 'del 2'
	bt.del_data(2)
	print 'non-rcursive pre_order:'
	bt.nonrecur_traverse()
	print 'del 92'
	bt.del_data(92)
	print 'non-rcursive pre_order:'
	bt.nonrecur_traverse()

def test_avltree():
	avltree = AVLTree()
	nlist = [81,92, 44 ,39, 51, 72, 72, 8 ,82, 2]
	print 'build AVLTree'
	for i in range(10):
		t = random.randint(0,100)
		#t = nlist[i]
		#print t,
		if i == 5:
			d = t
		avltree.insert(t)
		print 'insert ',t
		avltree.nonrecur_traverse(t='pre')
		print ''
		
	print ''
	print 'rcursive pre_order:'
	avltree.recur_traverse()
	print 'non-rcursive pre_order:'
	avltree.nonrecur_traverse()
	print 'rcursive in_order:'
	avltree.recur_traverse(t='in')
	print 'non-rcursive in_order:'
	avltree.nonrecur_traverse(t='in')
	print 'rcursive back_order:'
	avltree.recur_traverse(t='back')
	print 'non-rcursive back_order:'
	avltree.nonrecur_traverse(t='back')	
	print 'non-rcursive level_order:'
	avltree.nonrecur_traverse(t='level')

def main():
	''' Stack'''
	#test_stack()
	''' Queue '''
	#test_queue()
	''' BinTree '''
	#test_btree()
	''' AVLTree '''
	#test_avltree()
	
	''' Graph
	v = Vertex('v')
	w = Vertex('w')
	v1 = Vertex('v1')
	w1 = Vertex('w1')
	e = Edge(v,w)
	e1 = Edge(v1,w1)
	print e
	g = Graph([v,w],[e])
	print g
	#print  g.get_edge([v,w])[1]
	#print 'del edge:'
	#g.del_edge(e)
	print g
	g.add_edge(e1)

	print g
	print 'edges:'
	print g.edges()
	print g.out_edges(v)
	g.add_all_edges()
	print g.edges()
	#print g
	'''
	test_MaxDistance()
	pass

if __name__ == "__main__":
    main()