from tkinter import *
import subprocess


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.winfo_toplevel().title("Volume Control")

    def createWidgets(self):

        self.slider = Scale(self, from_=0, to=100, orient=HORIZONTAL, length=300, width=50)
        self.slider.set(self.get_volume())
        self.slider.pack()

        self.QUIT = Button(self, text="QUIT", fg="red", command=self.set_volume)
        self.QUIT.pack(side="bottom")

    def get_volume(self):
        return int(subprocess.check_output("pulsemixer --get-volume".split(" "))[0:2])

    def set_volume(self, v=None):
        if not v:
            v = self.slider.get()
        subprocess.call(f"pulsemixer --set-volume {v}".split(" "))
        self.winfo_toplevel().destroy()


root = Tk()
app = Application(master=root)
app.mainloop()
