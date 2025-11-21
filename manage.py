#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import socket

# Примусово використовуємо IPv4, бо IPv6 викликає Errno 101
original_getaddrinfo = socket.getaddrinfo

def ipv4_only_getaddrinfo(*args, **kwargs):
    # Фільтруємо результати, залишаючи тільки IPv4 (AF_INET)
    responses = original_getaddrinfo(*args, **kwargs)
    return [r for r in responses if r[0] == socket.AF_INET]

socket.getaddrinfo = ipv4_only_getaddrinfo

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SimpleDjangoProjectDziuba.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
