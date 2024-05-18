from flet import app, Page, View, Container, ImageFit, OptionalNumber, Theme, padding

from game_field import Game_Field
from start_window import Start_Window

from player_results import Player_results
from player import Player
from config import RESULT_FILE_NAME

def main(game_page: Page):
    print(game_page.width)
    game_page.title = "Слова из Слова"
    game_page.padding = 0
    
    
    
    
    game_page.on_resize = lambda _: print(game_page.width)
    
    game_page.fonts = {
        "School_Board":"/font/Chalkduster.ttf",
        "Open Sans": "fonts/OpenSans-Regular.ttf",
    }
    


    game_page.theme = Theme(font_family="School_Board")
    game_page.window_full_screen=True
    start_window = Start_Window()
    game_field = Game_Field()
    page_content = Container(
                expand=True,
                image_src="fone/main_bg.png",
                image_fit=ImageFit.FILL,
                height=game_page.height,
                padding=padding.only(top=2, left=20, right=20, bottom=2),
                margin=0
            )


    
    
    
    def route_change(route):

        
        
        
        if game_page.route == "/start_window":
            
            page_content.content = start_window
            game_page.views.clear()
            game_page.views.append(
                View(
                    "/start_window",
                    [
                    page_content
                    
                ],
                padding=0
                )
            )
        if game_page.route == "/game_field":
            
            page_content.content = game_field
            game_page.views.clear()
            game_page.views.append(
                View(
                    "/game_field",
                    [
                    page_content
                    
                ],
                padding=0
                )
            )

        game_page.update()
        
        
    def view_pop(view):
        game_page.views.pop()
        top_view = game_page.views[-1]
        game_page.go(top_view.route)
        
    
    game_page.on_route_change = route_change
    game_page.on_view_pop = view_pop
    game_page.go("/start_window")


if __name__ == "__main__":
    Player_results().init(RESULT_FILE_NAME)
    Player()
    app(target=main, assets_dir="assets")