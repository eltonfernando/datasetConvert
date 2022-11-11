from database import RepAnnotation, RepImage, RepBoundbox, Boundbox

repro = RepAnnotation()
image_name = "test3"
repro.insert(image_name)

box = Boundbox(
    name_image=" test3",
    label="Elton",
    x_min =2,
    y_min = 3,
    x_max= 20,
    y_max=30,
    confidencie=0.3)

boundbox = RepBoundbox()
boundbox.insert(box)
