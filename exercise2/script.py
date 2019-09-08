import math
import matplotlib.pyplot as plt

from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

fig, ax = plt.subplots()
ax1 = fig.add_subplot()

class Periodic(object):
        def __init__(self,endTime):
            """ Intializing the constructor
            @param endTime: Total time for plotting
            """

            self.endTime = endTime
            self.h = []
            self.x,self.y = [],[]

        def formula(self):
            """
            Periodic function values are calculated here
            """
            self.h = [3*math.pi*math.exp(-(5*math.sin(2*math.pi*x))) for x in range(self.endTime)]

        def plot(self):
            """
            Live Plotting using matplotlib.
            """
            time = self.endTime
            for t,h in zip(range(time),self.h):
                if t == 0:
                    points, = ax.plot(self.x, self.y, marker='o', linestyle='--')
                    ax.set_xlim(left=0.0,right=time)
                    ax.set_ylim(9.42477796074,9.4247779608)
                else:
                    x_coord,y_coord = t,h
                    print(x_coord,y_coord)
                    self.x.append(x_coord)
                    self.y.append(y_coord)
                    points.set_data(self.x, self.y)
                plt.pause(0.00001)

        def saveFile(self,val):
            """ Storing the data into a file
            @param val: Boolean Value
            """

            if val == True:
                f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".csv")
                h = str(self.h)
                f.write(h)
                print('Data saved')
                f.close()
            else:
                print('Data not saved')

if __name__ == "__main__":
    time = input("Enter the time for plotting")
    run = Periodic(int(time))
    run.formula()
    run.plot()
    store = bool(input("Do you want to save the data? Y/N ?"))
    run.saveFile(store)
