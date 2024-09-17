import datetime
import multiprocessing

def read_info(name):
    all_data=[]
    with open(name,'r',encoding='utf-8') as file:
        for line in file.readlines():
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

#Многопроцессорный вызов
if __name__ == '__main__':
    time_start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    time_end = datetime.datetime.now()
    time_multi = time_end - time_start
    print(f' Время выполнения при многопроцессорном вызове:{time_multi}')

# Линейный вызов
# time_start = datetime.datetime.now()
# for file in filenames:
#     read_info(file)
# time_end = datetime.datetime.now()
# time_linear = time_end - time_start
# print(f' Время выполнения при линейном вызове:{time_linear}')
