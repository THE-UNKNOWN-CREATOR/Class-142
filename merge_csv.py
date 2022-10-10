import csv

with open("movies.csv") as movie:
    reader = csv.reader(movie)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster_link")

with open("final.csv", "a+") as final:
    writer = csv.writer(final)
    writer.writerow(headers)

with open("movie_links.csv") as link:
    reader = csv.reader(link)
    data = list(reader)
    poster_movies = data[1:]

for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_item for movie_link_item in all_movies_link)

    if poster_found:
        for movie_link_item in all_movies_link:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+") as final:
                        writer = csv.writer(final)
                        writer.writerow(movie_item)