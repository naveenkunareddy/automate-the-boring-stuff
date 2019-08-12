from pathlib import Path

from PIL import Image


def find_folders(root):
    """
    Finds all folders containing more image files that non-image files
    and prints the corresponding absolute paths.

    Images are only considered images if they are at least 500x500 in size

    :param root:
    """
    directories = get_subdirectories(path=root)
    print(f'Searching for photo folders recursively in: "{root}"...\n')

    for directory in directories:
        file_count = len([f for f in directory.iterdir() if f.is_file()])
        images = get_images(path=directory)

        for filename in images:
            image = Image.open(filename)
            width, height = image.size

            if width < 500 or height < 500:
                images.remove(filename)

        image_count = len(images)
        if image_count > file_count - image_count:
            print(directory.resolve())


def get_subdirectories(path):
    """
    Gets list of all subdirectories (including current directory)
    recursively at path

    :param Path path: path to search
    """
    return list(path.rglob('./'))


def get_images(path):
    """
    Gets list of all images within the directory at path

    :param Path path: path to search
    """
    files = []
    patterns = ('*.png', '*.jpg', '*.gif', '*.bmp')
    for pattern in patterns:
        files.extend(path.glob(pattern))

    return files


if __name__ == '__main__':
    find_folders(root=Path('../../..'))
