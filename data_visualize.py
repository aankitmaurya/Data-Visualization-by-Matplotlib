# Data Visualization using matplotlib --source Edureka

# importing library
from matplotlib import pyplot as plt



# plt.plot([1,2,3,4,5,6],[4,5,6,7,8,9])
# plt.show()


# run above 3 lines of code you will see your first graph
# =========================================

# adding titles and lables
# x = [10,25,45,80]
# y = [44,55,66,77]
# plt.plot(x,y)
# plt.title('Graph Heading')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()

# now run the above code


# ==========================================

# adding style to graph

# from matplotlib import style

# style.use('ggplot')

# x = [5,10,15,20,25]
# y = [6,12,18,24,30]

# x1 = [2,4,6,8,10]
# y1 = [4,8,12,16,20]


# plt.plot(x,y,label= 'line one',linewidth= 4)

# plt.plot(x1,y1,label= 'line two',linewidth= 4)

# plt.title('Graph Heading')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')

# plt.legend()

# plt.grid(True, color='k')

# plt.show()



# ============================================
# Bar Graph

# Bar graph is basically used to compare two things these graph are very useful when 
# data changes with the time




# x = [5,10,15,20,25]
# y = [6,12,18,24,30]

# x1 = [2,4,6,8,9]
# y1 = [4,8,12,16,20]


# plt.bar(x,y,label= 'line one', color = 'r')

# plt.bar(x1,y1,label= 'line two', color = 'g')

# plt.title('Graph Heading')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')

# plt.legend()

# plt.show()


# =============================================

# Histogram

# data1 = [5,2,5,4,8,6,2,1,4,8,5,1,15,9,6,2,1,4,8,5,2,4]

# data2 = [0,4,8,12,16]
# # data is the category like how many values are falling in between 0 and 4, then 
# # how many values are falling in between 4 and 8

# plt.hist(data1, data2,histtype='bar', rwidth=0.5)


# plt.title('Histogram Graph Heading')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')

# plt.legend()

# plt.show()

# ===============================================


# Scatter plot


# x = [1,2,3,4,5,6,7,9]
# y = [5,4,6,21,8,24,16,9]

# plt.scatter(x,y, label= 'data points',color = 'r')

# plt.title('Histogram Graph Heading')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')

# plt.legend()

# plt.grid(True, color = 'y')
# plt.show()


# =================================================


slices = [7,2,3,6] 
activities = ['sleeping', 'playing', 'coding', 'music']
colors = ['r','y','g','b']

plt.pie(slices, 
	labels = activities,
	colors= colors,
	startangle = 90,
 	shadow = True,
 	explode=(0,0.1,0,0),
 	autopct= '%1.1f%%',

 	)

plt.title('Plt Plot')
plt.show()