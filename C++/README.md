# Unit Testing in C++

## Running C++ locally
Just some details on how to spin up C++ debugging and testing on local if your IDE is not already set up to do so.

### MinGW-w64
I've used Minimalistic GNU to compile my C++ locally and create an executable in the directory which is then used to run my C++ code locally and do my unit testing. 
MinGW link - https://www.mingw-w64.org/ 

### In VS Code
After following the steps to install MinGW, in VS Code, I opened a new terminal and called the compiler "g++", then told it which C++ file to compile "main.cpp" and to create a new executable file "-o" called runme "runme". 
"g++ main.cpp -o runme" compiles the .cpp file and creates a runme.exe which can run the code locally.
Other additional system settings are added in the .vscode folder.

## The cppunit unit testing Framework
This unit testing exercise will use the C++ unit testing framework called "cppunit".

### Installation
Follow instructions from https://freedesktop.org/wiki/Software/cppunit/ and clone git repo to local directory.
git clone git://anongit.freedesktop.org/git/libreoffice/cppunit/
After cloning the repo in a folder cppunit, our main.cpp can now #include the library locally.

### Testing in VS Code terminal using cppunit
Command: g++ main.cpp -lcppunit -o runme
-l informs that we are using a library, then followed by the library name cppunit

### Key takeaways from using cppunit
#### Determine what is a valid test in a C++ app using cppunit library
- TestCaller is NOT a test.
- Two asserts in one function DO NOT result in two tests.
- An assert DOES NOT count as as test, a function does.
- A function with a single assert IS a test.
- An assert IS NOT a test, a function IS a test.

##### More on assert functions
- https://web.archive.org/web/20180601221213/http://cppunit.sourceforge.net/doc/lastest/group___assertions.html 

## Basic physics engine
We create a basic physics engine which is inside the src folder. The files physics.cpp and physics.h provide an implementation of a Thing class later usied in main.cpp to perform tests.

