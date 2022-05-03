import requests
import socket


def check_localhost():
    """Checks whether the local host is correctly configured.

    Returns:
        True iff localhost is correctly configured.
    """

    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


def check_connectivity():
    """Checks whether the computer can make successful calls to the internet.

    Returns:
        True iff status_code equals to 200.
    """

    request = requests.get("https://www.google.com")
    return request.status_code == 200


if __name__ == '__main__':
    print(check_localhost())
    print(check_connectivity())
