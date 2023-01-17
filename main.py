import redis
import json

red = redis.Redis(
    host='localhost',
    port=6379
)
def namb():
    name = input("Введите имя: ")
    namb = input("Введите номер телефона: ")
    if name and namb:
        red.set(name, json.dumps(namb))
        print("Контакт записан в кэш")
    else:
        print("Ошибка записи")

def delete():
    name = input("Введите имя: ")
    if red.get(name) is not None:
        print(name, " удален")
        red.delete(name)  # удаляются ключи с помощью метода .delete()

while True:
    inquiry = input("set/delete/'name'")
    if inquiry == "set":
        namb()
    elif inquiry =="delete":
        delete()
    else:
        if red.get(inquiry):
            print(json.loads(red.get(inquiry)))
        else:
            print("Нет такого контакта")



# print(red.get('var1'))
# red.delete('var1')  # удаляются ключи с помощью метода .delete()
# print(red.get('dict1'))