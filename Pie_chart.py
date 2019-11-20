import matplotlib.pyplot as plt
  
# defining labels 
activities = ['eat', 'sleep', 'work', 'play'] 
  
# portion covered by each label 
slices = [3, 7, 8, 6] 
  
# color for each label 
colors = ['r', 'y', 'g', 'b'] 
  
# plotting the pie chart 
plt.pie(slices, labels = activities, colors=colors,  
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
        radius = 1.2, autopct = '%1.1f%%') 
  
# plotting legend 
#plt.legend(loc = 'upper right', bbox_to_anchor=(1, 0, 0.5, 1)) 
plt.legend(loc = 'upper right', bbox_to_anchor=(1, 0.5, 0.5, 0.5))
#plt.title("Pie Chart") 
  
# showing the plot 
plt.show() 
