def get_laboratorium_choices(nazwa_zakladu):
    """
    Return laboratorium choices based on the value of nazwa_zakladu.
    """
    if nazwa_zakladu == 'green':
        return [('z6l1', 'z6l1'), ('z6l2', 'z6l2')]
    elif nazwa_zakladu == 'red':
        return [('z5l1', 'z5l1'), ('z5l2', 'z5l2'), ('z5l3', 'z5l3')]
    else:
        return []