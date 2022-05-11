def countSetBits( n ):
    count = 0
    while n:
        count += 1
        n &= (n-1)
    return count
     

def FlippedCount(a , b):
 
    return countSetBits(a^b)

a = int(input())
b = int(input())
print("Binary conversion of a and b are:",bin(a).replace("0b", ""),bin(b).replace("0b", ""))
print("Number of flips required to convert a to b are:",FlippedCount(a, b))
