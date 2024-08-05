#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    // Find with path compression
    int find(int x, vector<int>& p) {
        if (x != p[x]) {
            p[x] = find(p[x], p);
        }
        return p[x];
    }

    // Union function
    void un(int x, int y, vector<int>& p) {
        int xi = find(x, p);
        int yi = find(y, p);
        if (xi != yi) {
            p[xi] = yi;
        }
    }

    // Main function to determine if a bipartition is possible
    bool possibleBipartition(int n, vector<vector<int>>& d) {
        // Initialize the parent vector
        vector<int> p(n + 1);
        for (int i = 0; i <= n; i++) {
            p[i] = i;
        }

        // Create adjacency list for dislikes
        unordered_map<int, vector<int>> a;
        for (auto& pair : d) {
            a[pair[0]].push_back(pair[1]);
            a[pair[1]].push_back(pair[0]);
        }

        // Check bipartition condition using union-find
        for (int i = 1; i <= n; i++) {
            if (!a[i].empty()) {
                // Get the first neighbor
                int firstNeighbor = a[i][0];
                for (int j = 1; j < a[i].size(); j++) {
                    // If a cycle is detected, it's not possible to bipartition
                    if (find(i, p) == find(a[i][j], p)) {
                        return false;
                    }
                    // Union the first neighbor and the current neighbor
                    un(firstNeighbor, a[i][j], p);
                }
            }
        }

        return true;
    }
};
