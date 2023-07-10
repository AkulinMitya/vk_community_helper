import os


class Post:
    def __init__(self, post_name: str, photos: list, text: str):
        self.post_name = post_name
        self.photos = photos
        self.text = text

    @staticmethod
    def create_post(post_name: str) -> 'Post':
        post_folder_path = os.path.join(os.getcwd(), post_name)
        images_folder_path = os.path.join(post_folder_path, 'images')
        text_file_path = os.path.join(post_folder_path, 'text.txt')

        photos = []
        if os.path.exists(images_folder_path) and os.path.isdir(images_folder_path):
            for filename in os.listdir(images_folder_path):
                photo_path = os.path.join(images_folder_path, filename)
                if os.path.isfile(photo_path):
                    photos.append(photo_path)

        text = ''
        if os.path.exists(text_file_path) and os.path.isfile(text_file_path):
            with open(text_file_path, 'r') as file:
                text = file.read()

        return Post(post_name, photos, text)

    def __str__(self) -> str:
        photo_count = len(self.photos)
        return f"Post: {self.post_name}\nPhotos: {photo_count}: {self.photos}\nText: {self.text}"
