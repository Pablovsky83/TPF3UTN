import tkinter as tk
from tkinter import messagebox, ttk, StringVar
from bd_manager import (
    BaseDeDatos,
)  # Asegúrate de reemplazar "nombre_del_modulo" con el nombre real del módulo donde está definida la clase BaseDeDatos.
from medicion import Medicion

# Resto del código de ui.py


class VentanaRegistroMediciones:
    def __init__(self, root, base_de_datos):
        self.root = root
        self.base_de_datos = base_de_datos

        self.root.title("Registro de Mediciones")

        self.crear_tabla()
        self.crear_botones()

    def crear_tabla(self):
        self.tabla = ttk.Treeview(
            self.root,
            columns=("ID", "Muestra", "Especie", "Pplant", "Pconfig", "Pini", "Pfin"),
            show="headings",
        )
        self.tabla.pack()

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Muestra", text="Código de muestra")
        self.tabla.heading("Especie", text="Especie")
        self.tabla.heading("Pplant", text="Presión de la planta")
        self.tabla.heading("Pconfig", text="Presión de configuración")
        self.tabla.heading("Pini", text="Presión inicial")
        self.tabla.heading("Pfin", text="Presión final")

        scrollbar = ttk.Scrollbar(
            self.root, orient="vertical", command=self.tabla.yview
        )
        scrollbar.pack(side="right", fill="y")
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.mostrar_registros()

    def mostrar_registros(self):
        self.limpiar_tabla()
        registros = self.base_de_datos.obtener_mediciones()
        for registro in registros:
            self.tabla.insert("", "end", values=registro)

    def limpiar_tabla(self):
        self.tabla.delete(*self.tabla.get_children())

    def crear_botones(self):
        ttk.Button(self.root, text="AGREGAR", command=self.agregar_registro).pack()
        ttk.Button(self.root, text="MODIFICAR", command=self.modificar_registro).pack()
        ttk.Button(self.root, text="ELIMINAR", command=self.eliminar_registro).pack()

    def agregar_registro(self):
        # Implementa la lógica para agregar un registro
        def guardar_registro():
            muestra = entrada_muestra.get()
            especie = entrada_especie.get()
            pplant = entrada_pplant.get()
            pconfig = entrada_pconfig.get()
            pini = entrada_pini.get()
            pfin = entrada_pfin.get()
            # Validar que los campos no estén vacíos
            campos_ok = all([muestra, especie, pplant, pconfig, pini, pfin])
            if campos_ok:
                # Intentar convertir los valores numéricos a float
                try:
                    pplant = float(pplant)
                    pconfig = float(pconfig)
                    pini = float(pini)
                    pfin = float(pfin)
                except ValueError:
                    messagebox.showerror(
                        "Error", "Los campos numéricos deben ser números válidos."
                    )
                    return
                # Insertar el nuevo registro en la base de datos
                medicion = Medicion(
                    muestra=muestra,
                    especie=especie,
                    pplant=pplant,
                    pconfig=pconfig,
                    pini=pini,
                    pfin=pfin,
                )

                self.base_de_datos.agregar_medicion(medicion)
                messagebox.showinfo("Éxito", "Registro agregado correctamente.")
                ventana_agregar.destroy()
                self.mostrar_registros()
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")

        ventana_agregar = tk.Toplevel(self.root)
        ventana_agregar.title("Agregar Registro")

        etiqueta_muestra = ttk.Label(ventana_agregar, text="Muestra:")
        etiqueta_muestra.pack()
        entrada_muestra = ttk.Entry(ventana_agregar)
        entrada_muestra.pack()

        etiqueta_especie = ttk.Label(ventana_agregar, text="Especie:")
        etiqueta_especie.pack()
        entrada_especie = ttk.Entry(ventana_agregar)
        entrada_especie.pack()

        etiqueta_pplant = ttk.Label(ventana_agregar, text="Pplant:")
        etiqueta_pplant.pack()
        entrada_pplant = ttk.Entry(ventana_agregar)
        entrada_pplant.pack()

        etiqueta_pconfig = ttk.Label(ventana_agregar, text="Pconfig:")
        etiqueta_pconfig.pack()
        entrada_pconfig = ttk.Entry(ventana_agregar)
        entrada_pconfig.pack()

        etiqueta_pini = ttk.Label(ventana_agregar, text="Pini:")
        etiqueta_pini.pack()
        entrada_pini = ttk.Entry(ventana_agregar)
        entrada_pini.pack()

        etiqueta_pfin = ttk.Label(ventana_agregar, text="Pfin:")
        etiqueta_pfin.pack()
        entrada_pfin = ttk.Entry(ventana_agregar)
        entrada_pfin.pack()

        boton_guardar = ttk.Button(
            ventana_agregar, text="Guardar", command=guardar_registro
        )
        boton_guardar.pack()

    def modificar_registro(self):
        # Implementa la lógica para modificar un registro
        seleccionado = self.tabla.focus()
        if seleccionado:
            datos = self.tabla.item(seleccionado)["values"]

        def guardar_modificacion():
            muestra = entrada_muestra.get()
            especie = entrada_especie.get()
            pplant = entrada_pplant.get()
            pconfig = entrada_pconfig.get()
            pini = entrada_pini.get()
            pfin = entrada_pfin.get()
            # Validar que los campos no estén vacíos
            campos_ok = all([muestra, especie, pplant, pconfig, pini, pfin])
            if campos_ok:
                # Intentar convertir los valores numéricos a float
                try:
                    pplant = float(pplant)
                    pconfig = float(pconfig)
                    pini = float(pini)
                    pfin = float(pfin)
                except ValueError:
                    messagebox.showerror(
                        "Error", "Los campos numéricos deben ser números válidos."
                    )
                    return
                # Insertar el nuevo registro en la base de datos
                medicion = Medicion(
                    muestra=muestra,
                    especie=especie,
                    pplant=pplant,
                    pconfig=pconfig,
                    pini=pini,
                    pfin=pfin,
                )

                self.base_de_datos.modificar_medicion(datos[0], medicion)
                messagebox.showinfo("Éxito", "Registro agregado correctamente.")
                ventana_modificar.destroy()
                self.mostrar_registros()
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")

        ventana_modificar = tk.Toplevel(self.root)
        ventana_modificar.title("Modificar Registro")

        etiqueta_muestra = ttk.Label(ventana_modificar, text="Muestra:")
        etiqueta_muestra.pack()
        entrada_muestra = ttk.Entry(ventana_modificar)
        entrada_muestra.pack()

        etiqueta_especie = ttk.Label(ventana_modificar, text="Especie:")
        etiqueta_especie.pack()
        entrada_especie = ttk.Entry(ventana_modificar)
        entrada_especie.pack()

        etiqueta_pplant = ttk.Label(ventana_modificar, text="Pplant:")
        etiqueta_pplant.pack()
        entrada_pplant = ttk.Entry(ventana_modificar)
        entrada_pplant.pack()

        etiqueta_pconfig = ttk.Label(ventana_modificar, text="Pconfig:")
        etiqueta_pconfig.pack()
        entrada_pconfig = ttk.Entry(ventana_modificar)
        entrada_pconfig.pack()

        etiqueta_pini = ttk.Label(ventana_modificar, text="Pini:")
        etiqueta_pini.pack()
        entrada_pini = ttk.Entry(ventana_modificar)
        entrada_pini.pack()

        etiqueta_pfin = ttk.Label(ventana_modificar, text="Pfin:")
        etiqueta_pfin.pack()
        entrada_pfin = ttk.Entry(ventana_modificar)
        entrada_pfin.pack()

        boton_guardar = ttk.Button(
            ventana_modificar, text="Guardar", command=guardar_modificacion
        )
        boton_guardar.pack()

    def eliminar_registro(self):
        # Implementa la lógica para eliminar un registro
        seleccionado = self.tabla.focus()

        if seleccionado:
            if messagebox.askyesno(
                "Confirmar", "¿Está seguro que quiere eliminar este registro?"
            ):
                datos = self.tabla.item(seleccionado)["values"]

                self.base_de_datos.eliminar_medicion(datos[0])

                self.mostrar_registros()
        else:
            messagebox.showwarning(
                "Advertencia", "Seleccione un registro para eliminar."
            )


if __name__ == "__main__":
    bd = BaseDeDatos("BD_neumatron.db")
    bd.crear_tabla()

    root = tk.Tk()
    app = VentanaRegistroMediciones(root, bd)
    root.mainloop()

    bd.cerrar_conexion()
