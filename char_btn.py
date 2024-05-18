from flet import TextButton, Row, Text, MainAxisAlignment, CrossAxisAlignment, colors


class Char_button():
    def __init__(self, _value:str, _size:int=10, on_click_action=None, font_family:str=None) -> None:
        self.value:str = _value
        self.size:int = _size
        self.button:TextButton = TextButton(content=Text(self.value,size=35, font_family=font_family), width=self.size, height=self.size, on_click=self.set_char)
        self.on_click = on_click_action

    def set_char(self, e):
        if self.button.text == '':
            return
        else:
            self.on_click(self.value)
            self.button.update()            
    
         
class Play_char_button(Char_button):
    def __init__(self, _value: str, _size: int=10, font_family:str=None, on_click_action=None) -> None:
        super().__init__(_value, _size, font_family=font_family, on_click_action=on_click_action)
        
    def set_char(self, e):
        if self.button.text == '':
            return
        else:
            self.on_click(self.value)
            # self.button.text = ''
            self.button.disabled = True
            self.button.update()            
    
    def reset(self):
        self.button.text = self.value
        self.button.disabled = False
        self.button.update()
        
    def block(self):
        self.button.disabled = True
        
class Word_buttons_Row():
    def __init__(self, word:str, page_width:int=1000, font_family:str=None, on_click=None) -> None:
        btn_size = page_width/len(word) - 20
        self.char_button_row = [Play_char_button(char, btn_size, font_family=font_family, on_click_action=on_click) for char in word]
        self.buttons = Row(
            controls=
            [btn.button for btn in self.char_button_row],
            spacing=0,
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER
        )
    
    def restart(self):
        for btn in self.char_button_row:
            btn.reset()
    
    def block(self):
        for btn in self.char_button_row:
            btn.block() 
            
            
