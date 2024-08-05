class Solution {
public:
    int dfs(int n, vector<vector<int>>& ad){
        priority_queue<pair<int,int> ,vector<pair<int,int>> ,greater<pair<int,int>>>pq;
        vector<int>v(n,INT_MAX);
        v[0]=0;
        pq.push({0,v[0]});
        while(!pq.empty()){
            int x=pq.top().first;
            int y=pq.top().second;
            pq.pop();
            for(auto i:ad[x]){
                if (y+1<v[i]){
                    v[i]=y+1;
                    pq.push({i,y+1});
                }
            }
        }
        return v[n-1];
    }
    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& q) {
        vector<vector<int>>a(n);
        vector<int>b;
        for(int i=0;i<n-1;i++){
            a[i].push_back(i+1);
        }
        for(int i=0;i<q.size();i++){
            a[q[i][0]].push_back(q[i][1]);
            b.push_back(dfs(n,a));
        }
        return b;
    }
};