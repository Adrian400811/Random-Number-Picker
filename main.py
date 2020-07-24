#import modules
import random
import tkinter as tk

window = tk.Tk()
window.title('Random Number Picker')
window.geometry('400x300')
window.configure(background='white')

def pick():
    low_lim = float(low_lim_entry.get())
    hi_lim = float(hi_lim_entry.get())
    result = (random.randint(int(low_lim),int(hi_lim)))
    result_label.configure(text=result)

low_lim_frame = tk.Frame(window)
low_lim_frame.pack(side=tk.TOP)
low_lim_label = tk.Label(low_lim_frame, text='Lower Limit')
low_lim_label.pack(side=tk.LEFT)
low_lim_entry = tk.Entry(low_lim_frame)
low_lim_entry.pack(side=tk.LEFT)

hi_lim_frame = tk.Frame(window)
hi_lim_frame.pack(side=tk.TOP)
hi_lim_label = tk.Label(hi_lim_frame, text='Higher Limit')
hi_lim_label.pack(side=tk.LEFT)
hi_lim_entry = tk.Entry(hi_lim_frame)
hi_lim_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text='Pick a number now', command=pick)
calculate_btn.pack()

window.mainloop()