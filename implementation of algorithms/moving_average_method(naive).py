def moving_average(timeseries, K):
    result = []  # Пустой список.
    for begin_index in range(0, len(timeseries) - K):
        end_index = begin_index + K
        # Просматриваем окно шириной K.
        current_sum = 0
        for v in timeseries[begin_index:end_index]:
            current_sum += v
        current_avg = current_sum / K
        result.append(current_avg)
    return result 