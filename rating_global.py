import operator

amountpeple = int(input())
users = dict()
# Глобальный рейтинг
for i in range(1, amountpeple + 1):  # создание списка участников(небольшого)
    r = int(input())
    users[i] = r
users = sorted(users.items(), key=operator.itemgetter(1))
for i in range(amountpeple):
    name = input()
    print(i+1, name, users[i])
#Какой-то момент контеста, когда к какому - то человеку прибавились балы за задачу





