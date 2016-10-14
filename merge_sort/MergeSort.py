class MergeSort(object):
    def __init__(self, numbers):
        self.values = numbers

    def sort(self):
        self.merge_sort(0, len(self.values)-1)
        return self.values

    def merge_sort(self, idx_bot, idx_top):
        if idx_bot < idx_top:
            idx_mid = (idx_bot + idx_top) // 2

            self.merge_sort(idx_bot, idx_mid)
            self.merge_sort(idx_mid + 1, idx_top)
            self.merge(idx_bot, idx_mid, idx_top)

    def merge(self, idx_bot, idx_mid, idx_top):
        temp_array = []
        i = idx_bot
        j = idx_mid + 1

        while i <= idx_mid and j <= idx_top:
            if self.values[i] <= self.values[j]:
                temp_array.append(self.values[i])
                i += 1
            else:
                temp_array.append(self.values[j])
                j += 1

        while i <= idx_mid:
            temp_array.append(self.values[i])
            i += 1

        while j <= idx_top:
            temp_array.append(self.values[j])
            j += 1

        for idx, value in enumerate(temp_array):
            self.values[idx_bot + idx] = value
