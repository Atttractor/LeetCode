"""
Medium
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

Runtime: 58.86% 684ms
Memory: 68.53% 41.7MB
"""


class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        left, right = 0, len(self.arr[index]) - 1

        while left <= right:
            m = (left + right) // 2
            if self.arr[index][m][0] <= snap_id:
                left = m + 1
            else:
                right = m - 1

        return self.arr[index][right][1]


if __name__ == '__main__':
    a = SnapshotArray(3)
    a.set(0, 5)
    a.snap()
    a.set(0, 6)
    print(a.arr)
    print(a.get(0, 0))
