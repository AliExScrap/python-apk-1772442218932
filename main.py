import tkinter as tk

class ChapeletElectronique:
    def __init__(self, root):
        self.root = root
        self.root.title("Tasbih")
        self.root.geometry("250x350")
        self.root.configure(bg="#2c3e50") # Couleur sombre style plastique
        
        self.count = 0

        # --- Affichage Digital ---
        self.ecran = tk.Label(
            root, text="0000", font=("Courier", 40, "bold"),
            bg="#95a5a6", fg="#2c3e50", width=6, pady=10
        )
        self.ecran.pack(pady=30)

        # --- Grand Bouton "Compter" ---
        # On utilise un Canvas pour créer un bouton rond sans image
        self.btn_click = tk.Canvas(root, width=120, height=120, bg="#2c3e50", highlightthickness=0)
        self.btn_click.pack(pady=10)
        
        # Dessin du bouton rond
        self.cercle = self.btn_click.create_oval(10, 10, 110, 110, fill="#e74c3c", outline="#c0392b", width=4)
        self.btn_click.tag_bind(self.cercle, "<Button-1>", lambda e: self.incrementer())

        # --- Petit Bouton "Reset" ---
        self.btn_reset = tk.Button(
            root, text="RESET", command=self.reset,
            font=("Arial", 10, "bold"), bg="#7f8c8d", fg="white",
            activebackground="#95a5a6", relief="flat"
        )
        self.btn_reset.pack(pady=20)

        # Liaison avec la touche Espace du clavier
        self.root.bind("<space>", lambda e: self.incrementer())

    def incrementer(self):
        self.count += 1
        # Formattage pour garder 4 chiffres (ex: 0001)
        self.ecran.config(text=f"{self.count:04}")
        # Effet visuel rapide sur le bouton
        self.btn_click.itemconfig(self.cercle, fill="#ff6b6b")
        self.root.after(100, lambda: self.btn_click.itemconfig(self.cercle, fill="#e74c3c"))

    def reset(self):
        self.count = 0
        self.ecran.config(text="0000")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChapeletElectronique(root)
    root.mainloop()
