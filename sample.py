from queue_module import Queue


q = Queue()


for i in range(3):
    q.addq(i)
    print(q)


print(q.isempty())


for i in range(3):
    q.deq()
    print(q)


print(q.isempty())
