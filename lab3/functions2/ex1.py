movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}]

def first():
    #принимает один фильм и возвращает True, если его рейтинг IMDB выше 5.5
    s = str(input())
    for i in movies:
        if i["name"] == s:
            if i["imdb"] > 5.5:
                return True
            else:
                return False
    return False

def second():
    #возвращает подсписок фильмов с рейтингом IMDB выше 5.5
    a = []
    for i in movies:
        if i["imdb"] > 5.5:
            a.append(i["name"])
    return a

def third():
    #принимает название категории и возвращает только те фильмы, которые относятся к данной категории
    s = str(input())
    a=[]
    for i in movies:
        if i["category"] == s:
            a.append(i["name"])
    return a

def fourth():
    #принимает список фильмов и вычисляет их средний рейтинг IMDB
    k=0.0
    a=input().split(", ")
    for i in a:
        for j in movies:
            if j["name"] == i:
                k+=j["imdb"]
                break
    return k/len(a)

def fifth():
    #принимает категорию и вычисляет средний рейтинг IMDB для фильмов этой категории
    k = 0.0
    m = 0
    s=str(input())
    for i in movies:
        if i["category"] == s:
            k += i["imdb"]
            m += 1
    return k/m


print(first())
print(second())
print(third())
print(fourth())
print(fifth())