#include<iostream>
#include<vector>
#include<stdio.h>
#include<fstream>
#include<sstream>
#include<string>
#include "csvhandling.h"
#include <bits/stdc++.h>
#include <algorithm>


using namespace std;

namespace csv{

string show_headers(string filename, char delimeter){
            ifstream csvfile;
            csvfile.open(filename.c_str(), ios_base::in);
            if(!csvfile.is_open()){
                cout<<"File "<<filename<<" not Found\n"<<endl;
                exit(EXIT_FAILURE);
            }
            cout<<"Headers for "<<filename<< "\n"<<endl;
            string line = " ";
            getline(csvfile,line);
            string word = "";
            for (auto x : line)
            {
                if (x == ' ' || x == delimeter)
                {
                    cout << word;
                    word = "||";
                }
                else
                {
                    word = word + x;
                }
            }
            cout<<endl;
            csvfile.close();
    return word;
}
bool getFileContent(string filename,vector <string>& vecOfStrs){

    ifstream csvfile(filename.c_str());

    if(!csvfile){
        cerr<<"Cannot open the file: "<<filename<<endl;
        return false;
    }

    string str;

    while(getline(csvfile,str)){
        if(str.size() > 0){
            vecOfStrs.push_back(str);
        }
    }

    csvfile.close();
    return true;
}

void get_csv_content(string filename){

        ifstream csvfile;
        csvfile.open(filename.c_str());

        if(!csvfile.is_open()){
            cout<<"Cannot open the file :: "<<filename<<endl;
            exit(EXIT_FAILURE);
        }
        cout<<"Found "<<filename<<" file\n"<<endl;

        vector<string> drawNo;
        vector<string> drawDate;
        vector<string> firstNumber;
        string line,word,temp;
        vector <string> stringvector;

        while(getline(csvfile,line)){

            istringstream iss(line);
            string linestream;
            //string::size_type sz;

            while(getline(iss,linestream,';')){

                stringvector.push_back(linestream);
            }
           /* int i = 0;
            drawNo.push_back(stringvector[i]);
            drawDate.push_back(stringvector[i+1]);
            firstNumber.push_back(stringvector[i+2]);
            i++;*/
        }

           for(size_t i = 0; i < drawNo.size();i ++){
                cout<<stringvector[i]<<'\t'<<stringvector[i]<<'\t'<<stringvector[i]<<endl;
           }

    csvfile.close();
}





}
