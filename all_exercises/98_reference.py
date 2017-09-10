"""
有個中文的說明。
http://www.360doc.com/content/14/0328/02/9482_364311622.shtml

這算是一個widget 的基本物件。
class Tk(Misc, Wm)
 |  Toplevel widget of Tk which represents mostly the main window
 |  of an application. It has an associated Tcl interpreter.


這應該 是框架的基本設定， **kw , or *args , 我前幾天剛好有看到，
一個* or 二個，是不同的意思，但基本上是說，它後面有幾個變數都可以，
沒有限定， ** 的話， 我記得可以使用，它沒有指定的變數。
reference:
    https://github.com/taizilongxu/interview_python#10-args-and-kwargs
>>> help(ttk.Frame)
class Frame(Widget)
 |  Ttk Frame widget is a container, used to group other widgets
 |  together.
 |  Methods defined here:
 |
 |  __init__(self, master=None, **kw)
 |      Construct a Ttk Frame with parent master.
 |
 |      STANDARD OPTIONS
 |
 |          class, cursor, style, takefocus
 |
 |      WIDGET-SPECIFIC OPTIONS
 |
 |          borderwidth, relief, padding, width, height


grid_configure(cnf={}, **kw) method of tkinter.ttk.Frame instance
Position a widget in the parent widget in a grid. Use as options:
column=number - use cell identified with given column (starting with 0)
columnspan=number - this widget will span several columns
in=master - use master to contain this widget
in_=master - see 'in' option description
ipadx=amount - add internal padding in x direction
ipady=amount - add internal padding in y direction
padx=amount - add padding in x direction
pady=amount - add padding in y direction
row=number - use cell identified with given row (starting with 0)
rowspan=number - this widget will span several rows
sticky=NSEW - if cell is larger on which sides will this
                  widget stick to the cell boundary

"""
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
