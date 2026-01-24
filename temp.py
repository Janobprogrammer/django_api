import requests

# url: str = "http://127.0.0.1:8000/api/accounts/login/"
# response: requests.Response = requests.post(
#     url=url,
#     data={
#         "email": "saidali20010209@gmail.com",
#         "password": "JProCoder2378"
#     }
# )
# print(response.status_code)
# print(response.json().get("access"))

url: str = "http://127.0.0.1:8000/api/accounts/profile/"

headers: dict = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY4NTAwNjU4LCJpYXQiOjE3Njg0OTcwNTgsImp0aSI6IjNhMmQ2Zjk2MDlmYzRkYTA4NDlkZGY5NTAxYzg5ZWUzIiwidXNlcl9pZCI6IjEifQ.ThyNAPEbd0Y743MB_WkNXwpSeu3kwZNxa3sZ-vx_hYE"
}
response: requests.Response = requests.get(
    url=url,
    headers=headers
)

print(response.status_code)
print(response.json())


# YCGMLPO357WX4XO4SM5G3LR4OJ5SHS3T
# NGROK Token