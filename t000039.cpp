#include <iostream>

int main()
{
    int a;
    while (true)
    {
        std::cin >> a;
        if (a == 153 || a == 370 || a == 371 || a == 407)
        {
            std::cout << "Yes" << std::endl;
        }
        else if (a == 0)
        {
            return 0;
        }
        else
        {
            std::cout << "No" << std::endl;
        }
    }
}