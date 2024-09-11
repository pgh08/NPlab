#include<bits/stdc++.h>
using namespace std;

pair<vector<char>,char> binaryAddition(vector<char> &b, vector<char> &zeros, char &carry){
    int n = b.size();
    vector<char> result;

    for(int i=n-1; i>=0; i--){
        int bitSum = (b[i]-'0') + (zeros[i]-'0') + (carry-'0');
        result.push_back((bitSum%2)+'0');
        carry = (bitSum/2) + '0';
    }

    reverse(result.begin(), result.end());

    return {result, carry};
}

void sender(vector<string> &a, int &n, vector<char> &checksum){
    int maxLen = 0;

    for(auto s : a){
        maxLen = max(maxLen, (int)s.length());
    }

    for(auto s : a){
        while(s.length() < maxLen){
            s = '0' + s;
        }
    }

    char carry = '0';
    vector<char> checkSum_result;

    for(int j=0; j<maxLen; j++){
        vector<char> b(n, '0');

        for(int i=0; i<n; i++){
            b[i] = a[i][j];
        }

        vector<char> zeros(n, '0');

        pair<vector<char>, char> resultCarry = binaryAddition(b, zeros, carry);
        carry = resultCarry.second;
        checkSum_result.insert(checkSum_result.end(), resultCarry.first.begin(), resultCarry.first.end());
    }

    for(auto bit : checkSum_result){
        checksum.push_back(bit == '0' ? '1' : '0');
    }

    cout<<"\nCarry = "<<carry<<"\nChecksum = ";
    for(auto bit : checkSum_result){
        cout<<bit;
    }
    cout<<endl;
}

void receiver(vector<string> &a, int &n, vector<char> &checksum){
    int maxLen = a[0].size();
    char carry = '0';

    vector<char> checksum_result;

    for(int j=0; j<maxLen; j++){
        vector<char> b(n, '0');

        for(int i=0; i<n; i++){
            b[i] = a[i][j];
        }

        vector<char> zeros(n, '0');
        pair<vector<char>, char> resultCarry = binaryAddition(b, zeros, carry);
        carry = resultCarry.second;
        checksum_result.insert(checksum_result.end(), resultCarry.first.begin(), resultCarry.first.end());
    }

    vector<char> temp;
    for(auto bit : checksum_result){
        temp.push_back(bit == '0' ? '1' : '0');
    }

    if(temp != checksum){
        cout<<"Error detected in message"<<endl;
    }
    else{
        cout<<"No error found in the message"<<endl;
    }
}

int main()
{
    int n;
    cout<<"Enter the number of input strings"<<endl;
    cin>>n;

    vector<string> a(n);
    vector<char> checksum;

    cout<<"From sender side......."<<endl;
    cout<<"Input string are : "<<endl;
    for(int i=0; i<n; i++){
        cin>>a[i];
    }

    sender(a, n, checksum);

    cout<<"\n\nFrom Receiver side for the checksum........"<<endl;
    for(char bit : checksum){
        cout<<bit;
    }
    cout<<endl;

    cout<<"Enter "<<n<<" input strings : "<<endl;
    for(int i=0; i<n; i++){
        cout<<"Enter the input binary string"<<endl;
        cin>>a[i];
    }

    receiver(a, n, checksum);

    return 0;
}