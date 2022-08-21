/*
Solution can be found in P1213.py
*/

#include <iostream>
#include <queue>
using namespace std;
struct STATUS{
    int step_num, action_type, pred_status;
    bool has_visit;
    STATUS() {
        has_visit = false;
    }
    void set_value(int sn, int at, int ps) {
        this->step_num = sn, this->action_type = at, this->pred_status = ps;
        has_visit = true;
    }
};
int actions[9][5] = {{0, 1, 3, 4, -1}, {0, 1, 2, -1, -1}, {1, 2, 4, 5, -1}, {0, 3, 6, -1, -1}, {1, 3, 4, 5, 7}, {2, 5, 8, -1, -1}, {3, 4, 6, 7, -1}, {6, 7, 8, -1, -1}, {4, 5, 7, 8, -1}};
int status[9];
const int NMAX = 1 << 18;
STATUS status_data[NMAX];
int status2num() {
    int _sum = 0;
    for (int i = 0; i < 9; i++) {
        _sum = _sum * 4 + status[i];
    }
    return _sum;
}
void num2status(int num) {
    for (int i = 8; i >= 0; i--) {
        status[i] = num % 4;
        num /= 4;
    }
}
int main() {
    int final_status = 0;
    int a, b, c;
    for (int i = 0; i < 3; i++) {
        scanf("%d%d%d", &a, &b, &c);
        status[i*3] = (a/3)%4;
        status[i*3+1] = (b/3)%4;
        status[i*3+2] = (c/3)%4;
    }
    int s0 = status2num();
    if (s0 == final_status) {
        return 0;
    }
    queue<int> dq;
    dq.push(s0);
    status_data[s0].set_value(0, -1, -1);
    while (true) {
        if (dq.size() == 0) { break; }
        int st = dq.front(); dq.pop();
        for (int i = 0; i < 9; i++) {
            num2status(st);
            for (int j = 0; j < 5; j++) {
                int idx = actions[i][j];
                if (idx > -1) {
                    status[idx] = (status[idx] + 1) % 4;
                }
            }
            int s_new = status2num();
            if (!status_data[s_new].has_visit) {
                status_data[s_new].set_value(status_data[st].step_num+1, i + 1, st);
                dq.push(s_new);
                // printf("visit %d from %d in type %d\n", s_new, st, i+1);
            }
        }
        if (status_data[final_status].has_visit) {
            int cur_state = final_status;
            vector<int> pathes;
            while (true) {
                if (status_data[cur_state].pred_status == -1) {
                    break;
                }
                pathes.push_back(status_data[cur_state].action_type);
                cur_state = status_data[cur_state].pred_status;
            }
            for (int i = pathes.size()-1; i >= 0; i--) {
                printf("%d ", pathes[i]);
            }
            printf("\n");
            break;
        }
        


    }


    return 0;
}