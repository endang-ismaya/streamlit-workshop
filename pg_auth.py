import requests

api_key = "AIzaSyDTL_mQ4dUWEUyt9S0Nhd7NGSr4m-fq9TM"

details = {
    "email": "endang.ismaya@yupanatech.com",
    "password": "endang@3184",
    "returnSecureToken": True,
}

r = requests.post(
    f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}",  # noqa E501
    data=details,
)

print(r.json())
