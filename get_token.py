import requests

url = "http://interapis.uz/accounts/login"
data: dict[str, str] = {
    "email": "saidali20010209@gmail.com",
    "password": "JProCoder2378",
}

response: requests.Response = requests.post(
    url=url,
    data=data,
)
print(response.status_code)
# print(response.text)
# print(response.json())
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcyODg1NzUxLCJpYXQiOjE3NzAyOTM3NTEsImp0aSI6IjkxNzM4ZjZkZjU2YjRmNjZiY2I3MzA5MjI3MmZmMDFhIiwidXNlcl9pZCI6IjEifQ.99XvqbVMDqDPFQDVbIs_8bMiOZTB_8IdfpMxn35PShU