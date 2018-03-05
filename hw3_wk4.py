data = [{'name': 'Immanuel', 'surname': 'Kant', 'sex': 'male', 'age': '12'},
{'name': 'Georg', 'surname': 'Hegel', 'sex': 'male', 'age': '15'},
{'name': 'Lou', 'surname': 'Andreas-Salome', 'sex': 'female', 'age': '13'},
{'name': 'Arthur', 'surname': 'Schopenhauer', 'sex': 'male', 'age': '17'},
{'name': 'Friedrich', 'surname': 'Nietzsche', 'sex': 'male', 'age': '12'}]

put = input('Enter value to search:')
num=list(enumerate(data, start=1))

for j in data:
    if j['name'] == put or j['sex'] == put:
        j
     print(j)
