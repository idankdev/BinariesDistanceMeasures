import lief
from hashlib import md5

BLOCK_SIZE = 24 # bytes


class Sample():
    def __init__(self, path: str, name: str = "UNKNOWN"):
        self.name = name
        self.original_path = path
        self.binary = lief.parse(path)
        self.strings = self.binary.get_strings()
        self.text_hash_blocks = []
        if self.binary.has_section(".text"):
            text_section = self.binary.get_section(".text")
            hasher = md5()
            for addr in range(self.binary.entrypoint, text_section.virtual_address + text_section.size, BLOCK_SIZE):
                hasher.update(bytes(self.binary.get_content_from_virtual_address(addr, BLOCK_SIZE)))
                self.text_hash_blocks.append(hasher.digest())
        self.file_hash_blocks = []
        hasher = md5()
        with open (path, "rb") as f:
            for block in iter(lambda: f.read(BLOCK_SIZE), b""):
                hasher.update(block)
                self.file_hash_blocks.append(hasher.digest())


    def __str__(self):
        return self.name
