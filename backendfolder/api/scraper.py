import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.freechildrenstories.com/"

def get_story_urls():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Adjust the selector to match the website's structure
    story_links = soup.select('.w-dyn-item a.w-inline-block')
    
    story_urls = [BASE_URL + link['href'] for link in story_links]
    return story_urls

def get_story_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Adjust the selectors to match the website's structure
    title = soup.select_one('.title-class').text.strip()  # Adjust the class name as needed
    content = soup.select_one('.content-class').text.strip()  # Adjust the class name as needed
    
    return {
        'title': title,
        'content': content
    }

def fetch_stories():
    story_urls = get_story_urls()
    stories = []
    for url in story_urls:
        story = get_story_content(url)
        stories.append(story)
    return stories

if __name__ == '__main__':
    stories = fetch_stories()
    for story in stories:
        print(f"Title: {story['title']}")
        print(f"Content: {story['content']}")
        print("\n" + "-"*40 + "\n")
