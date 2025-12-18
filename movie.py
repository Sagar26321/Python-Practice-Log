# 1. THE DEFINITION (Building the machine)
def get_movie_queue():
    temp_list = []
    while True:
        title = input("Enter movie (or 'exit'): ")
        if title == "exit":
            break
        else:
            temp_list.append(title)
    
    return temp_list # HAND the full list back to the main program

# ------------------------------------------------

# 2. THE CALL (Using the machine)
print("Let's build your Friday night list:")
friday_movies = get_movie_queue()

print("Let's build your Saturday night list:")
saturday_movies = get_movie_queue()

# 3. THE RESULT
print("Friday movies are:", friday_movies)
print("Saturday movies are:", saturday_movies)