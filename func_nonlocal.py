from binary_serch import binary_serch
def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Локальное х сменилось на', x)

func_outer()

my_list = [1, 3, 5, 7, 9]

print(binary_serch(my_list, 5))