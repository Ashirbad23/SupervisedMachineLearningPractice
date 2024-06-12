def max_security_value_sum(n, k, arr):
    max_sum = float('-inf')  # Initialize maximum security value sum

    # Iterate through all possible starting nodes
    for i in range(n):
        current_node = i
        security_sum = 0  # Initialize security value sum for current starting node

        # Jump through the network and calculate security value sum
        while current_node < n:
            security_sum += arr[current_node]
            current_node += k

        # Update maximum security value sum if current sum is greater
        if security_sum > max_sum:
            max_sum = security_sum

    return max_sum

# Example usage:
n = 6
k = 2
arr = [3, 5, -2, -4, 16, 2]
optimal_security_sum = max_security_value_sum(n, k, arr)
print("Maximum security value sum:", optimal_security_sum)
