# for i in range(1,10):
#     with open("三国演义-%s.txt"%i,"w") as f:
#         f.write("三国演义-%s.txt"%i)


# set=map(lambda x,y:x+y,[1,2,3],[4,5])
# for i in set:
#     print(i)


import functools

def showargs(x,y,a):
    print(a*x+y)


a=functools.partial(showargs,1,2)

a(7)