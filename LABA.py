import time

countdown = int(input("Начать обратный отсчет с: "))

while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown -= 1

print("Первая лаба выполнена!")
