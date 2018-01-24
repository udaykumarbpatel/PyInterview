class TempTracker(object):

    def __init__(self):
        self.min_temp = float('inf')
        self.max_temp = float('-inf')
        self.sum = 0.0
        self.count = 0
        self.mean = None
        self.occurrences = [0] * 111
        self.max_occurrences = 0
        self.mode = None

    def insert(self, temperature):
        self.occurrences[temperature] += 1
        if self.occurrences[temperature] > self.max_occurrences:
            self.mode = temperature
            self.max_occurrences = self.occurrences[temperature]

        self.count += 1
        self.sum = self.sum + temperature
        self.mean = self.sum / self.count
        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode
