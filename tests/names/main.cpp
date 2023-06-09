namespace A {
#include "a/a.hpp"
}

namespace B {
#include "b/b.hpp"
}

int main() {
    A::foo();
    B::foo();
}