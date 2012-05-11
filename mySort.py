#-*-coding:UTF-8-*-  
'''
Created on 2012-3-20

@author: Administrator
'''
# Sort.py
import random
import myDatastruct as myds
# 一些排序算法...

# 一些辅助方法
def print_list(alist):
    print '[',
    for i in range(len(alist)):
        print i,':',alist[i],',',
    print ']'

def sum_list(alist):
    res = 0
    for i in alist:
        res += i
    return res

def generate_list(length):
    return [random.randint(0,1000) for i in range(length)]

def check_sort(alist,t = 'a'):
    if t == 'd':
        for i in range(len(alist)-1):
            if alist[i] < alist[i+1]:
                print 'alist[i],alist[i+1]',alist[i],alist[i+1]
                return False
    else:
        for i in range(len(alist)-1):
            if alist[i] > alist[i+1]:
                print 'alist[i],alist[i+1]',alist[i],alist[i+1]
                return False
    return True
'''
def partition(alist,p = 0,q = -1):
    if q == -1:
        q = len(alist) - 1
    x = alist[p]
    i = p
    for j in range(p+1,q+1):
        if alist[j] <= x:
            i += 1
            alist[i],alist[j] = alist[j],alist[i]
    alist[p],alist[i] = alist[i],alist[p]

    return i
'''
# t = 'a' 升序, t = 'd' 降序
# 冒泡法
def bubble_sort(alist,t = 'a'):
    if t == 'd':
        for i in range(len(alist)-1):
            #print 'alist',alist
            for j in range(0,len(alist)-i-1):
                #print 'i,j,alist[j],alist[j+1]',i,j,alist[j],alist[j+1]
                if alist[j] < alist[j+1]:
                    alist[j],alist[j+1] = alist[j+1],alist[j]
    else:
        for i in range(len(alist)-1):
            for j in range(0,len(alist)-i-1):
                if alist[j] > alist[j+1]:
                    alist[j],alist[j+1] = alist[j+1],alist[j]

# 直接插入排序
def insert_sort(alist,t = 'a'):
    if t == 'd':
        for i in range(1,len(alist)):
            #print 'i,alist',i,alist
            for j in range(i-1,-1,-1):
                if alist[j] < alist[j+1]:
                    alist[j],alist[j+1] = alist[j+1],alist[j]
                else:
                    break
    else:
        for i in range(1,len(alist)):
            #print 'i,alist',i,alist
            for j in range(i-1,-1,-1):
                #print 'j,alist[j],alist[j+1]',j,alist[j],alist[j+1]
                if alist[j] > alist[j+1]:
                    alist[j],alist[j+1] = alist[j+1],alist[j]
                else:
                    break
# 选择排序
def select_sort(alist, t = 'a'):
    if t == 'd':
        for i in range(len(alist)-1,0,-1):
            mininum = alist[0]
            miniix = 0
            for j in range(0,i+1):
                if alist[j] < mininum:
                    mininum = alist[j]
                    miniix = j
            alist[i],alist[miniix] = alist[miniix],alist[i]
    else:
        for i in range(len(alist)-1,0,-1):
            maxnum = alist[0]
            maxix = 0
            for j in range(0,i+1):
                if alist[j] > maxnum:
                    maxnum = alist[j]
                    maxix = j
            alist[i],alist[maxix] = alist[maxix],alist[i]

# 希尔排序
# 对间距相同的子序列进行插入排序,直到最后间距为一
def shell_sort(alist, t='a'):
    incremnet = len(alist)>>1
    while incremnet >= 1:
        for i in range(incremnet):
            shell_helper(alist,i,incremnet,t)
        incremnet = incremnet>>1
# 辅助 插入排序函数
def shell_helper(alist,s,delt, t='a'):
    if t == 'd':
        for i in range(s+delt,len(alist),delt):
            for j in range(i,0,-delt):
                if alist[j-delt] < alist[j]:
                    alist[j],alist[j-delt] = alist[j-delt],alist[j]
                else:
                    break
    else:
        for i in range(s+delt,len(alist),delt):
            #print 'alist:',alist
            for j in range(i,0,-delt):    # 从后往前依次
                #print 'i,j,delt,alist[j],alist[j-delt]',i,j,delt,alist[j],alist[j-delt]
                if alist[j-delt] > alist[j]:
                    alist[j],alist[j-delt] = alist[j-delt],alist[j]
                else:
                    break
            

