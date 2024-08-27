class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& e, vector<double>& p, int start_node, int end_node) {
        priority_queue<pair<double, int>> pq;
        
        vector<vector<pair<int, double>>> adj(n);
        for (int i = 0; i < e.size(); ++i) {
            adj[e[i][0]].push_back({e[i][1], p[i]});
            adj[e[i][1]].push_back({e[i][0], p[i]});
        }
        vector<double> d(n, 0.0);
        d[start_node] = 1.0;
        pq.push({1.0, start_node});

        while (!pq.empty()) {
            int node = pq.top().second;
            double prob = pq.top().first;
            pq.pop();
            if (prob < d[node]) continue;
            for (auto edge : adj[node]) {
                int neighbor = edge.first;
                double edgeProb = edge.second;
                if (prob * edgeProb > d[neighbor]) {
                    d[neighbor] = prob * edgeProb;
                    pq.push({d[neighbor], neighbor});
                }
            }
        }
        return d[end_node];
    }
};
