class Solution {
public:
    int orangesRotting(vector<vector<int>>& g) {
        int n=g.size();
        int m=g[0].size();
        queue<pair<pair<int,int>,int>>q;
        vector<vector<int>>vis;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if (g[i][j]==2) q.push({{i,j},0});
            }
        }
        int ma=0;
        while (!q.empty()){
            int x=q.front().first.first;
            int y=q.front().first.second;
            int t=q.front().second;
            ma=max(ma,t);
            q.pop();
            if (x!=0 and g[x-1][y]==1) {
                q.push({{x-1,y},t+1});
                g[x-1][y]=2;
                }
            if (x!=n-1 and g[x+1][y]==1){
            q.push({{x+1,y},t+1});
            g[x+1][y]=2;
            }
            if (y!=0 and g[x][y-1]==1) {
                q.push({{x,y-1},t+1});
                g[x][y-1]=2;
            }
            if (y!=m-1 and g[x][y+1]==1){
                 q.push({{x,y+1},t+1});
                 g[x][y+1]=2;
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if (g[i][j]==1) return -1;
            }
        }
        return ma;
    }
};