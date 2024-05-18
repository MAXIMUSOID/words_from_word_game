from flet import UserControl, TextButton, Text, Column, Container, Row, MainAxisAlignment, colors, DataTable, DataColumn, DataCell, DataRow, BorderSide, padding, TextAlign
from char_btn import Word_buttons_Row
from word_check import WordCheck
import config
from timer import Timer

from player_results import Player_results
from player import Player

class Game_Field(UserControl):
    def build(self):
        
        self.timer = Timer(config.TIMER_VALUE, self.timer_change, self.end_session_timer)
        
        font_size = config.GAME_FIELD_FONT_SIZE
        word_size = config.WORD_SIZE
        
        self.player = Player()
        self.player_results = Player_results()
        
        self.answers = []
        self.WC:WordCheck = WordCheck()
        self.WC.ChekerInicialize()
        
        # Оригинальное слово
        self.word_button_row = Word_buttons_Row(config.WORD.upper(), self.page.width, on_click=self.addChar)
        self.word_button_row.block()
        
        # вводимое пользователем слово
        prefix_word = Text('Ваше слово: ', size=word_size, color=colors.WHITE60)
        self.user_word = Text('', size=word_size, color=colors.WHITE60)
        user_word_row = Container(Row(controls=[prefix_word, self.user_word], alignment=MainAxisAlignment.START), padding=padding.only(left=170))
        
        # кнопки управления
        self.check_word_btn = TextButton(content=Text('Проверить', size=font_size, color=colors.GREEN_500), disabled=True, on_click=self.checkWord)
        self.reset_word_btn = TextButton(content=Text('Сброс', size=font_size, color=colors.RED_500), disabled=True, on_click=self.reset)
        
        self.timer_text = Text(value=self.timer.get_time(), size=config.GAME_FIELD_FONT_SIZE)
        self.start_session_btn = TextButton(content=Text('Начать', size=font_size), on_click=self.start_count)
        self.end_session_btn = TextButton(content=Text('Закончить', size=font_size), on_click=self.end_session, visible=False)
        header_row = Row([self.timer_text, Row([self.start_session_btn, self.end_session_btn], alignment=MainAxisAlignment.END)], alignment=MainAxisAlignment.CENTER)
        
        control_btns = Container(Row([self.check_word_btn, self.reset_word_btn], alignment=MainAxisAlignment.SPACE_AROUND), padding=padding.symmetric(horizontal=5))
        
        # Пользовательская статистика
        self.word_count = Text('Отгадано слов: 0', size=font_size, color=colors.WHITE60)
        self.result_words = Text('', size=font_size, color=colors.WHITE60)
        user_statustic = Column(expand=True, controls=[self.word_count, self.result_words])
        
        # Статистика всех пользователей
        self.all_user_result = DataTable(
                columns=[
                DataColumn(Text("Место", size=config.GAME_FIELD_FONT_SIZE, color=colors.WHITE60)),
                DataColumn(Text("Имя", size=config.GAME_FIELD_FONT_SIZE, color=colors.WHITE60)),
                DataColumn(Text("Рез-т", size=config.GAME_FIELD_FONT_SIZE, color=colors.WHITE60)),
            ],
                horizontal_lines=BorderSide(1, colors.WHITE60),
                rows=self.get_all_user_statistic(),
                column_spacing=10,
                data_row_max_height=font_size*2,
                width=300,
                horizontal_margin=5
        )
        
        all_user_column = Column(
            [
                Text("НАША ГОРДОСТЬ:", size=font_size, color=colors.YELLOW_500),
                self.all_user_result
            ],
            width= 300
        )
        
        # Сбор всей статистики
        statistic = Row(
            expand=True,
            controls=
            [
            user_statustic,
            all_user_column
            ],

        )
        content = Column([header_row, statistic, user_word_row, self.word_button_row.buttons, control_btns])
        # content = Column([self.word_button_row.buttons, control_btns, user_word_row, statistic])
        
        return content
    def timer_change(self):
        self.timer_text.value = self.timer.get_time()
        self.update()
    
    def start_count(self, e):
        self.word_button_row.restart()
        self.check_word_btn.disabled = False
        self.reset_word_btn.disabled = False
        self.start_session_btn.visible = False
        self.end_session_btn.visible = True
        self.timer.start()
        self.update()
    
    def end_session_timer(self):
        self.timer.stop()
        self.page.go('/start_window')
    
    def end_session(self, _):
        self.timer.stop()
        self.page.go('/start_window')
    
    def addChar(self, value):
        self.user_word.value += value
        self.user_word.update()
        
    def checkWord(self, e):
        if self.WC.SubWordIsDictionary(self.user_word.value) and self.user_word.value not in self.answers:
            # Добавление слова
            self.answers.append(self.user_word.value)
            
            # Фиксация результата
            self.player_results.add_result(self.player.nickname, len(self.answers))
            
            # Отображение статистики пользователя
            self.word_count.value = f"Отгадано слов: {len(self.answers)}"
            self.result_words.value = ", ".join(self.answers)
            
            # Отображение статистики всех пользователей
            self.all_user_result.rows = self.get_all_user_statistic()
            
            # сброс вводимого слова
            self.user_word.value = ''
            self.word_button_row.restart()
            self.update()
            
    def get_all_user_statistic(self):
        table_rows = []
        results = self.player_results.get_all_user_statistic(self.player)
        for row in results:
            if row == (None, None, None):
                table_rows.append(
                    DataRow(
                    cells = [
                        DataCell(Text("", size=config.GAME_FIELD_FONT_SIZE, color=colors.WHITE60)),
                        DataCell(Text("***", size=config.GAME_FIELD_FONT_SIZE, color=colors.WHITE60, text_align=TextAlign.CENTER)),
                        DataCell(Text("", size=config.GAME_FIELD_FONT_SIZE, color=colors.WHITE60))
                    ]
                )
                    )
            elif self.player.nickname == row[1]:
                table_rows.append(
                    DataRow(
                    cells =[
                        DataCell(Text(row[0], size=config.GAME_FIELD_FONT_SIZE, color=colors.YELLOW_500)),
                        DataCell(Text(row[1], size=config.GAME_FIELD_FONT_SIZE, color=colors.YELLOW_500)),
                        DataCell(Text(row[2], size=config.GAME_FIELD_FONT_SIZE, color=colors.YELLOW_500))
                    ]
                ))
            else:
                table_rows.append(
                    DataRow(
                    cells =[
                        DataCell(Text(row[0], size=config.GAME_FIELD_FONT_SIZE, color=colors.WHITE60)),
                        DataCell(Text(row[1], size=config.GAME_FIELD_FONT_SIZE, color=colors.WHITE60)),
                        DataCell(Text(row[2], size=config.GAME_FIELD_FONT_SIZE, color=colors.WHITE60))
                    ]
                ))
        return table_rows        
    
    def reset(self, e):
        self.word_button_row.restart()
        self.user_word.value = ''
        self.update()
        
        
if __name__ == "__main__":
    print("начинаю")
    Player().set_player('d')
    Player_results().init(config.RESULT_FILE_NAME)
    Game_Field()
    print("заканчиваю")