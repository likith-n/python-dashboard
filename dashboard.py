from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#4C2A85", "#EAB8E4", "#F2C94C", "#F2994A", "#56CCF2", "#BB6BD9"])



x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
xx,yy = np.meshgrid(x,y)
z = xx**2 + yy**2
fig1 = plt.figure(figsize=(4,4))

ax = plt.subplot(projection='3d')
ax.set_title('3D Elliptic Paraboloid.')
p = ax.plot_surface(xx,yy,z,cmap='viridis')




x = [2,4,5,7,9]
y = [6,0,3,2,1]
z = [2,7,3,1,8]
fig2 = plt.figure(figsize=(4,4))
ax = plt.subplot(projection='3d')
ax.scatter3D(x,y,z,s=[100,100,100,100,100])
ax.set_title('3D Scatter Plot')
ax.plot3D(x,y,z,color='red')


x = np.linspace(-10,20,100)
y = np.linspace(-10,20,100)
xx,yy = np.meshgrid(x,y)
z= xx**3 - 3*xx*yy**2
fig5 = plt.figure(figsize=(5,5))

ax = plt.subplot(projection='3d')
ax.set_title('Monkey Saddle')
p = ax.plot_surface(xx,yy,z,cmap='viridis')



batters = pd.read_csv('batter.csv')
df = batters.head()
fig3, ax = plt.subplots(figsize=(5,5))
ax.scatter(batters['avg'],batters['strike_rate'])
ax.set_title('Batsman Performance')
ax.set_xlabel('Avg')
ax.set_ylabel('Strike Rate')

bats = pd.read_csv('batsman_record.csv')
fig4, ax = plt.subplots(figsize=(10,8))
ax.bar(bats['batsman'],bats['2015'],label='2015')
ax.bar(bats['batsman'],bats['2016'],bottom=bats['2015'],label='2016')
ax.bar(bats['batsman'],bats['2017'],bottom=bats['2015']+bats['2016'],label='2017')
ax.set_title('IPL Top Performance')
ax.legend()

root = Tk()
root.title("Dashboard")
root.state('zoomed')
root.config(bg='white')

side_frame = Frame(root, bg='#4C2A85', width=200)
side_frame.pack(side=LEFT, fill=Y)
label = Label(side_frame, text="Dashboard", font=25, bg='#4C2A85', fg='white')
label.pack(pady=20, padx=20)

charts_frame = Frame(root, bg='white')
charts_frame.pack(side=LEFT, fill=BOTH, expand=True)

upper_frame = Frame(charts_frame, bg='white')
upper_frame.pack(fill="both", expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=True)

canvas2 = FigureCanvasTkAgg(fig5, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=True)


lower_frame = Frame(charts_frame, bg='white')
lower_frame.pack(fill="both", expand=True)

canvas3 = FigureCanvasTkAgg(fig3, lower_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=True)

canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=True)

root.mainloop()