import random
from db_sql import Conector

class Producto:
    
    def __init__(self, con_imagen, categos, integridad, vendedor,
            tipo, prob_troll, prob_lacra, fecha, dt):
        self.con_imagen = con_imagen
        self.subcategoria_id = categos[0]
        self.subname = categos[1]
        self.catname = categos[2]
        self.tipo = tipo
        self.nombre = self.newNombre()
        self.integridad_id = integridad
        self.vendedor_id = vendedor
        self.estado_id = "1"
        self.descripcion = self.newDescripcion(prob_troll, prob_lacra)
        self.precio = "1"
        self.disponibles = "1"
        self.fecha_registro = fecha
        self.fecha_actualiza = fecha
        self.registro_dt = dt
        self.id = self.sendSQL()
 
    def sendSQL(self):
        return Conector.run_sql("INSERT INTO `productos` (`nombre`, `con_imagen`, `subcategoria_id`, `integridad_id`, `vendedor_id`, `estado_id`, `descripcion`, `precio`, `disponibles`, `fecha_registro`, `fecha_actualiza`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (self.nombre, self.con_imagen, self.subcategoria_id, self.integridad_id, self.vendedor_id, self.estado_id, self.descripcion, self.precio, self.disponibles, self.fecha_registro, self.fecha_actualiza))

    def newNombre(self):
        return "algo"

    def newDescripcion(self, prob_troll, prob_lacra):
        return "..."
