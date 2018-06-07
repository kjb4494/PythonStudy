
def q_01():
    class PeopleInfo:
        def __init__(self, name, stature):
            self.name = name
            self.stature = stature

        def infoOutput(self):
            print("{} {}".format(self.name, self.stature))

    peopleList = []
    for i in range(5):
        inputInfo = input("[이름 키] 입력: ").split()
        try:
            name = inputInfo[0]
            stature = int(inputInfo[1])
            peopleList.append(PeopleInfo(name, stature))
        except Exception as e:
            print("잘못된 입력: ", e)
            return

    peopleList.sort(key=lambda k: k.stature)

    peopleList[0].infoOutput()
    ifeq = 0
    while peopleList[ifeq].stature == peopleList[ifeq + 1].stature:
        ifeq += 1
        peopleList[ifeq].infoOutput()

def warming_up_output():
    q_01()