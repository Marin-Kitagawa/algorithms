def knapsack(capacity, weights, values, count):
    if count==0 or capacity == 0:
        return 0
    elif weights[count-1] > capacity:
        return knapsack(capacity, weights, values, count-1)
    else:
        remaining_capacity = capacity - weights[count-1]
        newly_added_value = values[count-1] + knapsack(remaining_capacity, weights, values, count-1)
        print(f"New Value: {newly_added_value}")
        without_new_value = knapsack(capacity, weights, values, count-1)
        print(f"Without new value: {without_new_value}")
        return max(newly_added_value, without_new_value)


weights = [10,20,30]
values = [60,100,120]
capcity=50

print(knapsack(capcity, weights, values, 3))
