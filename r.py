    flat_list = []
    members = dbase.get_members()
    for sublist in members:
        for item in sublist:
            flat_list.append(item)
            return (flat_list