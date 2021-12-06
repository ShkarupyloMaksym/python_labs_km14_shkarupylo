import json

with open('image_info_test2017\\annotations\\image_info_test-dev2017.json') as f:
    data = json.load(f)

print('1)Number of images: {}'.format(len(data['images'])))

# set was added to avoid repeating if it be (but in this variant we having them), because I don`t know can file have
# difference names of categories
print('2)Number of categories: {}'.format(len(set([i['name'] for i in data['categories']]))))

first = [i for i in data['images'] if i['file_name'] == ('1.jpg'.zfill(16))][0]
print('3)', end='')
end = ', '
for i in 'coco_url', "height", "width", "id":
    if i == 'id':
        end = '\n'
    print('{}: {}'.format(i, first[i]), end=end)

max_id = max([i['id'] for i in data['images']])
name_max_id = '{}.jpg'.format(max_id).zfill(16)
print("4)Name of photo with max 'id'{}".format(name_max_id))
