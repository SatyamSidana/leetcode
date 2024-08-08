class Solution {
public:
    int f(int i,int j,vector<int>& a,vector<vector<int>>& dp){
        if (i>j) return 0;
        int m=0;
        if (dp[i][j]!=-1) return dp[i][j];
        for(int ind=i;ind<=j;ind++){
            int coins = (a[i - 1] * a[ind] * a[j + 1]) 
                        + f(i, ind - 1, a,dp) 
                        + f(ind + 1, j, a,dp);
            m=max(coins,m);
        }
        dp[i][j]=m;
        return m;
    }
    int maxCoins(vector<int>& n) {
        
        n.insert(n.begin(),1);
        n.push_back(1);
        vector<int>a(n.size(),-1);
        vector<vector<int>>dp(n.size(),a);
        return f(1,n.size()-2,n,dp);
    }
};