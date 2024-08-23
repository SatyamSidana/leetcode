#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <vector>
using namespace __gnu_pbds;
using namespace std;

typedef tree<
double,
null_type,
less_equal<double>,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        ordered_set a;
        int n=nums.size();
        int j=0;
        vector<int> ans;
        for(int i=0;i<n;i++){
            a.insert(nums[i]);
            if(a.size()>k){
                a.erase(a.find_by_order(a.order_of_key(nums[i-k])));
            }
            if(a.size()==k){
                auto it=a.find_by_order(k-1);
                int m=*it;
                ans.push_back(m);
            }
        }
        return ans;
    }
};