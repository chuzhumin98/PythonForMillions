/*
Solution: see in 1713D.py
*/

#include <iostream>
using namespace std;
int main() {
    int t = 0;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n = 0;
        cin >> n;
        int N = 1 << n;
        int* arr = new int [N];
        for (int j = 0; j < N; j++) {
            arr[j] = j+1;
        }
        int len_arr = N;
        while (true) {
            if (len_arr == 1) {
                cout << "! " << arr[0] << endl;
                cout.flush();
                break;
            } else if (len_arr == 2) {
                cout << "? " << arr[0] << " " << arr[1] << endl;
                cout.flush();
                int flag;
                cin >> flag;
                if (flag == 1) {
                    cout << "! " << arr[0] << endl;
                    cout.flush();
                } else {
                    cout << "! " << arr[1] << endl;
                    cout.flush();
                }
                break;
            } else {
                int* arr_new = new int [len_arr / 4];
                for (int j = 0; j < len_arr / 4; j++) {
                    cout << "? " << arr[j*4] << " " << arr[j*4+2] << endl;
                    cout.flush();
                    int flag;
                    cin >> flag;
                    if (flag == 1) {
                        cout << "? " << arr[j*4] << " " << arr[j*4+3] << endl;
                        cout.flush();
                        int flag_2;
                        cin >> flag_2;
                        if (flag_2 == 1) {
                            arr_new[j] = arr[j*4];
                        } else {
                            arr_new[j] = arr[j*4 + 3];
                        }
                    } else if (flag == 2) {
                        cout << "? " << arr[j*4+1] << " " << arr[j*4+2] << endl;
                        cout.flush();
                        int flag_2;
                        cin >> flag_2;
                        if (flag_2 == 1) {
                            arr_new[j] = arr[j*4+1];
                        } else {
                            arr_new[j] = arr[j*4 + 2];
                        }
                    } else {
                        cout << "? " << arr[j*4+1] << " " << arr[j*4+3] << endl;
                        cout.flush();
                        int flag_2;
                        cin >> flag_2;
                        if (flag_2 == 1) {
                            arr_new[j] = arr[j*4+1];
                        } else {
                            arr_new[j] = arr[j*4 + 3];
                        }
                    }

                }

                delete []arr;
                arr = arr_new;
                len_arr /= 4;
            }
        }
    }

    return 0;
}