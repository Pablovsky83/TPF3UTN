import sqlite3


class BaseDeDatos:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd
        self.conexion = sqlite3.connect(self.nombre_bd)
        self.c = self.conexion.cursor()

    def crear_tabla(self):
        # Crear la tabla mediciones si no existe
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS mediciones (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Muestra TEXT,
                        Especie TEXT,
                        Pplant REAL,
                        Pconfig REAL,
                        Pini REAL,
                        Pfin REAL
                    )"""
        )
        self.conexion.commit()

    def agregar_medicion(self, medicion):
        # Agregar un registro de medición a la base de datos
        try:
            self.c.execute(
                "INSERT INTO mediciones (Muestra, Especie, Pplant, Pconfig, Pini, Pfin) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    medicion.muestra,
                    medicion.especie,
                    medicion.pplant,
                    medicion.pconfig,
                    medicion.pini,
                    medicion.pfin,
                ),
            )
            self.conexion.commit()
        except Exception as e:
            print(f"Error {e}")

    def modificar_medicion(self, id_registro, medicion):
        # Modificar un registro de medición en la base de datos
        self.c.execute(
            """UPDATE mediciones SET
                        Muestra = ?,
                        Especie = ?,
                        Pplant = ?,
                        Pconfig = ?,
                        Pini = ?,
                        Pfin = ?
                    WHERE ID = ?""",
            (
                medicion.muestra,
                medicion.especie,
                medicion.pplant,
                medicion.pconfig,
                medicion.pini,
                medicion.pfin,
                id_registro,
            ),
        )
        self.conexion.commit()

    def eliminar_medicion(self, id_registro):
        # Eliminar un registro de medición de la base de datos
        self.c.execute("DELETE FROM mediciones WHERE ID = ?", (id_registro,))
        self.conexion.commit()

    def obtener_mediciones(self):
        # Obtener todos los registros de mediciones de la base de datos
        self.c.execute("SELECT * FROM mediciones")
        return self.c.fetchall()

    def cerrar_conexion(self):
        self.conexion.close()
