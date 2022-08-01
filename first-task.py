import hashlib
def get_hash_value(s):
    return hash(s)

def encrypt_string(s):
    crypted = hashlib.blake2b()
    crypted.update(s.encode('utf-8'))
    return crypted.hexdigest()

if __name__ == "__main__":
    print(get_hash_value("Python Bootcamp"))
    print(encrypt_string("Python Bootcamp"))
