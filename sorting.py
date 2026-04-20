import random
import matplotlib.pyplot as plt
def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]
values = random_numbers(50, 0, 100)
print(values)

small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

def selection_sort(values):
    values = values[:]
    plt.ion()
    plt.show()
    for pozicia in range(len(values)):
        min = pozicia
        for prechadzanie in range(pozicia + 1, len(values)):
            if values[prechadzanie] < values[min]:
                min = prechadzanie
            index_highlight1 = pozicia
            index_highlight2 = prechadzanie
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

        values[pozicia], values[min] = values[min], values[pozicia]
    return values


values = [15, 2, 6,7, 13, 0, 22]
print("Povodny zoznam:", values)
print("Zoradeny zoznam:", selection_sort(values))




def bubble_sort(values):
    values = values[:]
    plt.ion()
    plt.show()
    for zoradene_od_konca in range(len(values)):
        zmenilo_sa = False
        print(zoradene_od_konca)
        for porovnanie in range(len(values) - 1 - zoradene_od_konca):
            if values[porovnanie] > values[porovnanie - 1]:
                zmenilo_sa = True
                values[porovnanie], values[porovnanie - 1] = values[porovnanie + 1], values[porovnanie]
        if not zmenilo_sa:
            break
    return values
values = random_numbers(20)
print("Povodny zoznam", values)
print("Zoradeny zoznam", bubble_sort(selection_sort(values)))



def main():
    data = [5, 1, 4, 2, 8]
    print("Povodne:", data)
    print("Selection Sort:", selection_sort(data))
    print("Bubble Sort:", bubble_sort(data))
    print("Zavolanie:", data)

    nahodne = random_numbers(20)
    print("Nahodny zoznam:", nahodne)
    print("Selection Sort:", selection_sort(nahodne))
    print("Bubble Sort:", bubble_sort(nahodne))

    if __name__ == "__main__":
        main()
