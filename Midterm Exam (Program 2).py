# Program 2: Create a program to produce the interface. After typing the name in the first text
# field, click the button to display the name to another text field. (50 points)


from tkinter import *
window = Tk()

window.geometry("600x400+30+20")
window.title("Midterm in OOP")

#add label
label1=Label(window,text="Enter your fullname", fg="red")
label1.place(x= 60, y = 150)

#Add text field widget
txtfld = Entry(window, bd = 3, font = ("verdana",16))
txtfld.place(x=250, y=150)

#add Button widget
btn = Button(window, text = "Click to display your fullname ", fg="red")
btn.place(x= 60, y = 200)

#Add text field widget
txtfld = Entry(window, bd = 3, font = ("verdana",16))
txtfld.place(x=250, y=200)

window.mainloop()
