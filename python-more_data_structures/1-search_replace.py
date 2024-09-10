def search_replace(my_list, search, replace):
    # Create a new list where each element is replaced if it matches 'search'
    return [replace if element == search else element for element in my_list]
