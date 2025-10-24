class Producto:
    def __init__(self, nombre, precio = 0, stock = 0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def consultar_stock(self):
        consulta = int(input("consultar stock: "))
        if self.stock == consulta: 
            return True
        else: 
            return False
          
    def descuento (self, precio):
        precio = precio * 0.15
        return precio

remera = Producto("Remera roja", 10000, 50)

remera.consultar_stock()
        