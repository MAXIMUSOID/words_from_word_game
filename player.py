class Player():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Player, cls).__new__(cls)
        return cls.instance
    
    def set_player(self, _nickname):
        self.nickname = _nickname
        self.value = 0
    

        
        
        
    