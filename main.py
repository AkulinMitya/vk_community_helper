from post import Post
from post_creator import PostCreator
from time_manager import TimeManager


def main():
    # podslushano_id = 59053641
    print("Hi! check Readme.")
    group_id = input("Input your group id\n")
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


def test():
    group_id = 59053641
    post_name = "post1"
    post_times = [1689049686, 1689136086]
    post_creator = PostCreator(group_id)
    post = Post.create_post(post_name)
    for post_time in post_times:
        post_creator.publicate_post(post, post_time)


if __name__ == '__main__':
    main()
    # test()
