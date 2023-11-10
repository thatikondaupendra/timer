import time
n=int(input("enter time in seconds: "))
while n:
    min=n//60
    sec=n%60
    print("{:2d}:{:2d}".format(min,sec),end="\r")
    time.sleep(1)
    n-=1