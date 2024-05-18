from flet import (
    OutlinedButton, 
    InputBorder,
    TextButton,
    Text,
    UserControl, 
    TextField, 
    Column, 
    Row,
    InputFilter, 
    TextCapitalization,
    MainAxisAlignment,
    CrossAxisAlignment,
    ControlEvent,
    colors)
from player import Player
from player_results import Player_results
from config import START_PAGE_FONT


class Start_Window(UserControl):
    def build(self):
        self.player = Player()
        self.player_results = Player_results()
        self.start_btn = TextButton(content=Text("Войти", size=START_PAGE_FONT, color=colors.WHITE60),disabled=True, on_click=self.start_game)
        
        prefix_text = Text(' Ваше имя: ', size=START_PAGE_FONT, color=colors.WHITE60)
        self.nickname_field = Text('', size=START_PAGE_FONT, color=colors.WHITE60)
        self.error_text = Text('', size=START_PAGE_FONT//2, color=colors.RED_400, height=START_PAGE_FONT)
        
        nickname_row = Row(
            controls=[
                prefix_text, self.nickname_field
            ],
            height=50
        )
        nickname_content = Column(
            controls=[
                nickname_row,
                self.error_text
                
            ]
        )
        
        content = Column(
            expand=True,
            controls=[nickname_content, self.start_btn, self.get_btn_keyboard_row('йцукенгшщзхъ', 'ёфывапролджэ', 'ячсмитьбю')],
            alignment=MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
        
        return content
    
    def nickname_unic_check(self, e):
        if len(self.nickname_field.value) == 0:
            self.error_text.value = "\t\t\tИмя не может быть пустым"
            self.start_btn.disabled = True
            
        elif len(self.nickname_field.value) > 12:
            self.error_text.value = "\t\t\tСлишком длинное имя"
            self.start_btn.disabled = True
            
        elif self.player_results.check_unic_nickname(self.nickname_field.value):
            self.start_btn.disabled = False
            self.error_text.value = ''
            
        else:
            self.start_btn.disabled = True
            self.error_text.value = "\t\t\tТакой ник уже есть"
        self.update()
        
    def start_game(self, _):
        self.player.set_player(self.nickname_field.value)
        self.player_results.add_result(self.player.nickname, 0)
        self.page.go("/game_field")
    
    def keyboard_click(self, e:ControlEvent):
        if e.control.data == 'del':
            self.nickname_field.value = self.nickname_field.value[:-1]
        elif len(self.nickname_field.value) > 12:
            return
        else:
            self.nickname_field.value+=e.control.data
        self.nickname_unic_check(e)
        self.update()
        
    
    def get_btn_keyboard_row(self, line_1:str, line_2:str, line_3:str)->Column:
        row_1 = Row(controls=[], alignment=MainAxisAlignment.CENTER, spacing=5)
        row_2 = Row(controls=[], alignment=MainAxisAlignment.CENTER, spacing=5)
        row_3 = Row(controls=[], alignment=MainAxisAlignment.CENTER, spacing=5)
        row_4 = Row(controls=
                    [
                        TextButton(content=Text('____', size=START_PAGE_FONT, color=colors.LIGHT_BLUE_200), width=200, data='_', on_click=self.keyboard_click)
                    ], 
                    alignment=MainAxisAlignment.CENTER)
        for char in line_1.upper():
            row_1.controls.append(TextButton(content=Text(char, size=START_PAGE_FONT, color=colors.LIGHT_BLUE_200), data=char, on_click=self.keyboard_click))
        row_1.controls.append(TextButton(content=Text('стереть', size=START_PAGE_FONT, color=colors.LIGHT_BLUE_200), data='del', on_click=self.keyboard_click))
        for char in line_2.upper():
            row_2.controls.append(TextButton(content=Text(char, size=START_PAGE_FONT, color=colors.LIGHT_BLUE_200), data=char, on_click=self.keyboard_click))
            
        for char in line_3.upper():
            row_3.controls.append(TextButton(content=Text(char, size=START_PAGE_FONT, color=colors.LIGHT_BLUE_200), data=char, on_click=self.keyboard_click))
            
            
        return Column(
            controls=[row_1, row_2, row_3, row_4], 
            alignment=MainAxisAlignment.END,
            horizontal_alignment=CrossAxisAlignment.END
            )