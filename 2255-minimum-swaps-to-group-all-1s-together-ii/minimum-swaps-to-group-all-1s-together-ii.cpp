class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int n=nums.size();
        if (n==1) return 0;
        nums.insert(nums.end(),nums.begin(),nums.end());
        int c=0;
        for(int i=0;i<n;i++) if (nums[i]==1) c+=1;
        int i=0;
        int z=0;
        int j=c-1;
        int m=n-c;
        for(int x=0;x<c;x++) if (nums[x]==0) z+=1;
        cout<<z;
        for(i=0;i<n;i++){
            if (nums[i]==0) z-=1;
            if (nums[j+1]==0) z+=1;
            j+=1;
            m=min(z,m);
        }
        return m;
    }
};