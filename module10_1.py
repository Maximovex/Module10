from threading import Thread
from time import sleep
from datetime import datetime

time_start=datetime.now()

def write_words(word_count,file_name):
    with open(file_name,'w',encoding='utf-8') as file:
        for i in range(1,word_count+1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end=datetime.now()

first_thr=Thread(target=write_words,args=(10,'example5.txt'))
sec_thr=Thread(target=write_words,args=(30,'example6.txt'))
third_thr=Thread(target=write_words,args=(200,'example7.txt'))
fourth_thr=Thread(target=write_words,args=(100,'example8.txt'))

first_thr.start()
sec_thr.start()
third_thr.start()
fourth_thr.start()

first_thr.join()
sec_thr.join()
third_thr.join()
fourth_thr.join()

time_thr_end=datetime.now()
time_res=time_end-time_start
time_thr_res=time_thr_end-time_end
print(f'Время записи без использования потоков: {time_res}\nВремя записи с использованием потоков: {time_thr_res}')
