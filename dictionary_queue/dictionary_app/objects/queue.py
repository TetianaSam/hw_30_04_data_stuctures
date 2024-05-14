import heapq

class PriorityQueue:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.queue = []

    def add_word(self, word, count):
        heapq.heappush(self.queue, (count, word))
        if len(self.queue) > self.max_size:
            heapq.heappop(self.queue)

    def get_top_n(self, n):
        return heapq.nlargest(n, self.queue)

    def get_bottom_n(self, n):
        return heapq.nsmallest(n, self.queue)