# 堆排序
def heap_sort(alist,t='a'):
    length = len(alist)
    if t == 'd':
        for i in range(length):
            for j in range(0,length-i):
                heap_helper(alist,j,t)
            alist[0],alist[length-i-1] = alist[length-i-1],alist[0]
    else:
        for i in range(length):
            for j in range(0,length-i):
                heap_helper(alist,j,t)
            alist[0],alist[length-i-1] = alist[length-i-1],alist[0]
def heap_helper(alist,ix,t='d'):
    p = parent(ix)
    if t == 'd':
        if p >= 0 and alist[p] > alist[ix]:
            alist[p],alist[ix] = alist[ix],alist[p]
            heap_helper(alist,p,t)
    else:
        if p >= 0 and alist[p] < alist[ix]:
            alist[p],alist[ix] = alist[ix],alist[p]
            heap_helper(alist,p,t)
def parent(ix):
    return (ix-1)//2

# 快速排序
def quick_sort(alist,t='a'):
    parition(alist,0,len(alist)-1,t)
def parition(alist,s,e,t='a'):
    if t == 'd':
        if s < e:
            pivot = select_pivot(alist,s,e)
            temp = alist[pivot]
            alist[pivot],alist[e] = alist[e],alist[pivot]
            left = s
            right = e
            while left < right:
                while alist[left] >= temp and left < right:
                    left += 1
                if alist[left] < temp:
                    alist[right] = alist[left]
                while alist[right] <= temp and left < right:
                    right -= 1
                if alist[right] > temp:
                    alist[left] = alist[right]
            alist[left] = temp
            parition(alist,s,left-1,t)
            parition(alist,left+1,e,t)
    else:
        if s < e:
            pivot = select_pivot(alist,s,e)
            temp = alist[pivot]
            alist[e],alist[pivot] = alist[pivot],alist[e]
            left = s
            right = e
            while left < right:
                while alist[left] <= temp and left < right:
                    left += 1
                if left < right:
                    alist[right] = alist[left]
                while alist[right] >= temp and left < right:
                    right -= 1
                if left < right:
                    alist[left] = alist[right]
            alist[left] = temp
            parition(alist,s,left-1,t)
            parition(alist,left+1,e,t)

def select_pivot(alist,s=0,e=-1):
    if e == -1:
        return random.randint(0,len(alist)-1)
    else:
        return random.randint(s,e)
# 有错...
def part(alist,left,right):
    print 'left,right,alist',left,right,alist
    if left < right:
        ix = select_pivot(alist,left,right)
        temp = alist[ix]
        s = left
        e = right
        while s < e:
            print 'ix',ix
            while alist[s] <= temp and s < e:
                s += 1
            print 's,ix',s,ix
            if s < e:
                print 'move alist[s] to alist[ix]',alist[s],alist[ix]
                alist[ix],alist[s] = alist[s],alist[ix]
                ix = s
                print 'alist',alist
            while alist[e] >= temp and s < e:
                e -= 1
            print 'e,ix',e,ix
            if s < e:
                print 'move alist[e] to alist[ix])',alist[e],alist[ix]
                alist[ix],alist[e] = alist[e],alist[ix]
                ix = e
                print 'alist',alist
        print 'move temp to alist[ix]',temp,ix
        alist[ix] = temp
        print 'alist',alist
        part(alist,left,ix-1)
        part(alist,ix+1,right)

# 基数排序
def bucket_sort(alist,t1='a',t2='l'):
    nlist = split_nlist(alist)
    length = len(nlist[0])
    s = 0
    e = length
    if t1 == 'd':
        pass
    else:
        if t2 == 'm':
            for i in range(1,e):
                bucker_helper(nlist,alist,i,t1)
        else:
            for i in range(e-1,0,-1):
                bucker_helper(nlist,alist,i,t1)
                #print 'nlist',nlist
def bucker_helper(alist,rlist,k,t1='a'):
    for i in range(1,len(alist)):
        temp = alist[i][k]
        for j in range(i,0,-1):
            if temp < alist[j-1][k]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
                rlist[j],rlist[j-1] = rlist[j-1],rlist[j]
            else:
                break
def int_to_list(num,t='l'):
    alist = []
    while num > 0:
        alist.insert(0,num%10)
        num = num /10
    return alist
