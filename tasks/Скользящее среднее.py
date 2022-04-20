# Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
# Измерения велись n секунд.
# В секунду i поступает qi запросов.
# Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.


n = int(input())
q = list(map(int, input().split()))
k = int(input())

result = []
current_sum = sum( q[0:k] )
result.append(current_sum / k)
for i in range(0, len(q) - k):
    current_sum -= q[i]
    current_sum += q[i + k]
    result.append(current_sum / k)

print(*result)