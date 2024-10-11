import requests

# Personal Access Token
token = 'YOUR_GITHUB_ACCESS_TOKEN'

# Header dengan token untuk autentikasi
headers = {'Authorization': f'token {token}'}

# Endpoint API GitHub, misalnya untuk mengambil data repositori
url = 'https://api.github.com/repos/USERNAME/REPOSITORY_NAME'

# Mengirim request GET ke API GitHub
response = requests.get(url, headers=headers)

# Mengecek respons dan menampilkan data
if response.status_code == 200:
    data = response.json()
    print(f"Repository Name: {data['name']}")
    print(f"Description: {data['description']}")
    print(f"Stars: {data['stargazers_count']}")
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")
