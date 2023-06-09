namespace Original {
#include "header.hpp"
}

namespace Duplicate {
#include "duplicate.hpp"
}

int main() {
    Original::foo();
    Duplicate::foo();
}