
my_color = 'red'
neighbor_color = 'blue'

def color_swapper(color1, color2):
    my_color = 'green'
    neighbor_color = 'pink'
    print(f'My color: {my_color}')
    print(f'Neighbor color: {neighbor_color}')

def global_color_swapper():
    global my_color
    global neighbor_color
    my_color = 'blue'
    neighbor_color = 'yellow'
    print(my_color)
    print(neighbor_color)

color_swapper(my_color, neighbor_color)


global_color_swapper()

