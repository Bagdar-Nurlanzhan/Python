class StringManipulator:
    def __init__(self, name, age: ):
        self.string = ""  
        # инициализация атрибута для хранения строки

    def getString(self):
        self.string = input("enter a string:")
        # сохраняет в self.string 

    def printString(self):
        print(self.string.upper())

manipulator = StringManipulator()  
# создаём объект класса
manipulator.getString()  
# вводим строку
manipulator.printString()  
# печатаем строку в верхнем регистре
