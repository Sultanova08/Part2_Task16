input_ = list(map(int, input("Enter a list element separated by space ").split()))
input_.sort()
for num in list(input_):
    if num % 2 == 0:
        print(num)

