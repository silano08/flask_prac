from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert / find / update / delete
#
# doc = {'name':'jane','age':21}
# # db안에 users라는 콜렉션에 insert
# db.users.insert_one(doc)

# same_ages = list(db.users.find({},{'_id':False}))
#
# for person in same_ages:
#     print(person)

# user = db.users.find_one({'name':'bobby'},{'_id':False})
# print(user)

# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

db.users.delete_one({'name':'bobby'})


# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})