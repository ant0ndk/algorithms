# Рита и Гоша играют в игру. 
# У Риты есть n фишек, на каждой из которых написано количество очков. 
# Фишки лежат на столе в порядке неубывания очков на них. 
# Сначала Гоша называет число k, затем Рита должна выбрать две фишки, 
# сумма очков на которых равна заданному числу.
# Рите надоело искать фишки самой, и она решила применить 
# свои навыки программирования для решения этой задачи. 
# Помогите ей написать программу для поиска нужных фишек.

# решение с оптимизированным алгоритмом

n = int(input())
score = list(map(int, input().split()))
k = int(input())

def twosum_with_sort(numbers, X):
    numbers.sort()
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == X:
            return f'{str(numbers[left])} {str(numbers[right])}'
        if current_sum < X:
            left += 1
        else:
            right -= 1
    return None    

print(twosum_with_sort(score, k))