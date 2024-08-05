class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string,int>a;
        for(const auto& i : arr) a[i]+=1;
        int cnt=0;
        
        for(auto str:arr){
            if(a[str]==1){
                cnt++;
                if(cnt==k){
                    return str;
                }
            }
        }
        return "";
    }
};