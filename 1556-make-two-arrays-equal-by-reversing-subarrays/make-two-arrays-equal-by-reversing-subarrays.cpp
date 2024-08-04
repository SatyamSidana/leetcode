class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        unordered_map<int,int>a;
        for(auto i:target) a[i]+=1;
        for(auto i:arr){
            if(a.find(i)!=a.end() && a[i]!=0){
                a[i]-=1;
            }
            else{
                return false;
            }
        }
        return true;
    }
};