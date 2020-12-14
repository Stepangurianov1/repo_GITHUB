second = int(input("введите время в секундах: "))
h = second // 3600
m = (second - h * 3600)//60
s = second - h * 3600 - m * 60
print(f"время: {h:02.00f}:{m:02.00f}:{s:02.00f}.")