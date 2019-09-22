#include <iostream> 
#include <string> 
using namespace std; 
int main(){ 

string s;
char pin[9][4]={{},{'a','b','c'},{'d','e','f'},{'g','h','i'},{'j','k','l'},{'m','n','o'},{'p','q','r','s'},{'t','u','v'},{'w','x','y','z'}};
string a;
int k=0;
    while(cin>>a){
        k=0;
        for(int i=1; i<a.size(); i++){
             if(a[i-1]<'0'||a[i-1]>'9'){
                 cout<<a[i-1];
             }
             if(a[i-1]==a[i]){
                 k++;
             }
             else{
                 cout<<pin[a[i-1]-'0'-1][k];
                 k=0;
             }
        }
        if(a[a.size()-1]<'0'||a[a.size()-1]>'9'){
             cout<<a[a.size()-1];
             continue;
        }
        cout<<pin[a[a.size()-1]-'0'-1][k]<<" ";
        k=0;
        //cout<<s<<endl;
   }
return 0;
}