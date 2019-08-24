N = int(input())
def isOdd(n):
    if n%2 == 0:
        return False
    return True

if isOdd(N) is True:
    print("Weird")
else:
    if N in range(2,6):
        print("Not Weird")
    if N in range(6,21):
        print("Weird")
    if N not in range(21):
        print("Not Weird")
