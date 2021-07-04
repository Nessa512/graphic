import pandas as pd
from matplotlib import pyplot as ptl

# data = pd.read_csv("data/stars.csv")
# print(pd.DataFrame(data))

lineY = [y for y in range(-100,100,1)]
lineX = [x**8 for x in range(-100,100,1)]

ptl.plot(lineY, lineX)

ptl.show()
