from collections import namedtuple
from json import dump, load
import os

Resumen = namedtuple("Resumen", ["items", "precio"])

class MenuItem:
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price
    def calcuar_precio_total(self, items):
        total = 0
        for i in items:
            Total += i.price
        return total
    def __str__(self):
        return self.name


class Beverage(MenuItem):
    def __init__(self, name, price, size:str):
        super().__init__(name, price)
        self.size = size
        if size == "small":
            self.price = 1500
        elif size == "medium":
            self.price = 2000
        else:
            self.price = 3000
           

class MainCourse(MenuItem):
    def __init__(self, name , price, rice:bool, salad:bool):
        super().__init__(name, price)
        self.rice = rice
        self.salad = salad
        if rice == True:
            self.price += 2000
        if salad == True:
            self.price += 1500

class Apetizer(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.price = price

class Dessert(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.price = price
   
class Order:
    def __init__(self):
        self.orden = []

    def anadir_orden(self, item: MenuItem):
        self.orden.append(item)

    def calcular_precio_total(self):
        total = 0
        for i in self.orden:
            total += i.price
        return total
    
    def mostrar_orden(self):
        for i in self.orden:
            print(f"{i.name} - {i.price}")
        print(f"Total: {self.calcular_precio_total()}")

    def generar_resumen(self):
        nombre_orden = f"{[str(i) for i in self.orden]}"
        precio_total = self.calcular_precio_total()
        return Resumen(nombre_orden, precio_total)

    def crear_menu(self, menu_name):
        menu_data = {
            "beverages": {},
            "main_courses": {},
            "appetizers": {},
            "desserts": {}
        }
        filename = f"{menu_name}.json"
        with open(filename, 'w') as f:
            dump(menu_data, f, indent=2)
        return filename

    def anadir_menu(self, menu_name, item_type, item_name, item_data):
        filename = f"{menu_name}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                menu_data = load(f)
        else:
            menu_data = {
                "beverages": {},
                "main_courses": {},
                "appetizers": {},
                "desserts": {}
            }
        
        menu_data[item_type][item_name] = item_data
        
        with open(filename, 'w') as f:
            dump(menu_data, f, indent=2)
    
    def eliminar_menu(self, menu_name, item_type, item_name):
        filename = f"{menu_name}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                menu_data = load(f)
            
            if item_type in menu_data and item_name in menu_data[item_type]:
                del menu_data[item_type][item_name]
                
                with open(filename, 'w') as f:
                    dump(menu_data, f, indent=2)

    def actualizar_menu(self, menu_name, item_type, item_name, item_data):
        filename = f"{menu_name}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                menu_data = load(f)
            
            if item_type in menu_data:
                menu_data[item_type][item_name] = item_data
                
                with open(filename, 'w') as f:
                    dump(menu_data, f, indent=2)
    
    def cargar_menu(self, menu_name):
        filename = f"{menu_name}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return load(f)
        return None



    def __str__(self):
        items = []
        for i in range(len(self.orden)):
            items.append(str(self.orden[i]))
        return f"Orden: {items}"

class Fifo:
    def __init__(self):
        self.ordenes = []
    
    def encolar(self, orden: Order):
        return self.ordenes.append(orden)
    
    def desencolar(self):
        return self.ordenes.pop(0)



if __name__ == "__main__":
    ordenes = Fifo()
    orden1 = Order()
    orden1.anadir_orden(Beverage("Coca-Cola", 0, "small"))
    orden1.anadir_orden(MainCourse("Pollo Asado", 10000, rice=True, salad=False))
    orden1.anadir_orden(Apetizer("Empanada", 2500))
    orden1.anadir_orden(Dessert("Helado", 3000))
    ordenes.encolar(orden1)
    orden2 = Order()
    orden2.anadir_orden(MainCourse("Carne Encebollada", 12000, rice=True, salad=True))
    orden2.anadir_orden(Dessert("Torta de chocolate", 3500))
    ordenes.encolar(orden2)
    orden3 = Order()
    orden3.anadir_orden(MainCourse("Pescado frito", 11000, rice=False, salad=True))
    orden3.anadir_orden(Apetizer("Patacón", 2000))
    orden3.anadir_orden(Beverage("Coca-Cola", 0, "medium"))
    orden3.anadir_orden(Beverage("Coca-Cola", 0, "large"))
    ordenes.encolar(orden3)    

    
    for i in range(len(ordenes.ordenes)):
        print(ordenes.desencolar())
    
    tupla = orden1.generar_resumen()
    print(f"items{tupla.items}")
    print(f"Precio: {tupla.precio}")

    orden = Order()
    orden.crear_menu("menu_restaurante")

    # Add items to menu
    orden.anadir_menu("menu_restaurante", "beverages", "Coca-Cola", {
        "price": 0, "sizes": ["small", "medium", "large"]
    })

    orden.anadir_menu("menu_restaurante", "main_courses", "Pollo Asado", {
        "price": 10000, "rice": True, "salad": False
    })

    # Update an item
    orden.actualizar_menu("menu_restaurante", "beverages", "Coca-Cola", {
        "price": 1000, "sizes": ["small", "medium", "large"]
    })

    # Remove an item
    orden.eliminar_menu("menu_restaurante", "beverages", "Coca-Cola")

    # Load menu data
    menu_data = orden.cargar_menu("menu_restaurante")
    print("Menu data:", menu_data)
