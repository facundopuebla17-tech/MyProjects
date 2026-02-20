from tkinter import messagebox


class Utilidades:
    def __init__(self, modelo):
        self.modelo = modelo

    def limpiar_campos(
        self,
        entry_fecha,
        entry_lugar,
        entry_profundidad,
        entry_tiempo,
        entry_obs,
        entry_buscar,
        tree,
    ):

        entry_fecha.delete(0, "end")
        entry_lugar.delete(0, "end")
        entry_profundidad.delete(0, "end")
        entry_tiempo.delete(0, "end")
        entry_obs.delete(0, "end")
        entry_buscar.delete(0, "end")
        self.mostrar_inmersiones(tree, entry_buscar)

    def alta_inmersion(
        self,
        entry_fecha,
        entry_lugar,
        entry_profundidad,
        entry_tiempo,
        entry_obs,
        tree
    ):

        fecha = entry_fecha.get()
        lugar = entry_lugar.get()
        try:
            profundidad = float(entry_profundidad.get())
            tiempo = int(entry_tiempo.get())
        except ValueError:
            messagebox.showerror(
                "Ups!",
                "Profundidad debe ser número y tiempo entero"
                )
            return
        observaciones = entry_obs.get()

        if not fecha or not lugar:
            messagebox.showerror(
                "Ups!",
                "Fecha y lugar son obligatorios"
                )
            return

        try:
            self.modelo.alta(
                fecha,
                lugar,
                profundidad,
                tiempo,
                observaciones
                )
            messagebox.showinfo(
                "Listo!!",
                "Inmersión registrada"
                )
            self.mostrar_inmersiones(tree, entry_buscar=None)
        except ValueError as e:
            messagebox.showerror(
                "Error de validacion",
                str(e)
                )

    def mostrar_inmersiones(self, tree, entry_buscar):

        filtro = entry_buscar.get() if entry_buscar else ""
        for row in tree.get_children():
            tree.delete(row)
        for r in self.modelo.consultar(filtro):
            tree.insert("", "end", values=r)

    def modificar_inmersion(
        self,
        tree,
        entry_fecha,
        entry_lugar,
        entry_profundidad,
        entry_tiempo,
        entry_obs
    ):

        seleccionado = tree.selection()
        if not seleccionado:
            messagebox.showwarning(
                "¡¡Atención!!",
                "Seleccione una inmersión"
                )
            return
        id_inmersion = tree.item(seleccionado)["values"][0]
        fecha = entry_fecha.get()
        lugar = entry_lugar.get()
        profundidad = float(
            entry_profundidad.get()
            )
        tiempo = int(
            entry_tiempo.get()
            )
        observaciones = entry_obs.get()
        self.modelo.modificar(
            id_inmersion,
            fecha,
            lugar,
            profundidad,
            tiempo,
            observaciones
        )
        messagebox.showinfo(
            "Listo!!",
            "Inmersión modificada"
            )
        self.mostrar_inmersiones(
            tree, entry_buscar=None
            )

    def eliminar_inmersion(self, tree):
        seleccionado = tree.selection()
        if not seleccionado:
            messagebox.showwarning(
                "¡¡Atención!!",
                "Seleccione una inmersión"
                )
            return
        id_inmersion = tree.item(seleccionado)["values"][0]
        self.modelo.eliminar(id_inmersion)
        messagebox.showinfo(
            "Listo!!",
            "Inmersión eliminada"
            )
        self.mostrar_inmersiones(tree, entry_buscar=None)

    def cargar_seleccion(
        self,
        event,
        tree,
        entry_fecha,
        entry_lugar,
        entry_profundidad,
        entry_tiempo,
        entry_obs,
        entry_buscar,
    ):

        seleccionado = tree.selection()
        if not seleccionado:
            return

        valores = tree.item(seleccionado)["values"]

        self.limpiar_campos(
            entry_fecha,
            entry_lugar,
            entry_profundidad,
            entry_tiempo,
            entry_obs,
            entry_buscar,
            tree,
        )
        entry_fecha.insert(0, valores[1])
        entry_lugar.insert(0, valores[2])
        entry_profundidad.insert(0, valores[3])
        entry_tiempo.insert(0, valores[4])
        entry_obs.insert(0, valores[5])
