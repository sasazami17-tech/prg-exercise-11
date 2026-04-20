def main():
    print("Hello from prg-exercise-11!")


if __name__ == "__main__":
    main()
import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]
values = random_numbers(10)
print(values)

small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

def selection_sort(values):
    values = values[:]
    for pozicia in range(len(values)):
        min = pozicia
        for prechadzanie in range(pozicia + 1, len(values)):
            if values[prechadzanie] < values[min]:
                min = prechadzanie

        values[pozicia], values[min] = values[min], values[pozicia]
    return values


values = [15, 2, 6,7, 13, 0, 22]
print("Povodny zoznam:", values)
print("Zoradeny zoznam:", selection_sort(values))












    # values = values.copy()
    # n = len(values)
    # for i in range(n):
    #     min = i
    #     for k in range(i+1, n):
    #         if values[k] <values[min]:
    #             min = k
    #     values[i], values[min] = values[min], values[i]
    # return values















    #
    #
    #
    # data = [5, 1, 4, 2, 8]
    # print("Původní:", data)
    # print("Seřazený:", selection_sort(data))
    # print("Po zavolání (kontrola):", data)
    # print()
    #
    # print("Náhodný seznam:", rnd)
    # print("Seřazený:", selection_sort(rnd))