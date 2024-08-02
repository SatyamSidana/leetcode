class Solution {
public:
    int valid(int num){
        string a=to_string(num);
        int c=0;
        for(int i=0;i<a.size();i++) c+=stoi(to_string(a[i]));
        if (c%2==0) return 1 ;
        return 0;
    }
    int countEven(int num) {
        int ans=0;
        for(int i=1;i<=num;i++) ans+=valid(i);
        return ans;
    }
};