class Solution:
 
    def merge(self,arr,l,mid,r):
        res = []
        i = l
        j = mid+1
        while i <= mid and j <= r:
            if arr[i]<arr[j]:
                res.append(arr[i])
                i+=1
            else:
                res.append(arr[j])
                j+=1
        res.extend(arr[i:mid+1])
        res.extend(arr[j:r+1])
        
        arr[l:r+1] = res
        
    def mergeSort(self, arr, l, r):
        if l>=r:
            return arr
        mid = (l+ r) // 2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)
        