# ESCOPO GLOBAL

num = 20
print(num)

def func():
    global num
    num = 50
    print(num)

func()

print(num)
