#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> patterns = {"00", "10", "010", "01001"};

bool validate(const string& input, int start) {
    if (start == input.size()) return true; 
    for (const string& pattern : patterns) {
        if (input.substr(start, pattern.size()) == pattern) {
            if (validate(input, start + pattern.size())) {
                return true;
            }
        }
    }
    return false;
}

bool check(string testcase) {
    return validate(testcase, 0);
}

int main() {
    string testcase;
    cout << "Masukkan bit string: ";
    cin >> testcase;
    cout << testcase << ": " << (check(testcase) ? "Valid" : "Tidak Valid") << endl;
    
    return 0;
}
