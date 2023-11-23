from tkinter import *
from tkinter import filedialog
root=Tk()
root.title("Szövegszerkesztő")
root.geometry("600x400")
root.resizable(FALSE,FALSE)

def betolt():
    szoveg.configure(state=NORMAL)
    szoveg_betolt = kisentry.get()
    szoveg.insert(END, szoveg_betolt + "\n")
    kisentry.delete(0, END)
    szoveg.configure(state=DISABLED)

def ment():
    szoveg_ment = szoveg.get("1.0", END)
    hely = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[( "*.txt", "*.*")])
    if hely:
        with open(hely,"w") as file:
            file.write(szoveg_ment)

def uj():
    szoveg.configure(state=NORMAL)
    szoveg.delete("1.0", END)
    szoveg.configure(state=DISABLED)

Cim=Label(root,text="Mikroszoft Vord",font=("Centaur",20))
Cim.pack(pady=10 )

szoveg= Text(root, width=62, height=9, state=DISABLED ,font=("Centaur",14))
szoveg.pack(pady=10 )

kisentry=Entry(root, width=40,font=("Centaur",14))
kisentry.pack(pady=10 )

gombframe=LabelFrame(root,border=0)
gombframe.pack(pady=10)

betoltes=Button(gombframe, text="Betöltés", command=betolt,font=("Centaur",15))
betoltes.grid(row=0, column=0 ,padx=10)

mentes=Button(gombframe, text="Mentés", command=ment,font=("Centaur",15))
mentes.grid(row=0, column=1 ,padx=10)

new=Button(gombframe,text="Új fájl", command=uj,font=("Centaur",15))
new.grid(row=0, column=2 ,padx=10)

root.mainloop()