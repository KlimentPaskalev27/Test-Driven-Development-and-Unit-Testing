// Include the TestCase header of the cppunit
#include <cppunit/TestCase.h>


class BasicTest : public CppUnit::TestCase {
    public:
    BasicTest( std::string name ) : CppUnit::TestCase( name ) {

        void runTest() override 
        {
            CPPUNIT_ASSERT( 2 + 2 == 4);
            CPPUNIT_ASSERT( 2 + 2 == 3);
        }
    }
}

int main ()
{
    BasicTest test{"BasicTest"};
    test.runTest();
}


//use in terminal -lcppunit to tell it that we are using a library called cppunit -> g++ main.cpp -lcppunit -o runme