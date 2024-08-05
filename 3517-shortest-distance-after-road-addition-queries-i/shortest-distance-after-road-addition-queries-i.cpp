#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

class Solution {
public:
    // DFS-like shortest path using priority queue (Dijkstra's algorithm-like)
    int dfs(int n, vector<vector<int>>& ad) {
        // Min-heap priority queue to find shortest paths
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<int> v(n, INT_MAX);  // Distance vector, initially set to "infinity"
        
        // Starting node with distance 0
        v[0] = 0;
        pq.push({0, v[0]});

        while (!pq.empty()) {
            int x = pq.top().first;  // Current node
            int y = pq.top().second; // Current distance
            pq.pop();

            // Iterate over all neighbors of node x
            for (auto i : ad[x]) {
                if (y + 1 < v[i]) {  // If a shorter path to node i is found
                    v[i] = y + 1;
                    pq.push({i, y + 1});
                }
            }
        }

        return v[n - 1];  // Return the distance to the last node
    }

    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& q) {
        vector<vector<int>> a(n);  // Initialize the adjacency list with size n
        vector<int> b;

        // Construct the initial adjacency list with sequential edges
        for (int i = 0; i < n - 1; i++) {
            a[i].push_back(i + 1);
        }

        // Process each query
        for (int i = 0; i < q.size(); i++) {
            a[q[i][0]].push_back(q[i][1]);  // Add the edge defined by the query
            int shortestDist = dfs(n, a);    // Debug: print the shortest distance
            b.push_back(shortestDist);      // Store the result
        }

        return b;
    }
};
