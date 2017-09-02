correlated = {'Milk' : ml, 'Detergents_Paper' : dp, 'Grocery' : gr}
number_of_intervals = 200

intervals_dict = {}

for key, value in correlated.iteritems():
    min_value = min(value)
    max_value = max(value)
    
    delta = max_value - min_value
    interval_size = delta / number_of_intervals
    
    intervals = []
    for i in range(min_value, max_value, 2 * interval_size):
        intervals.append((i, i + interval_size))
    
    intervals_dict[key] = intervals

densities_dict = {}
for key, value in correlated.iteritems():
    intervals = intervals_dict[key]
    density_by_interval = {}
    for v in value:
        for i in intervals:
            if v >= i[0] and v < i[1]:
                if density_by_interval.get(i) != None:
                    density_by_interval[i] = density_by_interval[i] + 1
                else:
                    density_by_interval[i] = 1
                break
    densities = []
    for interval_key in sorted(density_by_interval.iterkeys()):
        densities.append(density_by_interval[interval_key])

    densities_dict[key] = densities


d1 = pca_results.iloc[1,1:]
d2 = pca_results.iloc[2,1:]

print np.dot(d1, d2)

importance = {}
for feature in log_data.keys():
    f = pca_results[feature]
    imp = 0
    for v in f:
        imp += abs(v)
    importance[feature] = imp

print importance


# A function for generating table to answer question 4
def create_table(indicies_dict):
    result = "| index | occurence ||-------|-----------|"
    for key, value in repeated_indicies.iteritems():
        list_as_string = ", ".join(value)
        result += "|{}|{}|".format(key, list_as_string)
    return result

# print create_table(repeated_indicies)




    display(possible_outliers_for_feature)
    indicies[feature] = list(possible_outliers_for_feature.index)
    idc_list.extend(list(possible_outliers_for_feature.index))

print idc_list
    
def calculate_indicies_of_outliers(indicies):
    repeated_indicies = {}
    for key, value in indicies.iteritems():
        for v in value:
            idx_list = repeated_indicies.get(v)
            if idx_list == None:
                repeated_indicies[v] = [key]
            else:
                repeated_indicies[v].append(key)

    repeated_indicies_filtered = {}
    for key, value in repeated_indicies.iteritems():
        if len(value) > 1:
            repeated_indicies_filtered[key] = value

    return repeated_indicies_filtered

repeated_indicies = calculate_indicies_of_outliers(indicies)



    idx = [65, 66, 81, 95, 96, 128, 171, 193, 218, 304, 305, 338, 353, 355, 357, 412, 86, 98, 154, 356, 75, 38, 57, 145, 175, 264, 325, 420, 429, 439, 161, 109, 137, 142, 183, 184, 187, 203, 233, 285, 289, 343]
    idx = sorted(idx)

    for index, row in data.iterrows():
        if index in idx:
            data.drop(data.index[index], inplace=True)
            idx = map(lambda x: x-1, idx)


m = pd.DataFrame([[12000, 5796, 7951, 3071, 2881, 1524]], columns = data.keys())
m.index = ['Mean']
m = m.append(true_centers)
m = m.transpose()
m.plot()




