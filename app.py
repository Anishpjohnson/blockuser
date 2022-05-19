import requests
from dotenv import dotenv_values
config = dotenv_values(".env")


user_id = "auth0|62742bd22d92360069f0a8cb"


def access_token_generation():
    """
    # Get an auth token
    """
    try:
        response = requests.post(
            f"https://{config['AUTH0_DOMAIN']}/oauth/token",
            headers={'content-type': 'application/x-www-form-urlencoded'},
            data={'grant_type': 'client_credentials', 'client_secret': config['AUTH0_CLIENT_SECRET'],
                  'client_id': config['AUTH0_CLIENT_ID'], 'audience': f"https://{config['AUTH0_DOMAIN']}/api/v2/"},
            files=[]
        )
        print(response)
        if response.status_code != 200 or not response.json().get('access_token'):
            print(response.json())
            return False
        return response.json().get('access_token')
    except Exception as e:
        print(e)
        return False


def block_user(user_id: str, access_token: str):
    response = requests.patch(
        f"https://{config['AUTH0_DOMAIN']}/api/v2/users/{user_id}",
        headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'},
        json={'blocked': True}
    )
    print(response)
    if response.status_code != 200:
        print(f'Error occurred while blocking the user {user_id} {response.json()}')
    else:
        return True
    return False


def main():
    # get the access token
    access_token = access_token_generation()
    if not access_token:
        return False
    # TODO: read excel file
    # TODO: get userId from email
    block_user(user_id, access_token)


main()