from post import Post
from post_creator import PostCreator
from time_manager import TimeManager
import json


def get_group_id(filename: str):
    with open(filename, 'r') as json_file:
        file = json.load(json_file)
        return file["group_id"]


def main():
    print("Hi! check Readme.")
    group_id = get_group_id("resources.json")
    post_name = input("Input your post name\n")
    post_number = int(input("Input your post number\n"))
    post_times = []
    print("input post times, format 'year:month:day:hours:minutes'\n")
    for i in range(post_number):
        post_time = input()
        post_time = TimeManager.convert_to_unix_timestamp(post_time)
        post_times.append(post_time)

    post_creator = PostCreator(group_id)
    post = Post.create_post(post_name)
    for post_time in post_times:
        post_creator.publicate_post(post, post_time)


if __name__ == '__main__':
    main()
