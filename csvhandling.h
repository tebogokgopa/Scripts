#ifndef CSVHANDLING_H_INCLUDED
#define CSVHANDLING_H_INCLUDED
#include<string>
#include<stdio.h>
#include <iostream>
using namespace std;
namespace csv{


string show_headers(string filename, char delimeter);

void get_csv_content(string filename);
bool getFileContent(string filename,vector <string>& vecOfStrs);

}

#endif // CSVHANDLING_H_INCLUDED
