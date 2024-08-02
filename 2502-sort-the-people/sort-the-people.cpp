class Solution {
public:
    vector<string> sortPeople(vector<string>& n, vector<int>& h) {
        unordered_map<int,string>a;
        for(int i=0;i<n.size();i++) a[h[i]]=n[i];
        sort(h.begin(),h.end(),greater<int>());
        vector<string>ans;
        for(int i=0;i<h.size();i++){
            ans.push_back(a[h[i]]);
        }
        return ans;

    }
};