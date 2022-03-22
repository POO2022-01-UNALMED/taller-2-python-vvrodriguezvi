class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color



class Auto:
    def _init_(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados


    def cantidadAsientos(self):
        inicio = 0
        for i in range(len(self.asientos)):
          if(type(self.asientos[i]) is Asiento):
              inicio += 1
        return inicio

    def verificarIntegridad(self):
        inicio = 0
        self.asientos = list(filter(None, self.asientos))

        for i in range(len(self.asientos)):
            if(self.asientos[i].registro == self.registo == self.motor.registro):
                inicio += 1

            if(inicio == len(self.asientos)):
                return "Auto original"

            else:
                return "Las piezas no son originales"

class Motor:
    def _init_(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self,tipo):
       if tipo == "electrico" or tipo == "gasolina":
           self.tipo = tipo


