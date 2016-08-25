## Memcache

## set[key, value] --> returns True
## get(key) --> returns Value or None
## delete(key)
## flush()

class Memcache:
    def __init__(self):
        self.CACHE = {}

    def set(self, key, value):
        pass

    def get(self, key):
        pass

    def delete(self, key):
        pass

    def flush(self):
        pass

def test_memcache():
    m = Memcache()
    print m.set('a','1')
    print m.set('b','2')
    print m.CACHE
    print m.get('b')
    print m.get('c')
    m.delete('b')
    print m.CACHE
    m.flush()
    print m.CACHE

    # True
    # True
    # {'a':'1', 'b':'2'}
    # 2
    # {'a':'1'}
    # {}


if __name__ == '__main__':
    test_memcache()