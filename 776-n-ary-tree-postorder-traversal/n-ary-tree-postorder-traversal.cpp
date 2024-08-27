/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    vector<int> dfs(Node* cur,vector<int>& a){
        if (cur!=NULL){
            for(auto i:cur->children){
                dfs(i,a);
            }
            a.push_back(cur->val);
        }
        return a;
    }
public:
    vector<int> postorder(Node* root) {
        vector<int> a;
        dfs(root,a);
        return a;
    }
};