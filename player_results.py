import json
from player import Player
from config import RESULT_FILE_NAME

class Player_results():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Player_results, cls).__new__(cls)
        return cls.instance
    
    def init(self, _storage_file_name) -> None:
        self.results = {}
        self.storage_file_name = _storage_file_name
        self.get_results()
        
    def results_update(func):
        def wrapper(self, *args, **kwargs):
            func(args, kwargs)
            self.results = dict(sorted(self.results.items(), 
                          key=lambda item: item[1], reverse=True))
        return wrapper
        
    def get_results(self):
        with open(mode='r', file=self.storage_file_name) as f:
            
            self.results = json.load(f)

        
    def set_results(self):
            with open(mode='w', file=self.storage_file_name) as f:
                json.dump(self.results, f)

    def add_result(self, nickname, result):
        if result > -1:
            self.results[nickname] = result
            self.results = dict(sorted(self.results.items(), 
                          key=lambda item: item[1], reverse=True))
            self.set_results()
        
    def get_current_result(self, nickname:str)->int:
        if len(self.results) == 0:
            raise(ValueError)
        return list(self.results.keys()).index(nickname) + 1 # корректировка отсчёта места с единицы
    
    
    def get_all_user_statistic(self, player:Player)->list:
        statistic = []
        num = 1
        if len(self.results.keys()) < 11:
            for key in self.results.keys():
                statistic.append(tuple([num, key, self.results[key]])) 
                num+=1
            return statistic
        for key in list(self.results.keys())[:10]:
            statistic.append(tuple([num, key, self.results[key]])) 
            num += 1
        player_position = self.get_current_result(player.nickname)
        if player_position > 11:
            statistic.append(tuple([None, None, None]))
        if player_position > 10:
            statistic.append(tuple([player_position, player.nickname, self.results[player.nickname]])) 
            
        return statistic
    
    
    def get_top_user_statistic(self, top_num)->list:
        statistic = []

        if len(self.results.keys()) == 0:
            return []
        
        number = top_num if len(self.results.keys()) > top_num else len(self.results.keys())
        num = 1
        for key in list(self.results.keys())[:number]:
            statistic.append(tuple([num, key, self.results[key]])) 
            num+=1
        return statistic
        
        
    def check_unic_nickname(self, nickname):
        return not nickname in self.results.keys()

    def get_top_results(self, quantity):
        return self.results[:quantity]
    
    

    