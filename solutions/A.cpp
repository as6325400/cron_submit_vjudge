#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;

  while (T--)
  {
    int N;
    cin >> N;

    vector<pair<int, int>> items(N);

    for (int i = 0; i < N; i++)
    {
      cin >> items[i].first >> items[i].second;
    }

    int G;
    cin >> G;

    vector<int> maxWeight(G);

    for (int i = 0; i < G; i++)
    {
      cin >> maxWeight[i];
    }

    int totalMaxValue = 0;

    for (int i = 0; i < G; i++)
    {
      int MW = maxWeight[i];

      vector<int> dp(MW + 1, 0);

      for (int j = 0; j < N; j++)
      {
        int price = items[j].first;
        int weight = items[j].second;

        for (int k = MW; k >= weight; k--)
        {
          dp[k] = max(dp[k], dp[k - weight] + price);
        }
      }

      totalMaxValue += dp[MW];
    }

    cout << totalMaxValue << endl;
  }

  return 0;
}
