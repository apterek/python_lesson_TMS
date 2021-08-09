
deposit = 2130
deposit_time = 5
annual_percent = 10
bonus = 120

for i in range(deposit_time):
    deposit = deposit + (deposit / annual_percent) + bonus
    
print(deposit)
