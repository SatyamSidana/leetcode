class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<pair<int,int>>>ad(n);
        for(auto i:flights){
            ad[i[0]].push_back({i[1],i[2]});
        }
        vector<int>v(n,INT_MAX);
        v[src]=0;
        queue<pair<int,pair<int,int>>>q;
        q.push({0,{src,0}});
        while(!q.empty()){
            int a=q.front().first;
            int b=q.front().second.first;
            int c=q.front().second.second;
            q.pop();
           
            if(a>k){
               continue; 
            }
            for(auto i:ad[b]){
                if (a<=k && i.second+c<v[i.first]){
                    v[i.first]=i.second+c;
                    q.push({a+1,{i.first,i.second+c}});
                }
            }
        }
        if (v[dst]==INT_MAX)return -1;
        return v[dst];
    }
};