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
