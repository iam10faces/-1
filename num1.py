#Объявление стартовых значений
x = []
func = 42
#Подсчет количества строк в файле
with open('num1.txt', 'r') as f:
    ln_count = 0
    for line in f:
        ln_count += 1
#Начало работы со значениями в файле
with open('num1.txt', 'r') as file:
    for i in range(ln_count):
        #buff - буферная переменная
        buff = int(file.readline())
        x.append(buff)
#Подсчет функции
for i in range(len(x)):
    #num - одно из значений x
    num = x[i]
    func = func+1/num
#Вывод функции
print(func)
