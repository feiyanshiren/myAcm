#include<stdio.h>
#include<string>
using namespace std;

string intToRoman(int num) {
        if (num > 3999) {
            return "";
        }
        
        string BitNum[10] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        string TenNum[10] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        string HunNum[10] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        string ThuNum[4]  = {"", "M", "MM", "MMM"};
        
        string result;
        int divNum = 1000;
        while (divNum) {
            int index = num / divNum;
            switch (divNum) {
                case 1000:
                    result += ThuNum[index];
                    break;
                case 100:
                    result += HunNum[index];
                    break;
                case 10:
                    result += TenNum[index];
                    break;
                case 1:
                    result += BitNum[index];
                    break;
                default:
                    break;
            }
            if (divNum == 1) {
                break;
            }
            else{
                num %= divNum;
                divNum /= 10;
            }
        }
        return result;
    }
main(){
    int n;
    while(scanf("%d", &n) != EOF){
        printf("%s\n", intToRoman(n).c_str());
    }
}
