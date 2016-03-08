import pymongo

client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet_tab = walden['sheet_tab']

# path = '/home/v5pingan/projectpy/week2/walden.txt'
# with open(path,'r') as f:
#     lines = f.readlines()
#     for index,line in enumerate(lines):
#         data = {
#             'index':index,
#             'line':line,
#             'words':len(line.split())
#         }
#         sheet_tab.insert(data)

#$lt/$lte/$gt/$gte/$ne  依次等价于 </<=/>/>=/!=
for item in sheet_tab.find({'words':{'$lt':5}}):
    print(item)