import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df= {'food':['meat','banana','avacado','totato'],'calories': [25,130,50,19],'potassium':[40,55,26,20],'fat':[8,2,2,2.5]}
d= pd.DataFrame(df)
x = d['food']
y= d['calories']
y1=d['potassium']


p = np.arange(len(x))
p1=[width+.25 for width in p]
plt.bar(p,y)
plt.bar(p,y1)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
