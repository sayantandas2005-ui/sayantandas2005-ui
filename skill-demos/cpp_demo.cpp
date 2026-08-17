#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<int> values{10, 20, 30, 40, 50};
    int sum = std::accumulate(values.begin(), values.end(), 0);

    std::cout << "Count: " << values.size() << '\n';
    std::cout << "Sum: " << sum << '\n';
    std::cout << "Mean: " << static_cast<double>(sum) / values.size() << '\n';
    return 0;
}
