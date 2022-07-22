#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

int num[1000001], dp[1000001];
int n, maxx, idx;

vector <int> L;
stack <int> s;
vector <int>::iterator p;

int main() {
	cin >> n;
	for(int i=0;i<n;i++) {
		cin >> num[i];
		if(L.size() == 0) {
			L.push_back(num[i]);
			dp[i] = 1;
		}
		else {
			if(L[L.size()-1] < num[i]) {
				L.push_back(num[i]);
				dp[i] = L.size();
			}
			else {
				p = lower_bound(L.begin(), L.end(), num[i]);
				*p = num[i];
				dp[i] = p - L.begin() + 1;
			}
		}
		if(dp[i] > maxx) {
			idx = i;
			maxx = dp[i];
		}
	}
	cout << L.size() << "\n";
	s.push(num[idx]);
	for(int i=idx-1;i>=0;i--) {
		if(num[i] < num[idx] and dp[i]+1 == dp[idx]) {
			idx = i;
			s.push(num[i]);
		}
	}
	while(!s.empty()) {
		cout << s.top() << " ";
		s.pop();
	}
}