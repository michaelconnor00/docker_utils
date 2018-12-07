from docker import Client

"""
Back-up all images (not containers) to the file system as tar archives.
Note: delete any images you don't want to back-up first. 
Sequence of Operations:
- clean unreferenced image layers
- get image list
- for each, export to tar
"""

TIMEOUT_HRS = 2
TIMEOUT = 60 * 60 * TIMEOUT_HRS
DKR = Client(timeout=TIMEOUT)

def _image_list():
    return DKR.images(quiet=True)

def _clean_images():
    images = DKR.images(quiet=True, filters={'dangling':True})
    for img in images:
        DKR.remove_image(img)
