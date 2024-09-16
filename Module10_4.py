from threading import Thread
from random import randint
from time import sleep
import queue

class Table:
    guest=None
    def __init__(self,number):
        self.number=number
        
class Guest(Thread):
    def __init__(self,name):
        
        super().__init__()
        self.name=name
        
    def run(self):
        sleep(randint(3,10))

class Cafe:
    queue=queue.Queue()
    free_table=True
    def __init__(self,*tables):
        self.tables=tables
        
    def guest_arrival(self,*guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest=guest
                    guest.start()
                    free_table=True
                    print(f'{guest.name} сел(-а) за стол номер {table.number}.')
                    guest.join()
                    break
                else:
                    free_table=False
                    
            if free_table==False:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
                
    def serving_guests(self):
        while not self.queue.empty() or not self.free_table:
            for table in self.tables:
                if table.guest!= None and table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла).\nСтол номер {table.number} свободен.')
                    table.guest=None
                else:
                    table.guest=self.queue.get()
                    table.guest.start()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.join()

            
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.serving_guests()
