namespace Original {
#include "header.hpp"
}

namespace Symlink {
#include "symlink.hpp"
}

int main() {
    Original::foo();
    Symlink::foo();
}