from threading import Thread
from time import sleep

class Knight(Thread):
    days=0
    enemies=100
    won=False
    def __init__(self, kname, power):
        self.kname=kname
        self.power=power
        super().__init__()
        
    def run(self):
        print(f'{self.kname}, на нас напали!\n')
        while self.won==False:
            sleep(1)
            self.days+=1
            self.enemies=self.enemies-self.power
            print(f'{self.kname} сражается {self.days} дней..., осталось {self.enemies} воинов.\n')
            if self.enemies<=0:
                print(f'{self.kname} одержал победу спустя {self.days} дней(дня)!\n')
                self.won=True

first_knight = Knight('Sir Lancelot', 10) 
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все рыцари одержали победу!')
    
