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
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        ordered_set window;
        vector<double> ans;
        for (int i = 0; i < nums.size(); ++i) {
            window.insert(nums[i]);

            if (window.size() > k) {
                // Remove only one instance of nums[i - k]
                window.erase(window.find_by_order(window.order_of_key(nums[i - k])));
            }

            if (window.size() == k) {
                auto it = window.find_by_order(k / 2);
                double mid1 = *it;
                
                if (k % 2 != 0) {
                    ans.push_back(mid1);
                } else {
                    double mid2 = *std::prev(it);
                    ans.push_back((mid1 + mid2) / 2.0);
                }
            }
        }
        return ans;
    }
};
