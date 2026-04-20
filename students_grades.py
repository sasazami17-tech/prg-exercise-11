import matplotlib.pyplot as plt
class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.get_by_index(index)
        if 90 <= body:
            return "A"
        elif 80 <= body:
            return "B"
        elif 70 <= body:
            return "C"
        elif 60 <= body:
            return "D"
        elif 50 <= body:
            return "E"
        else:
            return "F"

    def find(self, hladany_pocet_bodov):
        result = []
        for i in range(len(self.scores)):
            if self.scores[i] == hladany_pocet_bodov:
                result.append(i)
        return result

    def get_sorted(self):
        scores = self.scores.copy()
        s = len(scores)
        for i in range(s):
            for p in range(0, s - i - 1):
                if scores[p] > scores[p + 1]:
                    scores[p], scores[p + 1] = scores[p + 1], scores[p]

        return scores

    def plot_histogram(self):
        plt.hist(self.scores, bins=15, color="pink", edgecolor="blue")
        plt.xlabel("Body")
        plt.ylabel("Počet študentov")
        plt.title("Histogram výsledkov testu")
        plt.show()
    def find_sorted(self, score):
        if self._sorted_scores is None:
            print("sorting…")
            self._sorted_scores = self.get_sorted()
            u = self._sorted_scores
            vlavo = 0
            vpravo = len(u) - 1

            while vlavo <= vpravo:
                stred = (vlavo + vpravo) // 2

                if u[stred] == score:
                    return stred
                elif u[stred] < score:
                    vlavo = stred + 1
                else:
                    vpravo = stred - 1

            return None
results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

print(results.count())          # 9
print(results.get_by_index(2))  # 91
print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]

print(results.get_grade(2))  # A (91 bodů)
print(results.get_grade(6))  # A (100 bodů)
print(results.get_grade(7))  # F (38 bodů)

print(results.find(100))  # [6]
print(results.find(50))   # [4]
print(results.find(77))

print(results.plot_histogram())
results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

print(results.find_sorted(91))   # sorting…  → index 7
print(results.find_sorted(50))   # → index 2 (už neřadí)
print(results.find_sorted(77))
