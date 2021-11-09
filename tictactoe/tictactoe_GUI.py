from tictactoe_game_engine import TictactoeGameEngine
import tkinter


class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title('틱택토')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')
        self.root.resizable(width=False, height=False)

        self.canvas = tkinter.Canvas(self.root, bg='white', width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)
        self.canvas.pack()

        self.images = {}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['O'] = tkinter.PhotoImage(file='O.gif')

        self.canvas.bind('<Button-1>', self.click_handler)  #*** (괄호가 없을 떄 바로 실행 안됨)


        self.root.mainloop()

    def click_handler(self, event):
        #input event.x, event.y -> row, col
        row, col = self.coordinate_to_position(event.x, event.y)
        #set row, col
        self.game_engine.set(row, col)
        #show board
        self.game_engine.show_board()
        #set winner

        #승자가 있거나 무승부일 때, 게임오버, 결과 출력하자
        #change turn

    def draw_board(self):
        pass

    def coordinate_to_position(self, x, y):
        return (y//100)+1, (x//100)+1


if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()
