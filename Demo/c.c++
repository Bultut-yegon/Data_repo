#include <iostream>
#include <string>

using namespace std;

int main(){
    int a;
    cout<< "Enter the number of people ";
    cin>>a;

    for(int m=0; m<a; m++){
        string name;
        cout<< "Enter the name of the person ";
        cin>>name;
    }
    int r=0;
    while (r<10) {
        cout<<"You are welcome"<<endl;
        ++r;
    }// use 10 or a which will be 10
    if(r>=10){
        cout<<"Space full"<<endl;
    }

   return 0;
}