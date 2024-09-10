def search_replace(my_list, search, replace):
    # Return a new list where each element is replaced if it matches 'search'
    return [replace if x == search else x for x in my_list]
