import  tkinter as Tkinter
import pygame
def print_value(val):
    print(val)
def play_music():
    pygame.init()
    pygame.mixer.music.load(port2)
    pygame.mixer.music.play(-1)

port1 = '/Users/evgeshakrasava/PycharmProjects/c.mp3'
port2 = '/home/qbc/Downloads/c.mp3'
root = Tkinter.Tk()

scale = Tkinter.Scale(orient='horizontal', from_=0, to=128, command=print_value)
scale.pack()

b = Tkinter.Button(root, text="OK", command=play_music)
b.pack()




root.mainloop()

'''
import Tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.scale = tk.Scale(self, orient="horizontal", 
                              from_=0, to=600, 
                              showvalue=False,
                              command=self._on_scale)
        self.scale_label = tk.Label(self, text="")
        self.scale.pack(side="top", fill="x")
        self.scale_label.pack(side="top")

    def _on_scale(self, value):
        value = int(value)
        minutes = value/60
        seconds = value%60
        self.scale_label.configure(text="%2.2d:%2.2d" % (minutes, seconds))

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True);
    root.mainloop()
'''
