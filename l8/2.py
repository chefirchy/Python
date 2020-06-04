

class Train:
  def __init__(self, destination: str, trainNum: str, dateStart):
    self.destination = destination
    self.trainNum = trainNum
    self.dateStart = dateStart

train = []
train.append(Train('Херсон', '02', dateStart(2019, 8, 30, 18)))
train.append(Train('Будапешт', '08', datetime(2019, 8, 30, 17)))
train.append(Train('Николаев', '04', datetime(2019, 8, 30, 14)))
train.append(Train('Япония', '03', datetime(2019, 8, 30, 22)))
train.append(Train('Степановка', '19', datetime(2019, 8, 30, 18)))


# for i in range(0, 5):
#   print(trains[i].trainNum)
