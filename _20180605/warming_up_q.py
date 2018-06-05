
import random

def q_01():
    class ScoreManager:
        def __init__(self, name, math, sci, eng):
            self.name = name
            self.math = math
            self.sci = sci
            self.eng = eng
            self.rank = 0

        def get_total_score(self):
            return self.math + self.sci + self.eng

        def get_average(self):
            return self.get_total_score()/3

    student_list = [ScoreManager('student_' + str(i+1), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) \
                    for i in range(0, 20)]
    student_list.sort(key=lambda x: x.get_total_score())
    eq_count = 0
    for i in range(0, len(student_list)):
        if i != 0:
            if student_list[i].get_total_score() == student_list[i-1].get_total_score():
                eq_count += 1
        student_list[i].rank = i + 1 - eq_count
        print("학생명: {}, 총점: {}, 순위: {}".format(student_list[i].name, student_list[i].get_total_score(), student_list[i].rank))


def warming_up_output():
    q_01()