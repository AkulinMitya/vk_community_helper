import json

import vk_api


def get_token(filename: str):
    with open(filename, 'r') as json_file:
        file = json.load(json_file)
        return file["token"]


class PostCreator:
    def __init__(self, group_id):
        self.token = get_token("resources.json")
        self.group_id = group_id

    def publicate_post(self, post, time):
        vk_session = vk_api.VkApi(token=self.token)
        vk = vk_session.get_api()

        # Upload photos to VK
        upload = vk_api.VkUpload(vk_session)
        photo_ids = []
        for photo_path in post.photos:
            photo = upload.photo_wall(photos=photo_path)[0]
            photo_ids.append(f"photo{photo['owner_id']}_{photo['id']}")

        # Post the message with photos
        attachments = ",".join(photo_ids)
        vk.wall.post(owner_id=f"-{self.group_id}", message=post.text, attachments=attachments, publish_date=time)

        print("Post successfully published!")
