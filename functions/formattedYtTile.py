import re

def formattedYoutubeTitle(title):
    title = re.sub(r'[^\w\s-]', '', title).strip().lower()
    title = re.sub(r'[-\s]+', '-', title)
    return title