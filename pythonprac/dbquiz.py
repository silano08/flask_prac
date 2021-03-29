from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#01 매트릭스 평점 가져오기


matrix = db.movies.find_one({'title':'매트릭스'},{'_id':False})
# print(matrix['star'])

#02 매트릭스와 같은 평점 다른 영화 제목들 가져오기

# target_star = matrix['star']
# target_movies = list(db.movies.find({'star':target_star},{'_id':False}))
#
# for tarfet in target_movies:
#     print(tarfet['title'])

#03 매트릭스 영화평점 0으로 만들기

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})