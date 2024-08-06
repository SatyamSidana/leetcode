class Solution {
public:
    int minimumPushes(string word) {
        vector<int>a(26,0);
        for(auto i:word)a[int(i)-int('a')]+=1;
        sort(a.begin(),a.end(),greater<int>());
        int c=0;
        int n=1;
        int ans=0;
        for(auto i:a){
            if (i>0) {
            ans+=i*(n);
            c+=1;
            if (c>7) {
                n+=1;
                c=0;
            }
            }
        }
        
        return ans;
    }
};