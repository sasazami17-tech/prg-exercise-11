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

def main():
    data = [15, 2, 6,7, 13, 0, 22]
    print("Podovne:", data)
    print("Zoradene:", selection_sort(data))
    print("Spatne zavolanie:", data)
    print()
    nahodne = random_numbers(20)
    print("Nahodny zoznam:", nahodne)
    print("Zoradene:", selection_sort(nahodne))

    if __name__ == "__main__":
        main()
