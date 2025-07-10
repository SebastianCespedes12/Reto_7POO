# Reto_7POO

>Add the proper data structure to manage multiple orders (maybe a FIFO queue)
```python
class Fifo:
    def __init__(self):
        self.ordenes = []
    
    def encolar(self, orden: Order):
        return self.ordenes.append(orden)
    
    def desencolar(self):
        return self.ordenes.pop(0)

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
```
>Define a named tuple somewhere in the menu, e.g. to define a set of items.
```python
from collections import namedtuple
Resumen = namedtuple("Resumen", ["items", "precio"])
class Order:
...

    def generar_resumen(self):
        nombre_orden = f"{[str(i) for i in self.orden]}"
        precio_total = self.calcular_precio_total()
        return Resumen(nombre_orden, precio_total)

tupla = orden1.generar_resumen()
print(f"items{tupla.items}")
print(f"Precio: {tupla.precio}")

```
>Create an interface in the order class, to create a new menu, aggregate the functions for add, update, delete items. All the menus should be stored as JSON files. (use dicts for this task.)
```python

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
orden = Order()
orden.crear_menu("menu_restaurante")

orden.anadir_menu("menu_restaurante", "beverages", "Coca-Cola", {
    "price": 0, "sizes": ["small", "medium", "large"]
})

orden.anadir_menu("menu_restaurante", "main_courses", "Pollo Asado", {
    "price": 10000, "rice": True, "salad": False
})

orden.actualizar_menu("menu_restaurante", "beverages", "Coca-Cola", {
    "price": 1000, "sizes": ["small", "medium", "large"]
})

orden.eliminar_menu("menu_restaurante", "beverages", "Coca-Cola")
```
