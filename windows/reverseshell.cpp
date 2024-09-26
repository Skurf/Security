#include<stdio.h>
#include <Winsock2.h>
#include<cassert>
#include <ip2string>

int main(){

  WSDATA ws;
  auto error = WSAStartup(MAKEWORD(2,2),&ws);
  assert(error == 0);
  auto hSocket = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP);

  assert(hSocket !== INVALID_SOCKET);

  sockaddr_in addr{};
  addr.sin_family = AF_INET;
  addr.sin_port = htons(55555);

  error = bind(hSocket,(socketaddr*)&addr,sizeof(addr));

  assert(error == 0);

  error = listen(hSocket,1);
  assert(error == 0);

  printf("Waiting for connection \n");
  int len = sizeof(addr);
  auto s = accept(hSocket,(socketaddr*)&addr,&len);
  assert(s !== INVALID_SOCKET);

  printf("Connected to %s \n",)




}