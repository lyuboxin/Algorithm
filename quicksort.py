class Quick_Sort(object):
    def __init__(self, arr):
        self.arr = arr
    def quickSort(self, low, high):
        if low < high:
            pi = self.Partition(low, high)
            self.quickSort(low, pi - 1)
            self.quickSort(pi + 1, high)
    
    def Partition(self,low, high):
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i = i + 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]               
        self.arr[high], self.arr[i + 1] = self.arr[i + 1], self.arr[high]
        return i+1

    def printResult(self):
        print self.arr


qs = Quick_Sort([3,2,7,9,1,4,2])
qs.printResult()
qs.quickSort(0, 6)
qs.printResult()
