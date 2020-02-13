#include <iostream>
#include<vector>
#include<stdio.h>
#include<fstream>
#include<sstream>
#include<string>
#include "csvhandling.h"
using namespace std;
using namespace csv;

int main()
{
    cout<<endl;
    //show_headers("numbers.csv", ';');
    get_csv_content("numbers.csv");
/*
    vector<string> vecOfStr;

    bool result = getFileContent("numbers.csv",vecOfStr);

    if(result){
            cout<<vecOfStr[5]<<endl;
            cout<<vecOfStr[5]<<endl;
    }*/
    return 0;

}



