from tkinter import *
from tkinter import ttk

    
root = Tk()
root.title("Peer Tutoring System")

mainframe = ttk.Frame(root, padding="12 12 24 24")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

username = StringVar()
password = StringVar()

nameEnter = ttk.Entry(mainframe, width=7, textvariable=username)
nameEnter.grid(column=3, row=1, sticky=(W, E))

passEnter = ttk.Entry(mainframe, width=7, textvariable=password)
passEnter.grid(column=3, row=2, sticky=(W, E))

#ttk.Label(mainframe, textvariable=username).grid(column=1, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Enter").grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="UserName:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Password").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

nameEnter.focus()

#root.bind('<Return>')

root.mainloop()
