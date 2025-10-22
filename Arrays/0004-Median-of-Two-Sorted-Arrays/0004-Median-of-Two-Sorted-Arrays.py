class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tot=len(nums1)+len(nums2)
        is_even=False if tot%2!=0 else True
        j,k=0,0
        arr=[]
        while(j<len(nums1) and k<len(nums2)):
            if(nums1[j]<nums2[k]):
                arr.append(nums1[j])
                j+=1
            else:
                arr.append(nums2[k])
                k+=1

        while(j<len(nums1)):
            arr.append(nums1[j])
            j+=1

        while(k<len(nums2)):
            arr.append(nums2[k])
            k+=1

        if is_even:
            elem=(arr[tot//2]+arr[(tot//2)-1])/2
        else:
            elem=arr[tot//2]/1
        return elem
