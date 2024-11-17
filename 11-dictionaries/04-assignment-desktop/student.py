def desktop(catalog, components): 
    total_price = 0
    for component in components:
        total_price += catalog[component]
    
    return total_price