"""function to communicate to zfs"""
from socket import create_connection


def get_quota_from_zfs(username, url="storage.internal", port=1995):
    storage_socket = create_connection((url, port), 1)
    storage_socket.send((username + "\n").encode())
    return storage_socket.recv(1024)
