import tkinter as tk

class MainWnd:
    def __init__(self, master):
        b1 = master.button()
        b1.pack()
        b2 = master.button()
        b2.pack()

        master.mainloop()

class SecondWnd:
    def __init__(self, master, cmd):
        application = tk.StringVar()
        username = tk.StringVar()
        password = tk.StringVar()
        email = tk.StringVar()

        tk.Label(master, text='Application: ')
        tk.Entry(master, textvariable=application)
        tk.Label(master, text='Username: ')
        tk.Entry(master, textvariable=username)
        tk.Label(master, text='Password: ')
        tk.Entry(master, textvariable=password)
        tk.Label(master, text='Email: ')
        tk.Entry(master, textvariable=email)
        tk.Button(master, text='Submit', command= cmd)

