
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Dec 11, 2018 02:22:11 AM +03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    GUI_support.set_Tk_var()
    top = Toplevel1 (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    GUI_support.set_Tk_var()
    top = Toplevel1 (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 

        top.geometry("609x723+620+168")
        top.title("Arama Motoru")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.148, rely=0.166, relheight=0.602
                , relwidth=0.714)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=435)

        self.Message1 = tk.Message(self.Frame1)
        self.Message1.place(relx=0.023, rely=0.023, relheight=0.926
                , relwidth=0.966)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text=''' ''')
        self.Message1.configure(textvariable=GUI_support.textVar)
        self.Message1.configure(width=420)

        self.but44 = tk.Button(top)
        self.but44.place(relx=0.722, rely=0.069, height=54, width=87)
        self.but44.configure(activebackground="#ececec")
        self.but44.configure(activeforeground="#000000")
        self.but44.configure(background="#d9d9d9")
        self.but44.configure(command=GUI_support.isClicked)
        self.but44.configure(disabledforeground="#a3a3a3")
        self.but44.configure(foreground="#000000")
        self.but44.configure(highlightbackground="#d9d9d9")
        self.but44.configure(highlightcolor="black")
        self.but44.configure(pady="0")
        self.but44.configure(text='''Search''')
        self.but44.configure(width=87)

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.181, rely=0.083,height=20, relwidth=0.483)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=GUI_support.entryInput)
        self.Entry1.configure(width=294)





