
# Open file and read data
with open('./Local_environment/oscar_no_small.txt', 'r', encoding='UTF-8') as f:
    data = f.read()

print(len(data.split()))
