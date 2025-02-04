# ЗАДАНИЕ ПО ТЕМЕ "Режимы открытия файлов"

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'a+')
        file.seek(0)
        file_content = file.read()
        file.close()
        return file_content

    def add(self, *products):
        for i in range(len(products)):
            list_products = self.get_products()
            if f'{str(products[i])}\n' in list_products:
                print(f'Продукт {str(products[i])} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                string = f'{str(products[i])}\n'
                file.writelines(string)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
