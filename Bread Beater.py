#for learning purposes 🥺🥺

import tkinter as tk

#basic stuffses
bread = 0
breadPerBeat = 1

#building stuffses
buildings = {
    "Loaf":     {"cost": 10, "bpb": 1, "exponent": 0},
    "Bakerer":        {"cost": 100, "bpb": 10, "exponent": 0},
    "Dough Machine":  {"cost": 1000, "bpb": 100, "exponent": 0},
    "Wind Mill":     {"cost": 10000, "bpb": 1000, "exponent": 0}
}

def clickBread():
    global bread
    bread += breadPerBeat
    updateDisplay()

def updateDisplay():
    breadLabel.config(text=f"Bread:{bread:.2f}")
    bpbLabel.config(text=f"Bread Per Click:{breadPerBeat}")

def buyBuilding(nameOfBuilding):
    global bread, breadPerBeat
    if bread >= buildings[nameOfBuilding]["cost"]:
        bread -= buildings[nameOfBuilding]["cost"]
        breadPerBeat += buildings[nameOfBuilding]["bpb"]
        buildings[nameOfBuilding]["exponent"] += 1
        buildings[nameOfBuilding]["cost"] *= (1 + buildings[nameOfBuilding]["exponent"] * 0.125)
        updateDisplay()

#main window stuffses
root = tk.Tk()
root.title("Bread Beater")
root.geometry("300x250")


#text stuffses
breadLabel = tk.Label(root, text="Bread: 0", font=("Arial", 20))
bpbLabel = tk.Label(root, text="Bread Per Beat: 1", font=("Arial", 20))

breadLabel.pack()
bpbLabel.pack()

#MAIN BUTTON stuffses???
clickBtn = tk.Button(
    root,
    text="Click! 🍞",
    font=("Arial", 15),
    width=12,
    height=2,
    command=clickBread
)
clickBtn.pack(pady=10)


#shop stuffses
for building, stuffses in buildings.items():
    btn = tk.Button(
        root,
        text=f"Buy {building} ({stuffses["cost"]} bread)",
        font=("Arial", 10),
        command=lambda b=building: buyBuilding(b)
    )
    btn.pack(pady=2)

root.mainloop()