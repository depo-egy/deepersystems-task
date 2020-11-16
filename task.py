import json 

f = open('source_file_2.json',)

data = json.load(f)

data_sorted  = sorted(data, key = lambda i: i['priority'])
first = data[0]

managers = []
for i in range(len(data_sorted)):
    managers.append(data_sorted[i]['managers'])
name = []
for i in range(len(data_sorted)):
    name.append(data_sorted[i]['name'])

manList = [ item for elem in managers for item in elem]

def unique(list1):  
    unique_list = []  
    for x in list1:  
        if x not in unique_list: 
            unique_list.append(x)  
    return(unique_list)

manLista = unique(manList)





name_list = []
for j in manLista:
			  name_list.append([data_sorted[i]['name'] for i in range(len(data_sorted)) if j in data_sorted[i]['managers']])

managers_list = {manLista[i]: name_list[i] for i in range(len(manLista))}

with open('managers.json', 'w') as outfile:
    json.dump(managers_list, outfile)
         
###############################################################
watchers = []
for i in range(len(data_sorted)):
    watchers.append(data_sorted[i]['watchers'])
names = []
for i in range(len(data_sorted)):
    names.append(data_sorted[i]['name'])

watList = [ item for elem in watchers for item in elem]

watLista = unique(watList)

names_list = []
for j in watLista:
			  names_list.append([data_sorted[i]['name'] for i in range(len(data_sorted)) if j in data_sorted[i]['watchers']])

watchers_list = {watLista[i]: name_list[i] for i in range(len(watLista))}

with open('watchers.json', 'w') as outfile:
    json.dump(watchers_list, outfile)			  
