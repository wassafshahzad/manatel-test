from django.utils.crypto import get_random_string
import string


def generate_unique(length: int) -> str:
    return get_random_string(
        length, allowed_chars=string.ascii_uppercase + string.digits)