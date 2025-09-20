from typing import Protocol


class StorageProtocol(Protocol):
    def set(self, *args, **kwargs):
        ...

    def get(self, key):
        ...

    def all(self):
        ...

    def exists(self, key):
        ...

    def remove(self, key):
        ...

    def update(self, key, value):
        ...


class FakeStorage(StorageProtocol):
    def __init__(self):
        self.storage = {}

    def set(self, value):
        if value['key'] not in self.storage:
            self.storage[value['key']] = value
        return True

    def get(self, key):
        if key in self.storage:
            return self.storage[key]
        raise KeyError(key)

    def all(self):
        return self.storage

    def exists(self, key):
        return key in self.storage

    def remove(self, key):
        del self.storage[key]
        return True

    def update(self, key, value):
        self.storage[key] = value
