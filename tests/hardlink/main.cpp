namespace Original {
#include "header.hpp"
}

namespace Hardlink {
#include "hardlink.hpp"
}

int main() {
    Original::foo();
    Hardlink::foo();
}