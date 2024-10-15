class Figure:
    sides_count = 0
    filled = False
    #инициализация
    def __init__(self,__color,*__sides):
        self.__color = __color
        self.__sides = __sides

    #вывод цвета фигуры
    def get_color(self):
        return list(self.__color)

    #проверка на правильность цвета
    def __is_valid_color(self,r,g,b):
        if r>255 or g>255 or b>255 :
            return False
        else:
            return True

    #если верный цвет, то меняем его у фигуры
    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color=[r,g,b]

    #вывод сторон фигуры
    def get_sides(self):
        if (len(self.__sides)==1):
            return [self.__sides[0]]
        else:
            return self.__sides

    #вывод длины фигуры (периметр)
    def __len__(self):
            return sum(self.__sides)

    #смена сторон фигуры
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides

#класс КРУГ
class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color)
        #self.set_sides(sides * self.sides_count)
        if len(sides)!=self.sides_count :
            self.set_sides(1)
        else:
            self.set_sides(sides[0])

#класс КУБ
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color)
        if len(sides)==1:
            #arr=tuple(sides[0] for i in range(12))
            #self.set_sides(arr)
            self.set_sides(sides[0],sides[0],sides[0],sides[0],sides[0],sides[0],sides[0],sides[0],sides[0],sides[0],sides[0],sides[0])
        else:
            self.set_sides(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    #рассчмиаем объем куба
    def get_volume(self):
        return self.get_sides()[0]**3

#класс ТРЕУГОЛЬНИК
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color)
        if len(sides) == self.sides_count:
            self.a = sides[0]
            self.b = sides[1]
            self.c = sides[2]
        else:
            self.a=0
            self.b=0
            self.c=0

    #узнать площадь треугольника по 3-м сторонам
    def get_square(self):
        p=(self.a+self.b+self.c)/2
        return round((p*(p-self.a)*(p-self.b)*(p-self.c)) ** 0.5,2)



#arr = (50 for i in range(12))
#print(">>",arr)


#Стандарт
circle1 = Circle((200, 200, 100),10) # (Цвет, стороны) +
cube1 = Cube((222, 35, 130), 6) #создаем куб со сторонами 6
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

#создаем треугольник
t=Triangle((200, 200, 100), 4,2,3)
#считаем площадь по 3м сторонам
print("Площадь треугольника равна: ",t.get_square())