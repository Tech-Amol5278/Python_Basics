# users = {
#     'name': 'Amol',
#     'age' : 24
#     'fav_movies' : ['coco','avengers'],
#     'fav_songs' : ['song1','song2']

# }
# Get the info from user and store in dict and print in above format 

name,age = input("Please enter your name and age in comma separeted : ").split(',')
fav_movies = input('Enter your favourite movies in comma separeted : ').split(',')
fav_songs = input('Enter your favourite songs in comma separeted : ').split(',')

user = {}
user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs

print(user)

for i,j in user.items():
    print(f"{i} : {j}")