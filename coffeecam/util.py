import hashlib


def find_most_logins(user_logins):
    u = list(user_logins.keys())[0]

    if len(u) == 0:
        return '-', '-'

    l = user_logins.get(u)

    for user, logins in user_logins.items():
        if logins > l:
            u = user
            l = logins

    return u, l


def md5(fname):
    hash_md5 = hashlib.md5()
    try:
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except FileNotFoundError:
        return '0'
