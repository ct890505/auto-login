import requests

# Trang web đích
login_url = 'https://thucongvu.kontum.gov.vn/'

# Github credentials
username = "vthai.stnmt"
password = "Vnpt@123"

# Create a session
session = requests.Session()

# Send a GET request to the login page to get the authenticity token
response = session.get(login_url)

# Check if "authenticity_token" exists in the response text
if 'name="authenticity_token" value="' in response.text:
    authenticity_token = response.text.split('name="authenticity_token" value="')[1].split('"')[0]

    # Prepare login data
    login_data = {
        'commit': 'Sign in',
        'authenticity_token': authenticity_token,
        'login': username,
        'password': password
    }

    # Send a POST request to log in
    response = session.post(login_url, data=login_data)

    print (response.text)
    # Check if login was successful (you can modify this based on your needs)
#     if 'thu' in response.text:
#         print('Logged in successfully')
#     else:
#         print('Login failed')
# else:
    print('Authenticity token not found in the response')
