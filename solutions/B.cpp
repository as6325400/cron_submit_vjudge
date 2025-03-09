#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define endl '\n'

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int m, n;
  while (cin >> m >> n)
  {
    vector<int> P(n), F(n);
    for (int i = 0; i < n; ++i)
      cin >> P[i] >> F[i];

    int U = (m > 1800) ? m + 200 : m;

    vector<int> dp(U + 1, -1);
    dp[0] = 0;

    for (int i = 0; i < n; ++i)
    {
      int price = P[i], favour = F[i];
      for (int j = U; j >= price; --j)
      {
        if (dp[j - price] != -1) 
          dp[j] = max(dp[j], dp[j - price] + favour);
      }
    }

    int maxF = 0;
    if (m > 1800 && m < 2000)
    {
      maxF = max(*max_element(dp.begin(), dp.begin() + (m + 1)),
                 *max_element(dp.begin() + 2001, dp.begin() + (U + 1)));
    }
    else
    {
      maxF = *max_element(dp.begin(), dp.begin() + (U + 1));
    }

    cout << maxF << endl;
  }
  return 0;
}
