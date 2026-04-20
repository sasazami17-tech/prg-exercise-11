from students_grades import StudentsGrades
def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Počet študentov:", results.count())
    for i in range(results.count()):
        pocet_bodov = results.get_by_index(i)
        znamka = results.get_grade(i)
        print(f"Študent {i}: {pocet_bodov} body – {znamka}")
        print("Študenti so sto bodmi:", results.find(100))
        print("Zoradene vysledky:", results.get_sorted())
        print("Podovne zaznamy:", results.scores)
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    results.plot_histogram()


from sorting import random_numbers

random_results = StudentsGrades(random_numbers(30, 0, 100))
print(random_results.count())
print(random_results.get_sorted())

if __name__ == "__main__":
    main()


