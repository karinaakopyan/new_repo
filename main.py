import time
n=int (input("time in seconds: "))
time.gmtime(0)
time_new = time.strftime("%H : %M : %S", time.gmtime(n))
print ("Time in required format: ", time_new)


