class TimeMap:
    def __init__(self):
        # We use a dictionary where the key is a string, 
        # and the value is a list of tuples: (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # Since timestamps strictly increase, appending keeps the list sorted
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist at all, return ""
        if key not in self.store:
            return ""
        
        values = self.store[key]
        l, r = 0, len(values) - 1
        res = ""
        
        # Standard binary search to find the largest timestamp <= target
        while l <= r:
            mid = (l + r) // 2
            
            # values[mid][0] is the timestamp at the current midpoint
            if values[mid][0] <= timestamp:
                res = values[mid][1]  # This is a valid candidate! Save the value.
                l = mid + 1           # Try to find an even closer (larger) timestamp
            else:
                r = mid - 1           # Timestamp is too large, search the left half
                
        return res