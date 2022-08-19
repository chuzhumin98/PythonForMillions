/*
solution can be found in P1279.py
*/
#include <iostream>
#include <string>
using namespace std;
const int NMAX = 2010;
int distances[NMAX][NMAX];
int main() {
    string sA;
    string sB;
    getline(cin, sA);
    getline(cin, sB);
    int K;
    cin >> K;
    int M = sA.length(), N = sB.length();
    for (int i = 0; i <= M; i++) {
        distances[i][0] = i * K;
    }
    for (int i = 0; i <= N; i++) {
        distances[0][i] = i * K;
    }
    for (int i = 1; i <= M; i++) {
        for (int j = 1; j <= N; j++) {
            distances[i][j] = min(distances[i-1][j] + K, distances[i][j-1] + K);
            distances[i][j] = min(distances[i][j], distances[i-1][j-1] + abs(int(sA[i-1]) - int(sB[j-1])));
        }
    }
    cout << distances[M][N] << endl;

    return 0;
}