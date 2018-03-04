data = []
data.append({'name': 'Immanuel', 'surname': 'Kant', 'sex': 'male', 'age': '12'})
data.append({'name': 'Georg', 'surname': 'Hegel', 'sex': 'male', 'age': '15'})
data.append({'name': 'Lou', 'surname': 'Andreas-Salome', 'sex': 'female', 'age': '13'})
data.append({'name': 'Arthur', 'surname': 'Schopenhauer', 'sex': 'male', 'age': '17'})
data.append({'name': 'Friedrich', 'surname': 'Nietzsche', 'sex': 'male', 'age': '12'})

put = input('Enter value to search:')

def num():
    for i in range(len(data)):
        i+=1
        return i

def output():
    while True:
        for j in data:
            if j['name'] == put or j['sex'] == put:
                return j
            else:
                pass  


print(num(), output())