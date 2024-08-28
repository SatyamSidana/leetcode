class Solution {
public:
    int shortestPathLength(vector<vector<int>>& g) {
        int n=g.size();
        if (n==1) return 0;
        queue<vector<int>>q;
        int endmask=(1<<n)-1;
        vector<vector<int>>v(n,vector<int>(endmask,0));
        for(int i=0;i<n;i++){
            q.push({i,0,1<<i});
        }
        while(!q.empty()){
            int s=q.front()[0];
            int c=q.front()[1];
            int mask=q.front()[2];
            q.pop();
            v[s][mask]=1;
            for(auto i:g[s]){
                int temp=mask|1<<i;
                if(temp==endmask) return c+1;
                else{
                    if (v[i][temp]==0){
                    v[i][temp]=1;
                    q.push({i,c+1,temp});
                }
                }
            }
        }
        return -1;
    }
};