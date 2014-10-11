def draw_array(canvas, array):
    canvas.delete('my_tag')

    for z, n in enumerate(array):
        canvas.create_line(z, 0, z, n, tags="my_tag")
    canvas.update()

