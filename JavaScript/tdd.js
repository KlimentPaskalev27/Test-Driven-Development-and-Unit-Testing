// First iteration
function testRetVal()
{
    var input = [1,2,3,4,5,6];
    var res = getHighest(input);

    if (res == undefined) return false;
    else return true;
}

var res = testRetVal();

if (res) console.log("testRetVal passed");
else console.log("testRetVal failed");

// powershell terminal -> node thisFileName.js
// ReferenceError: getHighest is not defined

//Second iteration
function getHighest(input) {
    return 0;
}

function testRetVal()
{
    var input = [1,2,3,4,5,6];
    var res = getHighest(input);

    if (res == undefined) return false;
    else return true;
}

var res = testRetVal();

if (res) console.log("testRetVal passed");
else console.log("testRetVal failed");

// powershell terminal -> node thisFileName.js
// testRetVal passed

//Third iteration

function testResInArray()
{
    var input = [1,2,3];
    var res = getHighest(input);

    if (res == 1 || res ==2 || res == 3) return true;
    else return false;
}

function getHighest(input) {
    return 0;
}

function testRetVal()
{
    var input = [1,2,3,4,5,6];
    var res = getHighest(input);

    if (res == undefined) return false;
    else return true;
}

var res = testRetVal();
if (res) console.log("testRetVal passed");
else console.log("testRetVal failed");

var res = testResInArray();
if (res) console.log("testResInArray passed");
else console.log("testResInArray failed");
// powershell terminal -> node thisFileName.js
// testRetVal passed
//testResInArray failed


//Fourth iteration
function testResInArray()
{
    var input = [1,2,3];
    var res = getHighest(input);

    if (res == 1 || res ==2 || res == 3) return true;
    else return false;
}

function getHighest(input) {
    return input[0];
}

function testRetVal()
{
    var input = [1,2,3,4,5,6];
    var res = getHighest(input);

    if (res == undefined) return false;
    else return true;
}

var res = testRetVal();
if (res) console.log("testRetVal passed");
else console.log("testRetVal failed");

var res = testResInArray();
if (res) console.log("testResInArray passed");
else console.log("testResInArray failed");
// powershell terminal -> node thisFileName.js
// testRetVal passed
// testResInArray passed


//Fifth iteration
function testCorrectRes()
{
    var input = [1,2,3];
    var res = getHighest(input);

    if (res == 3) return true;
    else return false;
}

function testResInArray()
{
    var input = [1,2,3];
    var res = getHighest(input);

    if (res == 1 || res ==2 || res == 3) return true;
    else return false;
}

function getHighest(input) {
    return input[0];
}

function testRetVal()
{
    var input = [1,2,3,4,5,6];
    var res = getHighest(input);

    if (res == undefined) return false;
    else return true;
}

var res = testRetVal();
if (res) console.log("testRetVal passed");
else console.log("testRetVal failed");

var res = testResInArray();
if (res) console.log("testResInArray passed");
else console.log("testResInArray failed");

var res = testCorrectRes();
if (res) console.log("testCorrectRes passed");
else console.log("testCorrectRes failed");
// powershell terminal -> node thisFileName.js
// testRetVal passed
// testResInArray passed
// testCorrectRes failed




// Sixth iteration
function testCorrectRes()
{
    var input = [1,2,3];
    var res = getHighest(input);

    if (res == 3) return true;
    else return false;
}

function testResInArray()
{
    var input = [1,2,3];
    var res = getHighest(input);

    if (res == 1 || res ==2 || res == 3) return true;
    else return false;
}

function getHighest(input) 
{
    var max = input[0];
    for(var i =1; i< input.length; i++)
    {
        if (input[i] > max) max = input[i];
    }
    return max;
}

function testRetVal()
{
    var input = [1,2,3,4,5,6];
    var res = getHighest(input);

    if (res == undefined) return false;
    else return true;
}

var res = testRetVal();
if (res) console.log("testRetVal passed");
else console.log("testRetVal failed");

var res = testResInArray();
if (res) console.log("testResInArray passed");
else console.log("testResInArray failed");

var res = testCorrectRes();
if (res) console.log("testCorrectRes passed");
else console.log("testCorrectRes failed");
// powershell terminal -> node thisFileName.js
// testRetVal passed
// testResInArray passed
// testCorrectRes passed