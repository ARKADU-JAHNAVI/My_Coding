class Solution:
    def quickSort(self, arr, low, high):
        #code here
         if low<high:
                
            pi=self.partition(arr,low,high)
            self.quickSort(arr,low,pi-1)
            self.quickSort(arr,pi+1,high)

    def partition(self, arr, low, high):
        #code here
         pivot=arr[low]
         start=low
         end=high
         while start<end:
             while start<high and arr[start]<=pivot:
                 start+=1
             while end >low and arr[end]>pivot:
                 end-=1
             if start<end:
                 arr[start],arr[end]=arr[end],arr[start]
         arr[low],arr[end]=arr[end],arr[low]
         return end