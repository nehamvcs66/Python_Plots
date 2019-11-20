import matplotlib.pyplot as plt 
#from IPython import get_ipython
  
# x-axis values 
x = [1,2,3,4,5,6,7,8,9,10] 
# y-axis values 
y = [2,4,5,7,6,8,9,11,12,12] 
  
# plotting points as a scatter plot 
plt.scatter(x, y, label= "stars", color= "red",  
            marker= "+", s=30) 
  
# x-axis label 
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('Scatter plot!') 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show()
#get_ipython().run_line_magic('matplotlib', 'qt')