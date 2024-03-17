import random
import time
def if_sorted(list):
    for i in range(len(list)-1):
        if list[i+1]<list[i]:
            return False
    return True
def monkey_sort(list):
    start_time=time.time()
    num = 0
    result = if_sorted(list)
    while not result:
        random.shuffle(list)
        result = if_sorted(list)
        num+=1
        print(f"第{num}次",list)
    end_time = time.time()
    print(f"第{num}次完成,好费时间:{end_time-start_time}",list)

def generate_list(total_num,start_num,end_num):
    """
    :param total_num:
    :param start_num:
    :param end_num:
    :return:
    """
    list_num=[random.randint(start_num,end_num) for i in range(total_num)]
    return list_num
if __name__ == '__main__':
    a = generate_list(1000,1,101)
    monkey_sort(a)


