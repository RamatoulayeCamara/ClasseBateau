from Importation import *
class Chargement:
    def passagers(root):
        cp____ = 1
        cursor = conn.cursor()
        query9 = "SELECT * FROM Passager WHERE idBateau ='" + str(cp____) + "'"
        cursor.execute(query9)
        result = cursor.fetchall()
        list1 = [list for list in result]   

        entries = []

        row = tk.Frame(root)
        lab0 = tk.Label(row, width=15, text="", borderwidth=1, relief="groove")
        lab1 = tk.Label(row, width=6, text="Vol", borderwidth=1, relief="groove")
        lab2 = tk.Label(row, width=6, text="Weight", borderwidth=1, relief="groove")
        lab3 = tk.Label(row, width=6, text="LCG", borderwidth=1, relief="groove")
        lab4 = tk.Label(row, width=6, text="TCG", borderwidth=1, relief="groove")
        lab5 = tk.Label(row, width=6, text="VCG", borderwidth=1, relief="groove")
        lab6 = tk.Label(row, width=6, text="FSM", borderwidth=1, relief="groove")

        row.pack(side=tk.TOP)
        lab0.pack(side=tk.LEFT)
        lab1.pack(side=tk.LEFT)
        lab2.pack(side=tk.LEFT)
        lab3.pack(side=tk.LEFT)
        lab4.pack(side=tk.LEFT)
        lab5.pack(side=tk.LEFT)
        lab6.pack(side=tk.LEFT)

        for field in list1:
            row = tk.Frame(root)
            lab = tk.Label(row, width=15, text=field[1], anchor="w")
            ent = tk.Entry(row, width=6)
            ent.insert(END, field[2])
            lab2 = tk.Label(row, width=6, text=field[3])
            lab3 = tk.Label(row, width=6, text=field[4])
            lab4 = tk.Label(row, width=6, text=field[5])
            lab5 = tk.Label(row, width=6, text=field[6])
            lab6 = tk.Label(row, width=6, text=field[7])
            row.pack(side=tk.TOP, padx=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.LEFT)
            lab2.pack(side=tk.LEFT)
            lab3.pack(side=tk.LEFT)
            lab4.pack(side=tk.LEFT)
            lab5.pack(side=tk.LEFT)
            lab6.pack(side=tk.LEFT)
            entries.append((field[1], ent))

        return entries
    def cargo(root):
        cp____ = 1
        cursor = conn.cursor()
        query9 = "SELECT * FROM Cargo WHERE idBateau ='" + str(cp____) + "'"
        cursor.execute(query9)
        result = cursor.fetchall()
        list1 = [list for list in result]

        entries = []

        row = tk.Frame(root)
        lab0 = tk.Label(row, width=15, text="", borderwidth=1, relief="groove")
        lab2 = tk.Label(row, width=6, text="Weight", borderwidth=1, relief="groove")
        lab3 = tk.Label(row, width=6, text="LCG", borderwidth=1, relief="groove")
        lab4 = tk.Label(row, width=6, text="TCG", borderwidth=1, relief="groove")
        lab5 = tk.Label(row, width=6, text="VCG", borderwidth=1, relief="groove")
        lab6 = tk.Label(row, width=6, text="FSM", borderwidth=1, relief="groove")

        row.pack(side=tk.TOP)
        lab0.pack(side=tk.LEFT)
        lab2.pack(side=tk.LEFT)
        lab3.pack(side=tk.LEFT)
        lab4.pack(side=tk.LEFT)
        lab5.pack(side=tk.LEFT)
        lab6.pack(side=tk.LEFT)

        for field in list1:
            row = tk.Frame(root)
            lab = tk.Label(row, width=15, text=field[1], anchor="w")
            ent = tk.Entry(row, width=6)
            ent.insert(END, field[2])
            lab2 = tk.Label(row, width=6, text=field[3])
            lab3 = tk.Label(row, width=6, text=field[4])
            lab4 = tk.Label(row, width=6, text=field[5])
            lab5 = tk.Label(row, width=6, text=field[6])
            row.pack(side=tk.TOP, padx=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.LEFT)
            lab2.pack(side=tk.LEFT)
            lab3.pack(side=tk.LEFT)
            lab4.pack(side=tk.LEFT)
            lab5.pack(side=tk.LEFT)
            entries.append((field[1], ent))

        return entries
    def create_menu(self):
        menuBar = tk.Menu(self.master)
        menuFichier2 = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Chargement", menu=menuFichier2)
        menuFichier2.add_command(label="Materiel et Equipage")
        menuFichier2.add_command(label="Passagers", command=self.validation6)
        menuFichier2.add_command(label="Cargo", command=self.validation7)


    