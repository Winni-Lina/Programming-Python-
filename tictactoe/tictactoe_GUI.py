from tictactoe_game_engine import TictactoeGameEngine
import tkinter


class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title('틱택토')
        self.root.resizable(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')
        self.root.resizable(width=False, height=False)

    def click_handler(self, event):
        pass
    def draw_board(self):
        pass

if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()
