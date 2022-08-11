/*
See solution in the code file 1713E.py
*/

#include <iostream>
using namespace std;

void get_parent(int* union_set, int* flags_set, int node) {
    if (union_set[node] == node) {
        return;
    } else {
        int parent = union_set[node];
        int flag = flags_set[node];

        get_parent(union_set, flags_set, parent);
        int root = union_set[parent];
        int flag_root = flags_set[parent];

        union_set[node] = root;
        flags_set[node] = (flag + flag_root) % 2;
    }
}

bool merge(int* union_set, int* flags_set, int nodeA, int nodeB, int flag) {
    get_parent(union_set, flags_set, nodeA);
    get_parent(union_set, flags_set, nodeB);
    if (union_set[nodeA] != union_set[nodeB]) {
        int parB = union_set[nodeB];
        union_set[parB] = union_set[nodeA];
        flags_set[parB] = (flag + flags_set[nodeA] + flags_set[nodeB]);
        return true;
    } else {
        return false;
    }
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t = 0;
    cin >> t;
    for (int _ = 0; _ < t; _++) {
        int n = 0;
        cin >> n;
        int** matrix = new int* [n];
        for (int i = 0; i < n; i++) {
            matrix[i] = new int [n];
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> matrix[i][j];
            }
        }

        int current_type_num = n;
        int* union_set = new int [n];
        int* flags_set = new int [n];
        for (int i = 0; i < n; i++) {
            union_set[i] = i;
            flags_set[i] = 0;
        }

        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if (matrix[i][j] < matrix[j][i]) {
                    bool flag = merge(union_set, flags_set, i, j, 0);
                    if (flag) {
                        current_type_num--;
                    }
                } else if (matrix[i][j] > matrix[j][i]) {
                    bool flag = merge(union_set, flags_set, i, j, 1);
                    if (flag) {
                        current_type_num--;
                    }
                }
                if (current_type_num == 1) {
                    break;
                }
            }
            if (current_type_num == 1) {
                break;
            }
        }

        for (int i = 0; i < n; i++) {
            get_parent(union_set, flags_set, i);
            if (flags_set[i] == 1) {
                for (int j = 0; j < n; j++) {
                    int temp = matrix[i][j];
                    matrix[i][j] = matrix[j][i];
                    matrix[j][i] = temp;
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << matrix[i][j] << " ";
            }
            cout << endl;
        }

        for (int i = 0; i < n; i++) {
            delete []matrix[i];
        }
        delete []matrix;
        delete []union_set;
        delete []flags_set;
    }
    return 0;
}