# Simple Interest Calculator GUI
# image from VectorStock

import tkinter
from tkinter import PhotoImage

root = tkinter.Tk()
root.title("Simple Interest Calculator")
root.geometry('520x270')
root.resizable(0,0)
root_image = PhotoImage(file = "/home/james/Documents/programming/python/1 . Projects/simple_interest/interest.png")
root.iconphoto(False, root_image)

root_font = ("Nimbus Sans Regular", 13)
input_color = ("#282b27")
output_color = ("#092100")
root.config(bg="#dbd1d0")

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

principal_text = tkinter.Text(input_frame, height=1, width=40)
rate_text = tkinter.Text(input_frame, height=1, width=40)
time_text = tkinter.Text(input_frame, height=1, width=40)
principal_text.grid(row=1, column=1, padx=(10,10))
rate_text.grid(row=2, column=1, padx=(10,10), sticky="WE")
time_text.grid(row=3, column=1, padx=(10,10), sticky="WE")

interest_text = tkinter.Text(output_frame, height=2, width=38)
cal_interest = tkinter.Button(output_frame, text="Interest", font=root_font)
exit_button = tkinter.Button(root, text="Exit", font=root_font, command=root.destroy)
interest_text.grid(row=2, column=0, padx=(10,10), pady=(5,5))
cal_interest.grid(row=3, column=0, padx=(5,5), pady=(5,5))
exit_button.grid(row=3, column=1, padx=(5,5), pady=(5,5))


root.mainloop()