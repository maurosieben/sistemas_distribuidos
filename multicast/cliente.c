//Cliente multicast 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <time.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define MAXBUFSIZE 1000 

int main()
{
   int sock, status, socklen;
   unsigned char buffer[MAXBUFSIZE];
   struct sockaddr_in saddr;
   struct in_addr iaddr;
   unsigned char ttl = 3;
   unsigned char one = 1;
   struct ip_mreq imreq;
     
   memset(&saddr, 0, sizeof(struct sockaddr_in));
   memset(&iaddr, 0, sizeof(struct in_addr));

   // Abre socket UDP
   sock = socket(PF_INET, SOCK_DGRAM, 0);
   if ( sock < 0 )
   {
     perror("Erro socket");
     exit(0);
   }

   saddr.sin_family = PF_INET;
   saddr.sin_port = htons(0); // Utiliza a primeira porta livre
   saddr.sin_addr.s_addr = htonl(INADDR_ANY); // Associa o socket com as interfaces
   status = bind(sock, (struct sockaddr *)&saddr, sizeof(struct sockaddr_in));

   if ( status < 0 )
   {
     perror("Error bind");
     exit(0);
   }

   iaddr.s_addr = INADDR_ANY; // Usa a interface DEFAULT
   
   setsockopt(sock, IPPROTO_IP, IP_MULTICAST_IF, &iaddr,
              sizeof(struct in_addr));

   // TTL = 3
   setsockopt(sock, IPPROTO_IP, IP_MULTICAST_TTL, &ttl,
              sizeof(unsigned char));

   // Envia o tráfego multicast também para a própria máquina
   status = setsockopt(sock, IPPROTO_IP, IP_MULTICAST_LOOP,
                       &one, sizeof(unsigned char));
   
   // End. e porta de destino
   saddr.sin_family = PF_INET;
   saddr.sin_addr.s_addr = inet_addr("239.255.32.33");
   saddr.sin_port = htons(38000);
// ************************************************************* //
   
   system("clear");
   printf("\t##### Multicast client #####\n");
      
   //strcpy(buffer, "127");
   buffer[0] =10;
   buffer[1] =12;
   socklen = sizeof(struct sockaddr_in);

   printf("\tSending msg: \"I am the client.\"\n");
   
   // Envia
   status = sendto(sock, buffer, strlen(buffer), 0,
                     (struct sockaddr *)&saddr, socklen);

   // Recebe
   memset(&buffer, 0, sizeof(buffer));
      
   printf("\tWaiting for response...\n");
   
   status = recvfrom(sock, buffer, MAXBUFSIZE, 0, 
                     (struct sockaddr *)&saddr, &socklen);

   buffer[status] = '\0';

   printf("\tReceived data:\n\t%s\n\n", buffer);
     
   shutdown(sock, 2);
   close(sock);
   
   return 0;
}
