from matplotlib import pyplot as plt
'''
#<----LINE PLOT---->
years= [2010,2012,2014,2016,2018]
sales= [10,12,14,6,23]
plt.plot(years,sales)
plt.xlabel("Years")
plt.ylabel("No. of sales")
plt.show()
#<----BAR PLOT--->
years= [2006,2007,2010,2019,2024]
sales= [10,90,30,40,50]
plt.bar(years,sales)
plt.xlabel("Years")
plt.ylabel("No. of sales")
plt.show()
#<---Scatter plot-->
customer=[1011,2033,4333,4555]
amount=[2000,4000,2000,5000]
plt.scatter(customer,amount)
plt.xlabel("Customer id")
plt.ylabel("Amount in bank")
plt.show()
#<----TO MERGE 2 TYPE OF GRAPHS--->
customer=[1011,2033,4333,4555]
amount=[2000,4000,2000,5000]
plt.scatter(customer,amount,marker="*")
plt.plot(customer,amount,linestyle="-")
plt.xlabel("Customer id")
plt.ylabel("Amount in bank")
plt.show()
#<----AREA PLOT--->
x=[1,2,3,4,5]
y1=[54,11,23,89,64]
y2=[33,65,23,12,55]
plt.fill_between(x,y1,y2,color="skyblue",alpha=0.4,label = "Area between 2 dataset")
plt.plot(x,y1,label="Dataset 1")
plt.plot(x,y2,label="Dataset 2")
plt.title("Area Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
'''
#<-----PIE CHART---->
sizes=[35,13,46,23]
labels=['catA','catB','catC','catD']
colors=['yellow','blue','red','green']
plt.pie(sizes,labels=labels,colors=colors)
plt.title("Pie chart Exmaple")
plt.show()
