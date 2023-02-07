def find_lost_card(n, cards):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(cards)
    return expected_sum - actual_sum

print("N: ")
n = int(input())
cards = [int(input()) for i in range(n - 1)]
print(find_lost_card(n, cards))