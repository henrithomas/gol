import imageio
filenames = [
    'C:\\Users\\henri\\dev\\gol\\exports\\img\\iter0.jpg',
    'C:\\Users\\henri\\dev\\gol\\exports\\img\\iter1.jpg',
    'C:\\Users\\henri\\dev\\gol\\exports\\img\\iter2.jpg',
    'C:\\Users\\henri\\dev\\gol\\exports\\img\\iter3.jpg',
    'C:\\Users\\henri\\dev\\gol\\exports\\img\\iter4.jpg',
    'C:\\Users\\henri\\dev\\gol\\exports\\img\\iter5.jpg',
    'C:\\Users\\henri\\dev\\gol\\exports\\img\\iter6.jpg',
]
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('C:\\Users\\henri\\dev\\gol\\exports\\movie.gif', images)