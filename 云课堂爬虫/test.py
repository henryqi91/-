from multiprocessing import Pool
import os,time,random

def task(name):
    print("run task %s" %name)
    for _ in range(2):
        time.sleep(1)
        # print(name)
    print("task %s finished" %name)

if __name__ == '__main__':
    p = Pool(6) #我的电脑是6核
    for i in range(7):
        p.apply_async(task,args=(i,))
    print("waiting...")
    p.close()
    p.join()
    print("done")
    pass