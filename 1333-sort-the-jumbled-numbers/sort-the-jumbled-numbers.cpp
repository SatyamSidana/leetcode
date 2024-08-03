class Solution {
public:
    int convert(vector<int>& m,int a) {
            int ans = 0 , j=0;
            if (a == 0) {
                ans = m[a];
            } else {
                while (a > 0) {
                    ans += pow(10, j) * m[a % 10];
                    a /= 10;
                    ++j;
                }
            }
        return ans;
    }
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        map<int,vector<int>>h;
        for(int i=0;i<nums.size();i++){
            int x=convert(mapping,nums[i]);
            h[x].push_back(nums[i]);
        }
        vector<int>b;
        for(auto i:h){
            for(auto j:i.second) b.push_back(j);
        }
        return b;
    }
};