from multiprocessing import Manager


def init(l):
    global lock
    lock = l

manager = Manager()
shared_list = manager.list()
shared_list.append(0)
shared_list.append(0)
# shared_list[0] = 0
# shared_list[1] = 0
