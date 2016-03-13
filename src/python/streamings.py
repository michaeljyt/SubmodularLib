import sys
import matplotlib.pyplot as plt
import numpy as np
import StringIO 
import draw



ks =  [100, 150, 200, 250, 300, 350, 400, 450]

labels = ['SieveStream', 'CircuitStream', 'Offline', 'RandomSampling', 'RandomStream', ]

values = {}
values[labels[0]] = [33601., 48725, 57905, 64355, 74824, 79379, 84410, 88732]
values[labels[1]] = [18008., 26612, 33035, 39177, 44351, 46887, 50954, 53965]
values[labels[2]] = [30280., 45364, 55316, 60663, 65222, 74446, 78696, 82555]
values[labels[3]] = [
    [18765.0, 19464.0, 19493.0, 19263.0, 17760.0, 21972.0, 20154.0, 19831.0, 19629.0, 20090.0],
    [26005.0, 26236.0, 26403.0, 27273.0, 29661.0, 25711.0, 28252.0, 27933.0, 25588.0, 25353.0],
    [35218.0, 34776.0, 34498.0, 36166.0, 33154.0, 35028.0, 36362.0, 34896.0, 32552.0, 32187.0],
    [42308.0, 41305.0, 43788.0, 40623.0, 41551.0, 41478.0, 42685.0, 40580.0, 42168.0, 42159.0],
    [47617.0, 48434.0, 46224.0, 46117.0, 47353.0, 46852.0, 46700.0, 45557.0, 46647.0, 43427.0],
    [52697.0, 51385.0, 53580.0, 55033.0, 53753.0, 52659.0, 53099.0, 52918.0, 51634.0, 54501.0],
    [61817.0, 59653.0, 58224.0, 57376.0, 60684.0, 56571.0, 59274.0, 59700.0, 59528.0, 59120.0],
    [62291.0, 60777.0, 63579.0, 63523.0, 61476.0, 64692.0, 62214.0, 63217.0, 64131.0, 63362.0]
]

values[labels[4]] = [
    [32298.0, 32298.0, 32298.0, 32298.0, 32298.0, 32298.0, 32298.0, 32298.0, 32298.0, 32298.0],
    [46991.0, 46991.0, 46991.0, 46991.0, 46991.0, 46991.0, 46991.0, 46991.0, 46991.0, 46991.0],
    [54865.0, 54753.0, 55205.0, 54765.0, 54848.0, 54856.0, 54868.0, 54856.0, 55034.0, 54874.0],
    [61132.0, 61040.0, 61059.0, 61022.0, 61040.0, 60889.0, 60877.0, 61059.0, 61040.0, 61040.0],
    [70200.0, 70440.0, 69966.0, 70183.0, 70490.0, 70400.0, 70038.0, 70216.0, 70423.0, 70328.0],
    [79718.0, 79090.0, 79401.0, 79561.0, 79718.0, 79529.0, 79344.0, 79529.0, 79684.0, 79731.0],
    [83669.0, 83906.0, 83868.0, 83689.0, 83785.0, 83856.0, 83847.0, 83771.0, 83821.0, 83512.0],
    [88130.0, 87921.0, 88277.0, 88034.0, 87997.0, 88301.0, 88348.0, 88301.0, 88185.0, 88244.0]
]





# draw the graph
styles = ['g-x', 'k-x', 'y-o', 'r-^', 'b-s']

#legend.get_frame().set_facecolor('#00FFCC')



ylabel = r'f(S) - value of function'
xlabel = r'k - cardinality constraint'
draw.draw_errorbar(ks, values, labels, styles, xlabel, ylabel)

