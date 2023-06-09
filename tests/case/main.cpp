namespace Lower {
#include "dir/header.hpp"
}

namespace Upper {
#include "dir/HEADER.hpp"
}

int main() {
    Lower::foo();
    Upper::foo();
}