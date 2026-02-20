import tkinter as tk
from tkinter import ttk


def crear_vista(bitacora):
    root = tk.Tk()
    root.title("🪸 Proyecto BITACORA DE BUCEO 🫧")

    tk.Label(root, text="Fecha (YYYY-MM-DD)").grid(
        row=0,
        column=0,
        padx=5,
        pady=5
        )
    entry_fecha = tk.Entry(root)
    entry_fecha.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Lugar").grid(
        row=1,
        column=0,
        padx=5,
        pady=5
        )
    entry_lugar = tk.Entry(root)
    entry_lugar.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Profundidad (m)").grid(
        row=2,
        column=0,
        padx=5,
        pady=5
        )
    entry_profundidad = tk.Entry(root)
    entry_profundidad.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="Tiempo (min)").grid(
        row=3,
        column=0,
        padx=5,
        pady=5
        )
    entry_tiempo = tk.Entry(root)
    entry_tiempo.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(root, text="Observaciones").grid(
        row=4,
        column=0,
        padx=5,
        pady=5
        )
    entry_obs = tk.Entry(root, width=40)
    entry_obs.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(root, text="Buscar (fecha/lugar)").grid(
        row=5,
        column=0,
        padx=5,
        pady=5
        )
    entry_buscar = tk.Entry(root, width=30)
    entry_buscar.grid(row=5, column=1, padx=5, pady=5)

    tk.Button(
        root,
        text="Alta",
        command=lambda: bitacora.alta_inmersion(
            entry_fecha,
            entry_lugar,
            entry_profundidad,
            entry_tiempo,
            entry_obs,
            tree
        ),
    ).grid(row=6, column=0, padx=5, pady=5)

    tk.Button(
        root,
        text="Modificar",
        command=lambda: bitacora.modificar_inmersion(
            tree,
            entry_fecha,
            entry_lugar,
            entry_profundidad,
            entry_tiempo,
            entry_obs
        ),
    ).grid(row=6, column=1, padx=5, pady=5)

    tk.Button(
        root,
        text="Eliminar",
        command=lambda: bitacora.eliminar_inmersion(tree)
    ).grid(row=6, column=2, padx=5, pady=5)

    tk.Button(
        root,
        text="Consultar",
        command=lambda: bitacora.mostrar_inmersiones(tree, entry_buscar),
    ).grid(row=6, column=3, padx=5, pady=5)

    tk.Button(
        root,
        text="Limpiar",
        command=lambda: bitacora.limpiar_campos(
            entry_fecha,
            entry_lugar,
            entry_profundidad,
            entry_tiempo,
            entry_obs,
            entry_buscar,
            tree,
        ),
    ).grid(row=6, column=4, padx=5, pady=5)

    columns = (
        "ID",
        "Fecha",
        "Lugar",
        "Profundidad",
        "Tiempo",
        "Observaciones"
        )
    tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    tree.grid(row=7, column=0, columnspan=5, padx=10, pady=10)
    bitacora.mostrar_inmersiones(tree, entry_buscar)
    root.mainloop()
