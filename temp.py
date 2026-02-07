import requests

# url = "http://interapis.uz/api/flashcards/flash-cards/"
url = "http://interapis.uz/media/flash_cards_images/test.png"
headers: dict = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcyODg1NzUxLCJpYXQiOjE3NzAyOTM3NTEsImp0aSI6IjkxNzM4ZjZkZjU2YjRmNjZiY2I3MzA5MjI3MmZmMDFhIiwidXNlcl9pZCI6IjEifQ.99XvqbVMDqDPFQDVbIs_8bMiOZTB_8IdfpMxn35PShU",
}
response: requests.Response = requests.get(
    url=url,
    headers=headers,
)
print("Status Code: ", response.status_code)
with open("season.png", "wb") as f:
    f.write(response.content)

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcyODg1NzUxLCJpYXQiOjE3NzAyOTM3NTEsImp0aSI6IjkxNzM4ZjZkZjU2YjRmNjZiY2I3MzA5MjI3MmZmMDFhIiwidXNlcl9pZCI6IjEifQ.99XvqbVMDqDPFQDVbIs_8bMiOZTB_8IdfpMxn35PShU
