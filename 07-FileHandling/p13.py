movie_titles = ["apple movie", "banana movie", "cranbery movie", "de movie", "early movie"]

file = open("movies.txt", "w")
for title in movie_titles:
    file.write(f"{title}\n")
file.close()