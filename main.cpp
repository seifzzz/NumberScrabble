#include <iostream>
#include <string>
using namespace std;

int main(){
cout<<"                              Welcome To 13Rot Chipper                          ";
cout<<"Do You Want To 1-Chipper Or 2-Dichipper?"<<endl<<"1 or 2: ";
int choice;
cin>>choice;
if(choice==1) {
cin.ignore();
string input;
string name;
string alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
string space="  ";
int  sum;
cout<<"Enter Your Message to Chipper: ";
getline(cin,input);
int length = input.size();
for (int counter=0;counter<=length;counter++){
   if(name[counter]==space[0]){
       name=name+space;
   }
   for (int i=0;i<=51;i++){
     if (input[counter]==alpha[i]){
     if ((i+13)>25){
            sum = (i-13);
}
     else{ sum =(i+13);
        }
        if((i>=26)&&(i<=51)){
            if((i+13>=51)){
                sum=(i-13);
            }
        else{
            sum=(i+13);
        }


        }

name=name+alpha[sum];
 }


 }

}


 cout<<name;
 }

 else if(choice==2){
cin.ignore();
string input2;
string name2;
string letters="abcdefghijklmnopqrstuvwxyz";
string space1=" ";
int total ;
cout<<"Enter Your Message To Dichpper: ";
getline(cin,input2);
int length1=input2.size();
for(int n=0;n<=length1;n++){
for(int x=0;x<=25;x++){
    if(input2[n]==letters[x]){
        if((x+13)>25){
            total=(x-13);
        }
    else {
        total=(x+13);
    }




    name2=name2+letters[total];

    }



}

}
cout<<name2;
 }
return 0;




 }











































































