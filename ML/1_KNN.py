#Write a KNN program from scratch
'''
Euclidean distance 
Manhattan distance
Minkowski distance
Chebyshev distance
Hamming distance  (dist b/w two binary)
Cosine distance

out steps

step 1 find the dist. of the new unknown value with every other known value
step 2 provide each known value a rank on the basis of the calculated values
step 3 sort the raks in ascending order

classification
higher probability - answer (on the basis of value of k)
'''
#dataset 
# Attributes: [study hrs, attendance%]
X_train = [[2, 60], [3, 65], [4, 70], [6, 80], [7, 85], [8, 90]]
Y_train = ['Fail', 'Fail', 'Fail', 'Pass', 'Pass', 'Pass']

print('Training dataset: \n', X_train, '\n',Y_train)

print('____________________________________________________________\n')
import math

x_new = [5, 80] #new input value

distance = []
 
for i in range(len(X_train)):
    known_studyhrs = X_train[i][0]
    known_attendance = X_train[i][1]

    new_hrs = x_new[0]
    new_attendance = x_new[1]

    Edistance = math.sqrt((known_studyhrs - new_hrs)**2 + (known_attendance - new_attendance)**2)  

    distance.append((Edistance, Y_train[i]))

#to display the calculated euclidean distance
print(f'distance of {x_new} from X_train\n')

for i in range(len(X_train)):
    print(f'{X_train[i]} = {distance[i]}')
    