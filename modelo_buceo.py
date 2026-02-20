import sqlite3
import re


class IngresoD:
    def __init__(self):
        self.conn = sqlite3.connect("buceo.db")
        self.cursor = self.conn.cursor()

    def validar_lugar(self, lugar):
        patron = r"^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
        if not re.match(patron, lugar):
            raise ValueError(
                "el lugar debe ser alfanumerico (nada raro). "
                )

    def crear_tabla(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS inmersiones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                lugar TEXT,
                profundidad REAL,
                tiempo INTEGER,
                observaciones TEXT
            )
            """
        )
        self.conn.commit()

    def alta(self, fecha, lugar, profundidad, tiempo, observaciones):
        self.validar_lugar(lugar)
        self.cursor.execute(
            """
            INSERT INTO inmersiones (
            fecha,
            lugar,
            profundidad,
            tiempo,
            observaciones)
            VALUES (?, ?, ?, ?, ?)
            """,
            (fecha, lugar, profundidad, tiempo, observaciones),
        )
        self.conn.commit()

    def consultar(self, filtro=""):
        if filtro:
            self.cursor.execute(
                "SELECT * FROM inmersiones WHERE lugar LIKE ? OR fecha LIKE ?",
                (f"%{filtro}%", f"%{filtro}%"),
            )
            return self.cursor.fetchall()
        else:
            self.cursor.execute("SELECT * FROM inmersiones")
            return self.cursor.fetchall()

    def modificar(
            self,
            id_inmersion,
            fecha,
            lugar,
            profundidad,
            tiempo,
            observaciones
            ):
        self.validar_lugar(lugar)
        self.cursor.execute(
            """
            UPDATE inmersiones
            SET fecha=?,
            lugar=?,
            profundidad=?,
            tiempo=?,
            observaciones=?
            WHERE id=?
            """,
            (
                fecha,
                lugar,
                profundidad,
                tiempo,
                observaciones,
                id_inmersion
                ),
        )
        self.conn.commit()

    def eliminar(self, id_inmersion):
        self.cursor.execute(
            "DELETE FROM inmersiones WHERE id=?", (id_inmersion,)
            )
        self.conn.commit()

    def cerrar(self):
        self.conn.close()
