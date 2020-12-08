# python 3 version of tkinter
import tkinter

# windows serves as main entry into GUI
window = tkinter.Tk()

# add a title to the window
window.title("Python GUI")

# set window size
window.geometry("450x250")

# Focus on four elements: Label, Button, Entry(Input), and Text

#Label
# create some sort of text display to the user that is using the program
label = tkinter.Label(window, text="Some label text",width = 50)

# defining the label we have to pack it and set it into the window
label.pack()

# Create Button for the window
def clicked():
    label = tkinter.Label(window, text="Button label",width = 50)
    label.pack()

butt = tkinter.Button(window, text="Click button!", command=clicked,width = 10)
butt.pack()

# Entry (Text Box)
entry = tkinter.Entry(window, width=10)
entry.pack()

# Text - Specialized Text Box, which is much more customizable than the regular Entry
text = tkinter.Text(window, width=20, height=5)
text.insert(tkinter.INSERT, "Hello")
text.insert(tkinter.END, "World")
text.pack()

# call mainloop and excute all command for the GUI
window.mainloop()

