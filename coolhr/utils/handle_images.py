import os
import os
import secrets
from coolhr import app
from PIL import Image


def save_images(form_image, imageto_replace):
    # delete former image if it exists in the directory and filename is not None from db
    if imageto_replace:
        imageto_replace_path = os.path.join(
            app.root_path, "static", "profile_images", "avatars", imageto_replace
        )
        if os.path.exists(imageto_replace_path):
            os.remove(imageto_replace_path)

    # upload new image
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = random_hex + f_ext
    image_path = os.path.join(
        app.root_path, "static", "profile_images", "avatars", image_fn
    )
    output_size = (600, 600)
    i = Image.open(form_image)
    i.thumbnail(output_size)
    i.save(image_path)
    return image_fn
