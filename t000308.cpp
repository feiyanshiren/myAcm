#include<iostream>
#include<algorithm>
#include<string> 
using namespace std;
int main() {
  int n;
  cin >> n;
  while (n--) {
    bool flag = false;
    string str1, str2;
    cin >> str1;
    str2 = str1;
    reverse(str2.begin(), str2.end()); //反转字符串 
    for (int i = str1.size(); i > 0; i--) {  //
      for (int j = 0; j <= str1.size() - i; j++) { //遍历字符串 
        string t = str1.substr(j, i); //截取字符串 
        string::size_type pos = str2.find(t); //size_type相当于一个宏定义 
        if (pos != string::npos) { //string::npos理解为一个返回值为假的值 
          cout << t << endl;
          flag = true;
          break;
        } 
      }
      if (flag)break;
    }
  }
} 
//题目意思是求一个子串，该子串反转之后还是该字符串中的子串 
//思路是先把该字符串反转 然后再找        