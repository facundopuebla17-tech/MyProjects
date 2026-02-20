import modelo_buceo
import vista_buceo
from controlador_buceo import Utilidades

if __name__ == "__main__":
    buceo = modelo_buceo.IngresoD()
    buceo.crear_tabla()
    bitacora = Utilidades(buceo)
    vista_buceo.crear_vista(bitacora)
