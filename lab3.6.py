N = int(input().strip())
sum_of_cards = (N * (N + 1)) // 2
sum_of_found_cards = 0

for i in range(N - 1):
    found_card = int(input().strip())
    sum_of_found_cards += found_card

lost_card = sum_of_cards - sum_of_found_cards
print(lost_card)
