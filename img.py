from tkinter  import *
win= Tk()
win.geometry("500x500")


image = Canvas(win,height="500",width="500")
image.place(relx=0,rely=0)
bag = PhotoImage(f"D:\MyPythonfolder2\download(3).jpg")
image.create_image(0,0,image=bag)
win.mainloop()