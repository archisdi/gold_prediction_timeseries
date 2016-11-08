author = "AI research team"

import ANN
import Datahandler as dh
fileTrain = 'DataTrainSMA.xlsx'
atribut, target = dh.generateToSeries(fileTrain, 3)

ANN.train(atribut, target, 5)