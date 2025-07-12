void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int i=0,j=0,k=0;
    if(m==0){
        int j=0;
        while(j<n){
            nums1[j]=nums2[j];
            j++;
        }
        return;
    }
    int arr[m];

    for(int i=0;i<m;i++){
        arr[i]=nums1[i];
    }
    while(i<m && j<n){
        if(arr[i]>nums2[j]){
            nums1[k++]=nums2[j++];
        }
        else{
            nums1[k++]=arr[i++];
        }
    }
    while(i<m){
        nums1[k++]=arr[i++];
    }
    while(j<n){
        nums1[k++]=nums2[j++];
    }
}
