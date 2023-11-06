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

# Check if login was successful (you can modify this based on your needs)
if 'Sign out' in response.text:
    print('Logged in successfully')
else:
    print('Login failed')

# Now you can use the 'session' object to access authenticated pages
