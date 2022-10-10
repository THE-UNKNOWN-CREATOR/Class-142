import csv
all_movies = []
liked = []
disliked = []
not_watched = []

with open("final.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    