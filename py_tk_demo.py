import tkinter as tk


# Konstante

TITLE_PADX = 5
TITLE_PADY = (30, 30)
TITLE_FONT = ('Times New Roman', 18)

SUBTITLE_PADX = 5
SUBTITLE_PADY = (20,10)
SUBTITLE_FONT = ('Times New Roman', 16)

BODY_PADX = 10
BODY_PADY = (5,5)
BODY_FONT = ('Verdana', 12)

BTN_PADX = (10,0)
BTN_LAST_PADX = (10,10)
BTN_IPADX = 10
BTN_PADY = 20
BTN_IPADY = 10
BTN_FONT = ('Verdana', 12)

movies_list = [
    'Gospodar Prstenova',
    'Hobit',
    '1.Maj, 3. dan',
    'Batman',
    'Sam u kuci'
]

# FUNKCIJE

def btn_load_handler():
    lb_movies_var.set(value=movies_list)
    print(f'Pozdrav iz "btn_load_handler" funkcije"')

def btn_save_handler():
    print(f'Pozdrav iz "btn_save_handler" funkcije"')
    
def btn_cancle_handler():
    lb_movies_var.set(value=[])
    print(f'Pozdrav iz "btn_cancle_handler" funkcije"')









main_window = tk.Tk()
main_window.title('Python Tkinter demo aplikacija')
main_window.geometry('600x600')


#region APP TITLE
lbl_app_title = tk.Label(main_window,
                         text='Dobro dosli u Tkinter demo aplikaciju!',
                         font=TITLE_FONT)

lbl_app_title.pack(padx=TITLE_PADX, pady=TITLE_PADY)
#endregion


#region HEADER
# HEADER
frm_header = tk.LabelFrame(main_window,
                           text='Akcije',
                           font=BODY_FONT)

frm_header.pack(padx=BODY_PADX, pady=BODY_PADY, fill=tk.BOTH)
frm_header.columnconfigure(index=0, weight=1)
frm_header.columnconfigure(index=1, weight=1)
frm_header.columnconfigure(index=2, weight=1)


btn_load = tk.Button(frm_header,
                     text='Ucitaj podatke',
                     command=btn_load_handler,
                     font=BTN_FONT)

btn_load.grid(row=0, column=0,
              sticky=tk.EW,
              padx=BTN_PADX,
              pady=BTN_PADY,
              ipadx=BTN_IPADX,
              ipady=BTN_IPADY)

btn_save = tk.Button(frm_header,
                     text='Snimi podatke',
                     command=btn_save_handler,
                     font=BTN_FONT)

btn_save.grid(row=0, column=1,
              sticky=tk.EW,
              padx=BTN_PADX,
              pady=BTN_PADY,
              ipadx=BTN_IPADX,
              ipady=BTN_IPADY)

btn_cancle = tk.Button(frm_header,
                     text='Odustani',
                     command=btn_cancle_handler,
                     font=BTN_FONT)

btn_cancle.grid(row=0, column=2,
                sticky=tk.EW,
              padx=BTN_LAST_PADX,
              pady=BTN_PADY,
              ipadx=BTN_IPADX,
              ipady=BTN_IPADY)
#endregion


#region BODY
frm_body = tk.LabelFrame(main_window,
                         text='Glavni okvir',
                         font=BODY_FONT)

frm_body.pack(padx=BODY_PADX, pady=BODY_PADY, fill=tk.BOTH)

lb_movies_var = tk.StringVar()


lb_movies = tk.Listbox(frm_body,
                       selectmode=tk.MULTIPLE,
                       font=BODY_FONT,
                       height=8,
                       width=50,
                       listvariable=lb_movies_var)

lb_movies.pack(padx=BODY_PADX, pady=BODY_PADY, fill=tk.BOTH)
#endregion




main_window.mainloop()

