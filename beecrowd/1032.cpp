#include <iostream>
#include <vector>

bool is_prime(int n);
int find_next_prime(int prime);
void print(std::vector <int> const &a);

int main() {
  int n;
  std::cin >> n;
  
  while (n != 0) {
    std::vector<int> people;

    for (int i = 0; i < n; i++) {
      people.push_back(i + 1);
    }

    int start = 0;
    int prime = 2;
    int index;
    while (people.size() > 1) {
      index = (start + prime - 1) % people.size();
      people.erase(people.begin() + index);

      start = index;
      prime = find_next_prime(prime);
    }

    std::cout << people[0] << "\n";
    std::cin >> n;
  }
}

int find_next_prime(int prime) {
  int possible_prime;
  if (prime == 2) possible_prime = 3;
  else {
    possible_prime = prime + 2;
    while (!is_prime(possible_prime)) possible_prime += 2;
  }
  return possible_prime;
}

bool is_prime(int n) {
  if (n == 2) {
    return true;
  }

  if (n % 2 == 0) {
    return false;
  }

  for (int i = 3; i < n / 2; i += 2) {
    if (n % i == 0) {
      return false;
    }
  }

  return true;
}
