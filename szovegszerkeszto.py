from tkinter import *
from tkinter import filedialog
root=Tk()
root.title("Szövegszerkesztő")
root.geometry("600x400")


Cim=Label(root,text="Mikroszoft Vord",font=("Centaur",20))
Cim.pack(pady=10 )

nagyentry= Text(root, width=70, height=12)
nagyentry.pack(pady=10 )

kisentry=Entry(root, width=50)
kisentry.pack(pady=10 )

betoltes=Button(root, text="Betöltés")
betoltes.pack(pady=10 )

mentes=Button(root, text="Mentés")
mentes.pack()
root.mainloop()