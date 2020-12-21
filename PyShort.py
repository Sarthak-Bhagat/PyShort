import requests
from tkinter import *
from tkinter import messagebox

def shorten():
	url = URL.get()
	api_key = "4c7484b15645d96c861cebe976177ba8064d6"
	api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
	data = requests.get(api_url).json()["url"]
	if data["status"] == 7:
		shortened_url = data["shortLink"]
		print("Shortened URL:", shortened_url)
		root.clipboard_clear()
		root.clipboard_append(shortened_url)
		root.update()	
		messagebox.showinfo(title='Success', message="Shortened URL copied to your clipboard")
		root.destroy()	

	else:
		messagebox.showerror(title='Error', message="[!] Error Shortening URL:")

root = Tk()
root.title("PyShort")

size = [400,200]
root.geometry(f'{size[0]}x{size[1]}')
root.resizable(True, True)

Canvas1 = Canvas(root)
Canvas1.config(bg="#383836")
Canvas1.pack(expand=True,fill=BOTH)

headingFrame = Frame(Canvas1,bg="grey",bd=5)
headingFrame.place(relx=0.13,rely=0.1,relwidth=0.75,relheight=0.25)
headingLabel = Label(headingFrame, text = "Paste Your URL here", bg='black', fg='white', font=('Courier',15), anchor=CENTER)
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
URL = Entry(Canvas1)
URL.place(relx=0.075,rely=0.435, relwidth=0.85,relheight=0.25)
ShortenBtn = Button(Canvas1,text="Shorten",bg='black', fg='white', command=shorten)
ShortenBtn.place(relx=0.275,rely=0.77, relwidth=0.45,relheight=0.2)

root.mainloop()


