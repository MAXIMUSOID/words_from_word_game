import asyncio
from datetime import timedelta


class Timer():
    def __init__(self, time_start:int, on_change, end_count) -> None:
        self.on_change = on_change
        self.end_count = end_count
        self.time = time_start
        self.count_accept = False
        pass
    
    async def __timer__(self):
        while self.time >= 0:
            if self.count_accept is False:
                return
            self.on_change()
            await asyncio.sleep(1)
            self.time -= 1
        else:
            self.end_count()
            
    def start(self):
        if self.count_accept:
            return
        self.count_accept = True
        asyncio.run(self.start_count())
        
    def stop(self):
        self.count_accept = False

    async def start_count(self):

        task = asyncio.create_task(self.__timer__())
        await task
        
    def get_time(self):
        time_text = str(timedelta(seconds=self.time))
        if self.time >= 3600:
            return str(timedelta(seconds=self.time))
        if self.time >= 60:
            return str(timedelta(seconds=self.time))[2:]
        else:
            return str(timedelta(seconds=self.time))[5:]
        
def main():    
    tm:Timer    
    def get_time():
        print(tm.get_time())        
        
    def end_count():
        print("Я закончил")
        
    tm = Timer(3605, get_time, end_count)
    tm.start()
if __name__ == '__main__':
    main()