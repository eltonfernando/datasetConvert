from dataconvert.database import RepAnnotation, RepImage, RepBoundbox, Boundbox, MetadataImage

def test_insert_annotation_image():
    image_name = "teste2"
    add_img = RepImage()
    add_img.insert(MetadataImage(
        name_image= image_name,
        width=500,
        height= 400,
        channel=3,
        blob = bytearray(b'\xcdasf')
    ))

    repro = RepAnnotation()
    
    repro.insert(image_name)
    result = RepAnnotation()
    print(result.select())

def stest_inset_box():
    name_image = "teste"
    box = Boundbox(
        name_image=name_image,
        label="Elton",
        x_min =2,
        y_min = 6,
        x_max= 20,
        y_max=30,
        confidencie=0.3)

    boundbox = RepBoundbox()
    boundbox.insert(box)
    repro = RepAnnotation()
    repro.insert(name_image=name_image)
