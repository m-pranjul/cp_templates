#"""
import sys
from math import factorial
input=sys.stdin.readline
mod=int(1e16+1)
inf=float('inf')
alpha=abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
           'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
           'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
yes="YES"
no="NO"
# Acercandose al infinito......................... 
def comding():
    ##START HERE
    
    return

def si(): return input()
def ii(): return int(input())
def tup(): return map(int,input().split())
def ls(): return [x for x in input().split()]
def sls(): return [map(str,input().split())]
def ils(): return [int(x) for x in input().split()]
def ncr(n,r): return factorial(n)//(factorial(r)*factorial(n-r))
def sils(): return sorted([int(x) for x in input().split()])
def ceil(x,y):
    if x%y==0: return x//y
    else: return x//y+1
def ceil(x):
    if x%1:return int(x)+1
    else:return int(x)
def gcd(x, y):
    while y: x, y = y, x % y
    return x
def isPrime(n):
    if (n <= 1) : return False
    if (n <= 3) : return True
    if (n % 2 == 0 or n % 3 == 0) : return False
    i = 5
    while(i*i<=n) : 
        if (n%i==0 or n%(i+2)==0):return False
        i=i + 6
    return True
for __ in range(ii()): comding()
# """