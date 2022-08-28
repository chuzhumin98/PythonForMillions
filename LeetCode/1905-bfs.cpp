/*
Solution: DFS
note that for each linked island in grid2, if it is a sub-island of grid1, we only need to confirm this area is island in grid1 (connectility is naturally guaranteed).
Thus, we only need to conduct bfs for each grid2's connection blocks, the problem done!
*/

#include <iostream>
#include <vector>
#include <queue>
#define NMAX 500
using namespace std;
struct Point {
    int x, y;
    Point(int xx, int yy) {
        this->x = xx; this->y = yy;
    }
}; 
class Solution {
public:
    int m, n;
    int belongs2[NMAX][NMAX];
    int bfs(vector<vector<int> >& grid, int belongs[][NMAX], vector<vector<int> >& gridCMP) {
        int idx = -1;
        for (int i = 0; i < this->m; i++) {
            for (int j = 0; j < this->n; j++) {
                belongs[i][j] = -1;
            }
        }

        int _ans = 0;     
    
        for (int i = 0; i < this->m; i++) {
            for (int j = 0; j < this->n; j++) {
                if (belongs[i][j] == -1 && grid[i][j] == 1) {
                    bool isFu = true;
                    idx++;
                    queue<Point> dq;
                    dq.push(Point(i, j));
                    belongs[i][j] = idx;
                    vector<Point> group;
                    while (dq.size() > 0) {
                        Point p = dq.front(); dq.pop();
                        if (gridCMP[p.x][p.y] == 0) {
                            isFu = false;
                        }
                        if (p.x > 0) {
                            if (grid[p.x-1][p.y] == 1 && belongs[p.x-1][p.y] == -1) {
                                dq.push(Point(p.x-1, p.y));
                                belongs[p.x-1][p.y] = idx;
                            }
                        }
                        if (p.y > 0) {
                            if (grid[p.x][p.y-1] == 1 && belongs[p.x][p.y-1] == -1) {
                                dq.push(Point(p.x, p.y-1));
                                belongs[p.x][p.y-1] = idx;
                            }
                        }
                        if (p.x < this->m - 1) {
                            if (grid[p.x+1][p.y] == 1 && belongs[p.x+1][p.y] == -1) {
                                dq.push(Point(p.x+1, p.y));
                                belongs[p.x+1][p.y] = idx;
                            }
                        }
                        if (p.y < this->n - 1) {
                            if (grid[p.x][p.y+1] == 1 && belongs[p.x][p.y+1] == -1) {
                                dq.push(Point(p.x, p.y+1));
                                belongs[p.x][p.y+1] = idx;
                            }
                        }
                    }
                    if (isFu) {
                        _ans ++;
                    }
                }
            }
        }
        return _ans;

    }

    int countSubIslands(vector<vector<int> >& grid1, vector<vector<int> >& grid2) {
        this->m = grid1.size();
        this->n = grid1[0].size();
        return this->bfs(grid2, belongs2, grid1);

    }
};

int main() {


    return 0;
}