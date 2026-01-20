
def compress_image(input_path, output_path, filesize_threshold=500):
    """Function to compress an image using ffmpeg to a maximum of the specified filesize threshold [kB]. 
    It will compress in multiple stages if necessary to meet the threshold."""

    for image in r"D:\Code\Project_Van_Hool\Media":
        