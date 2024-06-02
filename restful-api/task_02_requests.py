#!/usr/bin/python3
"""RESTful API"""
import csv
import requests


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print the
        status code and titles of the posts.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder and save them to a CSV file.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()
        posts_data = [{'id': post['id'], 'title': post['title'],
                       'body': post['body']} for post in posts]
        with open('posts.csv', mode='w', newline='') as file:
            write = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            write.writeheader()
            write.writerows(posts_data)
        print("post have been saved to posts.csv")
