from tkinter import * #importing everything from tkinter
import time #importing library for determing real world time

main_window = Tk() #main windows for our clock
clock = Label(main_window, font=('Bodoni', 100, 'italic','bold'),fg='yellow', bg='red') #designating place for clock timer
clock.pack(fill=BOTH, expand=1)
def tick(): #making the clock tick
    s = time.strftime('%H:%M:%S') 
    if s != clock["text"]:
        clock["text"] = s
    clock.after(200, tick)#change after 200 milliseconds

tick()
main_window.mainloop()
