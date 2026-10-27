# Basic Python Instructions  Execute the following instructions and observe the results.

# Variables 
x = 15 
y = 3.25 
name = "FAI Lab" 
print(x, y, name) 

# Conditional statement 
if x > 5: 
    print(f"{x} is greater than 5")
else: 
    print(f"{x} is less than or equal to 5") 

# Loop 
for i in range(5): 
    print(i) 

# Functions: 
def square(nbr): 
    return nbr * nbr 
print(square(4))


# Using Basic Libraries 

# Numpy
import numpy as np 

# Create a NumPy array 
array = np.array([1, 2, 3, 4, 5]) 
print(array)

# Basic operations with NumPy arrays 
print("Sum:", np.sum(array)) 
print("Mean:", np.mean(array)) 

# Pandas
import pandas as pd 

# Create a simple DataFrame 
data = {'Name': ['Ali', 'Karima', 'Omar'], 
        'Age': [24, 27, 22], 
        'Score': [88, 92, 95]} 
df = pd.DataFrame(data) 
print(df) 

# Access a column 
print(df['Name']) 


#Loading and Visualizing Data 

dflab1 = pd.read_csv('salary_Data.csv') 


print(dflab1.head()) 

import matplotlib.pyplot as plt 

# Simple line plot with Matplotlib 
plt.plot(dflab1['YearsExperience'], dflab1['Salary'], 'o-')   
plt.xlabel('Experience') 
plt.ylabel('Salary') 
plt.title('Experience vs Salary') 
plt.show() 

# Histogram with Matplotlib 
plt.hist(dflab1['YearsExperience'], bins=10, alpha=0.7, color='blue')   
plt.xlabel('Experience') 
plt.ylabel('Frequency') 
plt.title('Experience distribution') 
plt.show()