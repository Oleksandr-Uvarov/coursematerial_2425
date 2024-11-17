def orbit_chain(orbits, start):
    lst = []

    current = start
    while True:
        if current not in orbits:
            lst.append(current)
            return lst
        else:
            lst.append(current)
            current = orbits[current]
        

        

orbits = {    
        'Moon': 'Earth',
        'Mars': 'Sun',
        'Earth': 'Sun',
        'Jupiter': 'Sun',
        'Saturn': 'Sun',
        'Sun': 'Sagittarius A*',
        'Phobos': 'Mars',
        'Deimos': 'Mars',
        'Titan': 'Saturn',
        'Enceladus': 'Saturn',
        'Hyperion': 'Saturn',
        'Tethys': 'Saturn',
        'Ganymede': 'Jupiter',
        'Callisto': 'Jupiter',
        'Europa': 'Jupiter',
        'Proxima Centauri b': 'Proxima Centauri',
        'Proxima Centauri': 'Sagittarius A*'}

print(orbit_chain(orbits, "Mars"))
print(orbit_chain(orbits, "Sagittarius A*"))