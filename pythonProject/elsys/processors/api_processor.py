import requests

COMMENTS_URL = "https://jsonplaceholder.typicode.com/posts/1/comments"
POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


class ApiProcessor:
    @staticmethod
    def longest_comment():
        data = requests.get(COMMENTS_URL)
        comments = sorted(data.json(), key=lambda d: d['body'], reverse=True)
        return comments[0]

    @staticmethod
    def post_with_longest_title():
        data = requests.get(POSTS_URL)
        posts = sorted(data.json(), key=lambda d: d['title'], reverse=True)
        return posts[0]
