#-*-coding:UTF-8-*-  
'''
Created on 2012-3-23

@author: Administrator
'''
import myDatastruct as myds
import mySort as mysort
import random
# 二叉树转双链表
def BTreeToDLinklist(btree):
    head = []
    def _convert(node,head,pre):
        if node.left:
            pre = _convert(node.left,head,pre)
            pre.right = node
            node.left = pre
        else:
            if pre == None:
                head.append(node)
                pre = node
            else:
                pre.right = node
                node.left = pre
        #
        if node.right:
            next = _convert(node.right,head,node)
            return next
        else:
            return node
        # 返回中序最后一个
    tail = _convert(btree.root,head,None)
    head[0].left = tail
    tail.right = head[0]
    return head[0]

def test_BTreeToDLinkList():
    def print_DLinkList(head):
        p = head
        while p:
            print 'head.data,head.left.data,head.right.data',p.data,p.left.data,p.right.data
            p = p.right
            if p == head:
                break
    #alist = [10,6,4,14,12,16]
    alist = [random.randint(0,99) for i in range(10)]
    bt = myds.BTree()
    for e in alist:
        bt.insert(e)
    bt.nonrecur_traverse(t='in')
    head = BTreeToDLinklist(bt)
    
    #print head.data
    print_DLinkList(head)
    
# mini stack
def test_miniStack():
    mstack = myds.miniStack()
    for i in range(10):
        mstack.push(random.randint(0,99))
        mstack.show()
    print ''
    for i in range(10):
        print mstack.pop(),mstack.mini()
        mstack.show()   

# max sum, 有正有负
def maxsum(alist):
    # 当和为负数,跳到下一个重新开始累积
    if len(alist) == 0:
        return None
    max = alist[0]
    sum = 0
    i = 0
    while i < len(alist):
        sum += alist[i]
        if sum > 0:
            if sum > max:
                max = sum
        else:
            i,j = i+1,i+1
            sum = 0
            continue
        i += 1
    return max
def test_maxsum():
    alist = [1,-2,3,10,-4,7,2,-5]
    print alist
    print maxsum(alist)
    for i in range(5):
        alist[:] = []
        for j in range(10):
            alist.append(random.randint(-10,10))
        print alist
        print maxsum(alist)
    alist = [random.randint(-20,0) for i in range(10)]
    alist.append(0)
    print alist
    print maxsum(alist)

# find path
def findsumpath(btree,val):
    # 后续遍历,如果是叶节点 检查和
    def _print(node):
        print node[0].data,',',
    node = btree.root
    if btree.root == None:
        return
    st = myds.Stack()
    sum = 0
    while node or not st.is_empty():
        if node:
            sum += node.data
            st.push((node,0))
            if node.left:
                node = node.left
            else:
                node = None
        else:
            node,tag = st.pop() # 没有左节点,或左节点已访问            
            # node 是叶节点
            if node.is_leaf():
                if sum == val:
                    print 'sum(',
                    st.show(visit=_print)
                    print node.data,
                    print ')=',val
                else:
                    print 'not find,sum:',sum
                sum -= node.data   
                node = None
            # node 的 右孩子还未访问
            elif tag == 0 and node.right:
                st.push((node,1))
                node = node.right
            # node 的 右孩子已访问
            else: 
                sum -= node.data
                node = None
                         
def test_findsumpath():
    alist = [10,5,4,7,12]
    bt = myds.BTree()
    for e in alist:
        bt.insert(e)
    bt.nonrecur_traverse()
    findsumpath(bt,22)

# 排数
# 有点问题...?
def perm_nums():
    nlist = [0 for i in range(10)]
    result = []
    count = [0]
    def _check(nlist,count):
        count[0] += 1
        for i in range(len(nlist)):
            #print 'nlist.count(i),nlist[i]',nlist.count(i),nlist[i]
            if nlist.count(i) != nlist[i]:
                return False
        return True
                
    def _perm_nums(nlist,num,leave,res,count):
        if num == 10:
            if leave == 0:
                if _check(nlist,count):
                    print 'findx',nlist
                    res.append(nlist)
            return
        else:
            if leave < 0:
                return
        for i in range(0,leave+1):
            nlist[num] = i
            _perm_nums(nlist,num+1,leave-i,res,count)
    _perm_nums(nlist,0,10,result,count)
    print 'find:'
    print result
    print 'count',count[0]
    #for e in res:
    #    print e
    #nlist = [6,2,1,0,0,0,1,0,0,0]
    #nlist = [10,0,0,0,0,0,0,0,0]
    #print _check(nlist)                   
# 

# 判断链表相交

def main():
    #test_BTreeToDLinkList()
    #test_miniStack()
    #test_maxsum()
    #test_findsumpath()
    perm_nums()
    pass

if __name__ == "__main__":
    main()