print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
def random_set_operations():
    num_set = {random.randint(15, 45) for _ in range(10)}
    count_less_than_30 = sum(1 for num in num_set if num < 30)
    num_set = {num for num in num_set if num <= 35}
    print(f"Random Set: {num_set}")
    print(f"Count of numbers <30: {count_less_than_30}")

random_set_operations()
