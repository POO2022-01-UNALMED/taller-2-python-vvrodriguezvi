from statistics import mode

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores = ["rojo", "negro", "blanco","verde", "amarillo"]
        
        if color in colores == True:
            self.color = color

class Auto:

    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos #es una lista del objeto Auto
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        contador = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                contador += 1
        return contador

    def verificarIntegridad(self):
        for asiento in self.asientos:
            if asiento:
                if not (asiento.registro == self.motor.registro == self.registro):
                    return "Las piezas no son originales"
        return "Auto original"
         

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tipos = ["electrico", "gasolina"]
        if tipo in tipos == True:
            self.tipo = tipo