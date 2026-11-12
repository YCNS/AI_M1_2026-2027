import numpy as np
import matplotlib.pyplot as plt

# Data initialization
np.random.seed(101)                                        
grades_of_students = np.random.randint(0, 21, size=(100, 5))  
modules = ['THL', 'DSS', 'DB', 'SE', 'RE']
print("First 5 students:\n", grades_of_students[:5])

 
# Basic statistics
mean_per_student = grades_of_students.mean(axis=1)
mean_per_module = grades_of_students.mean(axis=0)
median_per_module = np.median(grades_of_students, axis=0)
var_per_module = grades_of_students.var(axis=0)
std_per_module = grades_of_students.std(axis=0)
 
print("Mean per student (first 5):", np.round(mean_per_student[:5], 2))
for i, m in enumerate(modules):
    print(f"{m:>3} | mean={mean_per_module[i]:.2f}  median={median_per_module[i]:.1f}  "
          f"var={var_per_module[i]:.2f}  std={std_per_module[i]:.2f}")
 
print("Overall min:", grades_of_students.min(), "| Overall max:", grades_of_students.max())
 
thl = grades_of_students[:, 0]
print("THL percentiles (25, 50, 75):", np.percentile(thl, [25, 50, 75]))


# Boolean mask and filtering
mask_10_15 = (grades_of_students >= 10) & (grades_of_students <= 15)
print("Number of grades in [10, 15]:", mask_10_15.sum())     # True counts as 1
grades_10_15 = grades_of_students[mask_10_15]
print("Extracted grades (first 20):", grades_10_15[:20])

 
# Visualization: bar plot of the module averages
plt.figure(figsize=(7, 4))
plt.bar(modules, mean_per_module, color=['#4C72B0', '#55A868', '#C44E52', '#8172B2', '#CCB974'])
plt.title("Average grade per module")
plt.xlabel("Module")
plt.ylabel("Average grade")
plt.ylim(0, 20)
plt.show()

 
# Visualization: box plot of the distribution per module
plt.figure(figsize=(7, 4))
bp = plt.boxplot(grades_of_students, patch_artist=True)
plt.xticks(range(1, 6), modules)
for patch, color in zip(bp['boxes'], ['#4C72B0', '#55A868', '#C44E52', '#8172B2', '#CCB974']):
    patch.set_facecolor(color)
plt.title("Grade distribution per module")
plt.xlabel("Module")
plt.ylabel("Grade")
plt.show()


# Extra practice
# 1. Students with ALL grades above 15
all_above_15 = np.where((grades_of_students > 15).all(axis=1))[0]
print("Students with all grades > 15 (indices):", all_above_15)

 
# 2. Top 5 students by average grade
top5_idx = np.argsort(mean_per_student)[::-1][:5]
for rank, idx in enumerate(top5_idx, start=1):
    print(f"{rank}. student #{idx} -> average {mean_per_student[idx]:.2f}")
 
# 3. Module with the highest average
best = np.argmax(mean_per_module)
print(f"Best module: {modules[best]} ({mean_per_module[best]:.2f})")