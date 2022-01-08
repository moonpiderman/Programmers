class SparseArray:
    def __init__(self, arr, size):
        self.size = size
        self.map = {}

        origin_length = len(arr)
        for i, v in enumerate(arr):
            if i >= origin_length:
                break
            if v != 0:
                map[i] = v

    def error_bound(self, i):
        if i < 0 or i >= self.size:
            raise IndexError()

    def set(self, i, v):
        self.error_bound(i)
        self.map[i] = v

    def get(self, i):
        self.error_bound(i)
        v = self.map.get(i)

        if v is None:
            return 0
        return v

if __name__ == '__main__':
    array = [0, 0, 0, 0, 0, 2, 1, 0, 0, 3, 0, 7, 0, 1, 9, 0, 0, 0, 11]
    test = SparseArray(array, 19)
