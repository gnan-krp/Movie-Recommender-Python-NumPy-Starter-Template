def ascii_bar_chart(movie_titles, ratings):
    print("\nMovie Ratings (ASCII Bar Chart):")
    for title, rating in zip(movie_titles, ratings):
        bars = "#" * int(rating*2)
        print(f"{title:25} | {bars} ({rating})")
