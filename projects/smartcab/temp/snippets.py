print "minor {}".format(data['minor_acc'].mean())
print "major {}".format(data['major_acc'].mean())
print "minor v {}".format(data['minor'].mean())
print "major v {}".format(data['major'].mean())

from numpy.linalg import lstsq as approx

filtered = data.loc[(data['testing'] != True) & (data['trial'] >= 10)]
x = filtered['trial'].values
major_acc = filtered['major_acc'].values
minor_acc = filtered['minor_acc'].values
minor = filtered['minor'].values
major = filtered['major'].values

A = np.vstack([x, np.ones(len(x))]).T

mjaa, mjab = approx(A, major_acc)[0]
miaa, miab = approx(A, minor_acc)[0]
mava, mavb = approx(A, major)[0]
miva, mivb = approx(A, minor)[0]

import matplotlib.pyplot as plt
plt.plot(x, major_acc, 'o', color='r', markersize=3)
plt.plot(x, minor_acc, 'o', color='b', markersize=3)
plt.plot(x, major, 'o', color='g', markersize=3)
plt.plot(x, minor, 'o', color='c', markersize=3)
plt.plot(x, mjaa*x + mjab, 'r', label='Major Accidents')
plt.plot(x, miaa*x + miab, 'b', label='Minor Accidents')
plt.plot(x, mava*x + mavb, 'g', label='Major Violations')
plt.plot(x, miva*x + mivb, 'c', label='Minor Violations')
plt.legend()
plt.show()

print mjaa





qtable = pd.read_csv('temp/dataframe.csv')

qtable['waypoint'] = qtable['state'].apply(lambda x: ast.literal_eval(x)['waypoint'])
qtable['light'] = qtable['state'].apply(lambda x: ast.literal_eval(x)['light'])
qtable['li'] = qtable['state'].apply(lambda x: ast.literal_eval(x)['left'])
qtable['oi'] = qtable['state'].apply(lambda x: ast.literal_eval(x)['oncoming'])

qtable = qtable.drop('state', axis=1)

qtable['max'] = qtable[["forward", "left", "right", "none"]].idxmax(axis=1)

red = qtable.loc[qtable['light'] == 'red']
red = red.loc[red['waypoint'] == 'right']
red = red.loc[(red['max'] == 'right') | (red['max'] == 'none')]

green = qtable.loc[qtable['light'] == 'green']

ongoing_locks_left = green.loc[(green['waypoint'] == 'left') & ((green['oi'] == 'forward') | (green['oi'] == 'right'))]

intention_failed = green.loc[green['max'] != green['waypoint']]
ongoing_locks_left_index = intention_failed.index.isin(ongoing_locks_left.index.values)
intention_failed = intention_failed[~ongoing_locks_left_index]

1 - (float((len(qtable) - len(intention_failed))) / float(len(qtable)))

