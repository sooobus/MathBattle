import operator

amountpeple = int(input())
new_users = dict()
# Рейтинг после конца контеста
points = 0
sa = 1#  1 бал за задачу
k = 40 # пока у нас коэффициент повышения для людей меньше тысячи
for i in range(1, amountpeple + 1):  # создание списка участников(небольшого)
    r = int(input())
    new_users[i] = r #К какому - то чуваку прибавили балл за задачу и он должен подняться в рейтинге на какое - то место, используя при этом ЭЛО
    if points == 1:# Применение рейтинга ЭЛО
        if new_users[i-1]< new_users[i]:
            ea = 1/(1 + 10*(new_users[i] - new_users[i-1])/400)
            r2 = r   + k *(sa - ea)
            points = points + 1
            new_users[i]=r2
        else:
            ea = 1 / (1 + 10 * (new_users[i -1] - new_users[i]) / 400)
            r1 = r + k * (sa - ea)
            points = points + 1
            new_users[i-1] = r1
    else:
        points = points + 1
new_users = sorted(new_users.items(), key=operator.itemgetter(1))
print(new_users)
#Затем надо соединить с людьми которые не участвовали в контесте, но это следует...
amountpeple1 = int(input())
users = dict()
# Глобальный рейтинг после контеста
for i in range(1, amountpeple1 + 1):  # создание списка участников(небольшого)
    r = int(input())
    users[i] = r
users = sorted(users.items(), key=operator.itemgetter(1))
a =amountpeple1 + amountpeple
a1 = set()
a1.add(users)
a1.add(new_users)
for i in range(a):
    name = input()
    print(i+1, name, users[i])
    print(new_users[i])# Код мне надо задебажить, он не совсем работает так как надо, я доделаю