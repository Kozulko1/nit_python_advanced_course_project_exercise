
print("""
Kontam da je bolje da je klasa odvojena stvar
""")

from hash_module import hash_password, check_hash

class User:
    def __init__(self):
        print(hash_password("dummy hash function call"))
