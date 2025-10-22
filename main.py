class Producto:
    def __init__(self, nombre, precio = 0, stock = 0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def descuento (self, precio):
        precio = precio * 0.15
        return precio


        