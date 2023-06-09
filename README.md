## `#pragma once` Test

## Results

This table shows whether the compilers believe two files are "the same" when using `#pragma once`.

| Name      | Clang     | GCC       | MSVC      |
| ----------| --------- | --------- | --------- |
| Symlink   | same      | same      | different |
| Hardlink  | same      | same      | different |
| Duplicate | different | same      | different |
| Case      | different | different | same      |

## Raw Results

### Clang 14.0

```bash
$ clang --version
Ubuntu clang version 14.0.0-1ubuntu1
Target: x86_64-pc-linux-gnu
Thread model: posix
InstalledDir: /usr/bin
$ python3 run.py clang
Setting up 'duplicate' test
 - Removing existing file (tests/duplicate/duplicate.hpp)
 - Creating duplicate of header.hpp
 - Updating modification time

Setting up 'hardlink' test
 - Removing existing hardlink (tests/hardlink/hardlink.hpp)
 - Creating hardlink of header.hpp

Setting up 'symlink' test
 - Removing existing symlink (tests/symlink/symlink.hpp)
 - Creating symlink of header.hpp

Setting up 'case' test
 - Removing existing directory (tests/case/dir)
 - Creating directory (tests/case/dir)
 - Creating (tests/case/dir/header.hpp)
 - Creating (tests/case/dir/HEADER.hpp)

Running tests
tests/hardlink/main.cpp:11:5: error: no member named 'foo' in namespace 'Hardlink'; did you mean 'Original::foo'?
    Hardlink::foo();
    ^~~~~~~~~~~~~
    Original::foo
tests/hardlink/hardlink.hpp:3:5: note: 'Original::foo' declared here
int foo() { return 42; }
    ^
1 error generated.
tests/symlink/main.cpp:11:5: error: no member named 'foo' in namespace 'Symlink'; did you mean 'Original::foo'?
    Symlink::foo();
    ^~~~~~~~~~~~
    Original::foo
tests/symlink/symlink.hpp:3:5: note: 'Original::foo' declared here
int foo() { return 42; }
    ^
1 error generated.
```

### GCC 11.3.0

```bash
$ gcc --version
gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
$ python3 run.py gcc
Setting up 'duplicate' test
 - Removing existing file (tests/duplicate/duplicate.hpp)
 - Creating duplicate of header.hpp
 - Updating modification time

Setting up 'hardlink' test
 - Removing existing hardlink (tests/hardlink/hardlink.hpp)
 - Creating hardlink of header.hpp

Setting up 'symlink' test
 - Removing existing symlink (tests/symlink/symlink.hpp)
 - Creating symlink of header.hpp

Setting up 'case' test
 - Removing existing directory (tests/case/dir)
 - Creating directory (tests/case/dir)
 - Creating (tests/case/dir/header.hpp)
 - Creating (tests/case/dir/HEADER.hpp)

Running tests
tests/hardlink/main.cpp: In function ‘int main()’:
tests/hardlink/main.cpp:11:15: error: ‘foo’ is not a member of ‘Hardlink’; did you mean ‘Original::foo’?
   11 |     Hardlink::foo();
      |               ^~~
In file included from tests/hardlink/main.cpp:2:
tests/hardlink/header.hpp:3:5: note: ‘Original::foo’ declared here
    3 | int foo() { return 42; }
      |     ^~~
tests/symlink/main.cpp: In function ‘int main()’:
tests/symlink/main.cpp:11:14: error: ‘foo’ is not a member of ‘Symlink’; did you mean ‘Original::foo’?
   11 |     Symlink::foo();
      |              ^~~
In file included from tests/symlink/main.cpp:2:
tests/symlink/header.hpp:3:5: note: ‘Original::foo’ declared here
    3 | int foo() { return 42; }
      |     ^~~
tests/duplicate/main.cpp: In function ‘int main()’:
tests/duplicate/main.cpp:11:16: error: ‘foo’ is not a member of ‘Duplicate’; did you mean ‘Original::foo’?
   11 |     Duplicate::foo();
      |                ^~~
In file included from tests/duplicate/main.cpp:2:
tests/duplicate/header.hpp:3:5: note: ‘Original::foo’ declared here
    3 | int foo() { return 42; }
      |     ^~~
```

### MSVC 2022

```bash
$ python run.py msvc
Setting up 'duplicate' test
 - Removing existing file (tests/duplicate/duplicate.hpp)
 - Creating duplicate of header.hpp
 - Updating modification time

Setting up 'hardlink' test
 - Removing existing hardlink (tests/hardlink/hardlink.hpp)
 - Creating hardlink of header.hpp

Setting up 'symlink' test
 - Removing existing symlink (tests/symlink/symlink.hpp)
 - Creating symlink of header.hpp

Setting up 'case' test
 - Removing existing directory (tests/case/dir)
 - Creating directory (tests/case/dir)
 - Creating (tests/case/dir/header.hpp)
 - Creating (tests/case/dir/HEADER.hpp)

Running tests
Microsoft (R) C/C++ Optimizing Compiler Version 19.31.31104 for x86
Copyright (C) Microsoft Corporation.  All rights reserved.

main.cpp
tests/case/main.cpp(11): error C2039: 'foo': is not a member of 'Upper'
tests/case/main.cpp(5): note: see declaration of 'Upper'
tests/case/main.cpp(11): error C3861: 'foo': identifier not found
Microsoft (R) C/C++ Optimizing Compiler Version 19.31.31104 for x86
Copyright (C) Microsoft Corporation.  All rights reserved.

main.cpp
Microsoft (R) C/C++ Optimizing Compiler Version 19.31.31104 for x86
Copyright (C) Microsoft Corporation.  All rights reserved.

main.cpp
Microsoft (R) C/C++ Optimizing Compiler Version 19.31.31104 for x86
Copyright (C) Microsoft Corporation.  All rights reserved.

main.cpp
Microsoft (R) C/C++ Optimizing Compiler Version 19.31.31104 for x86
Copyright (C) Microsoft Corporation.  All rights reserved.

main.cpp
```