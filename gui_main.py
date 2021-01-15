# Simple Interest Calculator GUI
# image from VectorStock

import tkinter
from tkinter import PhotoImage,END,IntVar

root = tkinter.Tk()
root.title("Simple Interest Calculator")
root.geometry('520x320')
root.resizable(0,0)
root_image = PhotoImage(file = "/home/james/Documents/programming/python/1 . Projects/simple_interest/interest.png")
root.iconphoto(False, root_image)

root_font = ("Nimbus Sans Regular", 13)
input_color = ("#282b27")
output_color = ("#092100")
root.config(bg="#dbd1d0")

# FUNCTIONS
def simple_interest():
    ''' Calculates Simple Intrest , where 'p' = Principal, 'r' = Rate in % and 't' = Time'''
    principal = int(principal_text_field.get('1.0', END))
    rate = int(rate_text_field.get('1.0', END))
    time = int(time_text_field.get('1.0', END))
    interest = principal * rate * time / 100
    # inserts the interest calculated into the intrest_text_field
"""    interest_text_field.insert('1.0', interest)
    if principal != int():
        interest_text_field.insert("ERROR!!")
    elif rate != int():
        interest_text_field.insert("ERROR!!")
    elif time != int():
        interest_text_field.insert("ERROR!!")"""


def clear():
    '''clears text fields'''
    principal_text_field.delete('1.0',END)
    rate_text_field.delete('1.0', END)
    time_text_field.delete('1.0', END)
    interest_text_field.delete('1.0', END)

# MAIN PROGRAM STARTS HERE ...
input_frame = tkinter.LabelFrame(root, font=root_font)
output_frame = tkinter.LabelFrame(root)
input_frame.grid(row=2, column=0, padx=75, pady=10, sticky="W")
output_frame.grid(pady=10, padx=5)

intro_label = tkinter.Label(root, text="Simple Interest Calculator", font=root_font,bg="#dbd1d0")
intro_label.grid(row=0, column=0, rowspan=2, padx=155, pady=15)

principal = tkinter.Label(input_frame, text="Principal", font=root_font)
principal.grid(row=1, column=0)
rate = tkinter.Label(input_frame, text="Rate", font=root_font)
rate.grid(row=2, column=0)
time = tkinter.Label(input_frame, text="Time", font=root_font)
time.grid(row=3, column=0)

"""interest = IntVar()"""
principal_text_field = tkinter.Text(input_frame, height=1, width=40)
rate_text_field = tkinter.Text(input_frame, height=1, width=40)
time_text_field = tkinter.Text(input_frame, height=1, width=40)
principal_text_field.grid(row=1, column=1, padx=(10,10))
rate_text_field.grid(row=2, column=1, padx=(10,10), sticky="WE")
time_text_field.grid(row=3, column=1, padx=(10,10), sticky="WE")
cal_interest = tkinter.Button(input_frame, text="Interest", font=root_font, command=simple_interest)
cal_interest.grid(row=4, column=0, padx=(5,0), pady=(5,5),columnspan=3)


interest_text_field = tkinter.Text(output_frame, height=2, width=38)
interest_text_field.grid(row=0, column=0, padx=(10,10), pady=(5,5))
clear_button = tkinter.Button(output_frame, text="Clear", font=root_font, command=clear)
clear_button.grid(pady=(0,10))
#clear_button.grid(row=3, column=2, padx=(5,5), pady=(5,5))


root.mainloop() 