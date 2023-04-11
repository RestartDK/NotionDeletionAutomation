# todo_done_auto.py
# This program will automatically clear the completed tasks from the todo list in
# Get Shit Done page
import requests
from datetime import datetime, timezone
import json

NOTION_TOKEN = "ENTER NOTION API TOKEN"
DATABASE_ID = "ENTER NOTION PAGE ID"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "content-type": "application/json",
    "Notion-Version": "2022-06-28",
}


def getPages(num_pages = None):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    # If the user does not indicate a larger num of pages, use 100
    standard = num_pages is None
    # Otherwise, use the indicated number of pages
    page_size = 100 if standard else num_pages

    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    with open('db.json', 'w', encoding='utf8') as f:
        # Rewind the JSON file
        f.seek(0)   
        # Dump the data onto the JSON file
        json.dump(data, f, ensure_ascii=False, indent=4)
        # Method for code to work if new data is smaller
        f.truncate()

    results = data["results"]
    # Default API call does only 100 pages, if more, keep iterating
    # through database storing results in JSON file until requested
    # number of pages has been reached
    while data["has_more"] and standard:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])

    return results


def getDonePages(pages):
    done = []

    # Searching through the JSON file if a task is done, store it in array
    for page in pages:
        page_id = page["id"]
        props = page["properties"]
        checkbox = props["Done"]["checkbox"]

        if checkbox == True:
            done.append(page_id)

    return done


def deletePage(page_id: str):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"archived": True}

    res = requests.patch(url, json=payload, headers=headers)
    return res.status_code

def main():
    pages = getPages()
    done_pages = getDonePages(pages)

    for page_id in done_pages:
        deletePage(page_id)


if __name__ == "__main__":
    main()
