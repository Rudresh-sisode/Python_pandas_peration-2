import pandas
x=pandas.DataFrame({'int_col':[10,20,60,80,-10],'flot_col':[0.1,0.5,0.9,10.9,None],
                    'str_col':['a','b',None,'c','a']})


print(x.ix[:,['flot_col','int_col']])
#the condition is float_col not greater than 0.1
print(x[~(x['flot_col']>0.1)])

#create new data frame and rename int_col into new_name
x1=x.rename(columns={'int_col':'new_name'})
print(x1)

#drop the rows where any values is mising from the dada frame

print(x.dropna())

##11.	Change all the values of str_col with new value and drop the missing values.
#value should have prefix map_ and original value. Eg map_a, map_b
print(x['str_col'].dropna().map(lambda a:'map_'+a))

#group all the values of st_col and fine the mean of float_col in all the
#groups respectively
groupded=x['flot_col'].groupby(x['str_col'])
print(groupded.mean())
