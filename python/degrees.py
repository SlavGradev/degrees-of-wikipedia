import pywikibot
from collections import deque

site = pywikibot.Site()
start_title = "London"
end_title = "Birmingham"

queue = deque([(pywikibot.Page(site, start_title), 0)])
visited = set()

while(len(queue) != 0):
    page, distance = queue.popleft()

    if page.title() in visited:
        print("{} already visited".format(page.title()))
        continue

    print("visiting {}".format(page.title()))

    visited.add(page.title())
    
    if(page.title() == end_title):
        print("distance is {}".format(distance))
        break
    
    linked_pages = list(page.linkedPages())
    for linked_page in linked_pages:
        queue.append((linked_page, distance + 1))

