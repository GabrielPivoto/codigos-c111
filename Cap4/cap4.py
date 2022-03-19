import numpy as np

arr = np.loadtxt('space.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')


#Exercise 1
mission_report = arr[1:,7] #Saving the last column in one array
successful_missions = len(mission_report[np.char.find(mission_report,'Success') == 0]) #Number of missions that went sucessfully

print('Percentage of missions that went successfully: {:.2f}%'.format(successful_missions/len(mission_report)*100))
print("")

#Exercise 2
costs = arr[1:,6].astype(float) #Saving all the costs in one array
print('Average costs based on available values: {:.2f}'.format(sum(costs[costs>0])/len(costs[costs>0])))
print("")

#Exercise 3
countries = arr[1:,2]
usa = np.char.find(countries,'USA') > 0
print('Total of missions realized by the USA: {}'.format(len(countries[usa])))
print("")

#Exercise 4
companies,costs = arr[1:,1],arr[1:,6].astype(float)
condition = np.where(companies == 'SpaceX')
print('Most expensive mission realized by SpaceX: {:.2f}'.format(max(costs[condition])))
print("")

#Exercise 5
(a,b) = np.unique(companies, return_counts = True)
for i in range(len(a)):
    print('Company: {}, number of missions: {}'.format(a[i],b[i]))