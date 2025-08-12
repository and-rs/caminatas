def create_image_cycler():
    images = [
        # "/static/images/carousel_img_1.avif",
        # TODO: new optimized images
        "/static/images/bg1.png",
        "/static/images/forest.jpg",
        "/static/images/trail.jpg",
        "/static/images/trees.jpg",
    ]
    current_index = 0

    def get_next_image():
        nonlocal current_index
        src = images[current_index]
        current_index = (current_index + 1) % len(images)
        return src

    return get_next_image
