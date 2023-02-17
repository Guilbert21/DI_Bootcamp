import requests
import time
time.__d
def get_page_load(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    print(f"time to load page{url}: is {load_time} seconds")
    return load_time

get_page_load("http://learn.di-learning.com/courses/collection/18/course/13/section/65/chapter/349#")





