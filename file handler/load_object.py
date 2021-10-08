import pickle
from person import Person

# 객체 하나
with open('object.bin', 'rb') as f :
    data = pickle.load(f)
print(f'load한 데이터: {data}')

# 리스트 객체
with open('object.bin', 'rb') as f :
    data = pickle.load(f)

for d in data:
    print(d)