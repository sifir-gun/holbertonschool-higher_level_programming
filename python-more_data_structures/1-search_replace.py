def search_replace(my_list, search, replace):
    # Create a new list with replaced elements if they match 'search'
    new_list = [replace if x == search else x for x in my_list]
    return new_list
