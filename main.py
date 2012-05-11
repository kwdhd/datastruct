# -*- coding:UTF-8 -*-
import io
import math

def main():
    print 'main:\n'
    num = -1<<31
    print num
    #find_less()
    e = 'c'
    if e > 'a':
        print 'bigger'
        
    print pow(7,100)
    for i in range(1,120):
        print pow(7,i)

    
    
def find_smallletter():
    def isBig(ch):
        if ch>= 'A' and ch<='Z':
            return True
        else:
            return False
    def isSmall(ch):
        if ch>= 'a' and ch<='z':
            return True
        else:
            return False
        
    fp = open('smallletter.txt','r')
    arr = []
    while fp.readline():
        temp = []
        for i in range(0,len):
            pass
    
def find_less():
    fp = open('find_less.txt')
    
    str = fp.read()
    length = len(str)
    answer = []
    
    for i in range(0,len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            answer.append(str[i])
    print answer
        
if __name__ == "__main__":
    main()
    
    