def split_nlist(alist):
    nlist = []
    maxium = 0
    for n in alist:
        a = int_to_list(n,'m')
        if maxium < len(a):
            maxium = len(a)
        nlist.append(a)
    #print 'nlist',nlist
    for n in nlist:
        count = maxium - len(n)
        #print 'count',count
        for i in range(count):
            n.insert(0,-1)
    for i in range(len(nlist)):
        nlist[i].insert(0,alist[i])    
    return nlist
# 归并排序
def mergesort(alist,p = 0,q = -1):
    if q == -1:
        #print 'q=-1'
        q = len(alist) - 1
    if p >= q:
        #print 'p,q',p,q
        return
    #print 'p,(p+q)/2,(p+q)/2+1,q:',p,(p+q)/2,(p+q)/2+1,q
    mergesort(alist,p,(p+q)/2)
    mergesort(alist,(p+q)/2+1,q)
    #print alist[p:(p+q)/2]
    #print alist[(p+q)/2+1:q]
    merge(alist,p,(p+q)/2,(p+q)/2+1,q)
# 归并
def merge(alist,a,b,c,d):
    left = a    # 左下标,插入到此为止,                其实没有意义
    for i in range(c,d+1):    # 后半部分插入前半部分
        temp = alist[i]
        ix = i - 1        # 从后往前查找
        while ix >= left:    
            if alist[ix] > temp:    # 把比待插入元素大的右移
                alist[ix+1] = alist[ix]
                ix -= 1
            else:
                break
        alist[ix+1] = temp
        left = ix + 1


def main():
    list1 = generate_list(10)
    list2 = generate_list(10)
    '''
    print 'bubble sort:'
    print 'list1:',list1
    bubble_sort(list1)
    print 'list1:',list1
    print check_sort(list1)
    print 'list2:',list2
    bubble_sort(list2,'d')
    print 'list2:',list2
    print check_sort(list2,'d')
    '''
    '''
    print 'insert sort:'
    print 'list1:',list1
    insert_sort(list1)
    print 'list1:',list1
    print check_sort(list1)
    print 'list2:',list2
    insert_sort(list2,'d')
    print 'list2:',list2
    print check_sort(list2,'d')
    '''
    '''
    print 'select sort:'
    print 'list1:',list1
    select_sort(list1)
    print 'list1:',list1
    print check_sort(list1)
    print 'list2:',list2
    select_sort(list2,'d')
    print 'list2:',list2
    print check_sort(list2,'d')
    '''
    '''
    print 'shell sort:'
    print 'list1:',list1
    shell_sort(list1)
    print 'list1:',list1
    print check_sort(list1)
    print 'list2:',list2
    shell_sort(list2,'d')
    print 'list2:',list2
    print check_sort(list2,'d')
    '''
    '''
    print 'heap sort:'
    print 'list1:',list1
    heap_sort(list1)
    print 'list1:',list1
    print check_sort(list1)
    print 'list2:',list2
    heap_sort(list2,'d')
    print 'list2:',list2
    print check_sort(list2,'d')
    '''
    '''
    print 'quick sort:'
    print 'list1:',
    print_list(list1)
    quick_sort(list1)
    print 'list1:',
    print_list(list1)
    print check_sort(list1)
    print ''
    print 'list2:',
    print_list(list2)
    quick_sort(list2,'d')
    print 'list2:',
    print_list(list2)
    print check_sort(list2,'d')
    '''
    '''
    print 'test parition:'
    print 'list1:',
    print_list(list1)
    part(list1,0,len(list1)-1)
    print 'list1:',
    print_list(list1)
    print check_sort(list1)
    print ''
    '''

    #for i in range(0,10,2):
    #    print i
    #for i in range(1,10):
    #    print i
    #print 0//2


    #print int_to_list(1235343)
    '''
    tlist =  generate_list(10)
    print tlist
    split_list = split_nlist(tlist)
    print(split_list)
    bucker_helper(split_list,tlist,1)
    print(split_list)
    print tlist
    '''

    print 'bucket sort:'
    print 'list1:',
    print_list(list1)
    bucket_sort(list1)
    print 'list1:',
    print_list(list1)
    print check_sort(list1)
    print ''
    print 'list2:',
    print_list(list2)
    bucket_sort(list2,'d')
    print 'list2:',
    print_list(list2)
    print check_sort(list2,'d')

    pass

if __name__ == "__main__":
    main()