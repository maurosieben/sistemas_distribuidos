
//Inclui as bibliotecas
#include <Thread.h>
#include "string.h"
#include <stdio.h>
#include <stdlib.h>
// Define os pinos de entrada analógica
int AN0= A0;
int AN1= A1;
int AN2= A2;

// Inclui as variaveis globais do programa
int temperatura, vazao, pressao,aux_calc,tempo=0;
int  quantidade = 0;
int set_temp_min = 10;
int set_temp_max = 60;
int set_tempo=0;
char requisicao= ' ';
char processo = 'F';
bool start, pulso=false;
int x=0;
String sensores = String(10);
String teste= String(5);
String conv_quantidade= String(5);
String rx_buffer = String(100);
char matriz[100];
char str_set_T[3];
String str_tempo,str_quantidade,str_vazao,str_pressao,str_temperatura,str_rx_buffer;

// Declaração das threads do sistema
Thread analogicos = Thread();
Thread supervisorio = Thread();
Thread controle = Thread();
Thread timer = Thread();

// Chamada das threads
void leitura(){
  aux_calc = analogRead(AN0)/10.23;
 temperatura = aux_calc*1.5;
 aux_calc = analogRead(AN1)/10.23;
 vazao = aux_calc * 0.5;
 aux_calc = analogRead(AN2)/10.23;
 pressao = aux_calc *1;

}
void relogio(){
   if (set_tempo > 0){
    set_tempo = set_tempo - 1;
     tempo = set_tempo;
      processo = 'R';
    }
   if (set_tempo <= 0)
    {
      tempo = 0;
      set_tempo = 0;
      processo = 'F';
      start = false;
    }
  quantidade = quantidade + vazao;//+ integrar; 
    delay(1000);
}

void control(){
  if(start==true){
    digitalWrite(22,HIGH);
  }
  else
  {
    digitalWrite(22,LOW);
  }
 if(temperatura >= set_temp_max){
    digitalWrite(24,HIGH);
  }
  else
  {
    digitalWrite(24,LOW);
  }
   if(temperatura <= set_temp_min){
    digitalWrite(26,HIGH);
  }
  else
  {
    digitalWrite(26,LOW);
  }
}
void dados(){

while (Serial.available()>0) { 
   requisicao = Serial.read();
  
   //Inicia verificação dos dados seriais
  switch (requisicao){
  case 'L':
   // Complementos de string temperatura=============
      if (temperatura >= 100)
      {
       teste = String(temperatura);
      }
       if (temperatura < 10)
      {
       teste =  "00" + String(temperatura);
      }
      if (temperatura >=10 && temperatura< 100)
      {
       teste = "0" + String(temperatura);
      }
      str_temperatura = teste;
     
      // Complementos de string pressão=============
      if (pressao >= 100)
      {
       teste = String(pressao);
      }
       if (pressao < 10)
      {
       teste =  "00" + String(pressao);
      }
      if (pressao >=10 && pressao< 100)
      {
       teste = "0" + String(pressao);
      }
      str_pressao =  teste;
     
     // Complementos de string vazão=============
      if (vazao >= 100)
      {
       teste = String(vazao);
      }
       if (vazao < 10)
      {
       teste =  "00" + String(vazao);
      }
      if (vazao >=10 && vazao< 100)
      {
       teste = "0" + String(vazao);
      }
      str_vazao =  teste;
     // Complementos de string quantidade=============
      if (quantidade >= 1000)
      {
       conv_quantidade = String(quantidade);
      }
       if (quantidade >= 100 && quantidade < 1000)
      {
       conv_quantidade = "0" + String(quantidade);
      }
       if (quantidade >=10 && quantidade < 100)
      {
       conv_quantidade = "00" + String(quantidade);
      }
      if (quantidade < 10)
      {
       conv_quantidade =  "000" + String(quantidade);
      }
      str_quantidade =  conv_quantidade;
     
     // Complementos de string tempo=============
      if (tempo >= 100)
      {
       teste = String(tempo);
      }
       if (tempo < 10)
      {
       teste =  "00" + String(tempo);
      }
      if (tempo >=10 && tempo< 100)
      {
       teste = "0" + String(tempo);
      }
      str_tempo =  teste;
     
     //================================================
      delayMicroseconds(1000);
        // Formato dos dados enviados
        //#T#VALOR#P#VALOR#V#VALOR#Q#VALOR#
    
     Serial.println("#T#" + str_temperatura + "#V#" + str_vazao + "#P#" + str_pressao + "#Q#" + str_quantidade + "#" + processo + "#" + str_tempo + '#');
    
      delayMicroseconds(1000);
  break;
  case 'E':
   //Serial.println("ESCRITA");
    //rx_buffer = Serial.read();
   rx_buffer = Serial.readString();
  // Serial.println(rx_buffer);
   delayMicroseconds(1000);
   // separar os dados de string
    int size_dados=rx_buffer.length();
    int contagem=0;
     quantidade = 0;
     start = true;
     
    for (contagem;contagem <=size_dados;contagem++){
      //#T#60#t#10#S#10#

      // Trata o set de temperatura maxima
       if(rx_buffer[contagem]== 'T')
      {
         str_set_T[0]= rx_buffer[contagem + 2];
         str_set_T[1]= rx_buffer[contagem + 3];
         str_set_T[2]= rx_buffer[contagem + 4];
         if( str_set_T[2] == '#')
         {
           char tmp1[2];
           tmp1[0]=str_set_T[0];
           tmp1[1]=str_set_T[1];
           set_temp_max = atoi(tmp1);
        }
         else{
           set_temp_max = atoi(str_set_T);
        }
      }

        // Trata o set de temperatura minima
       if(rx_buffer[contagem]== 't')
      {
            
         str_set_T[0]= rx_buffer[contagem + 2];
         str_set_T[1]= rx_buffer[contagem + 3];
         str_set_T[2]= rx_buffer[contagem + 4];
         if( str_set_T[2] == '#')
         {
           char tmp1[2];
           tmp1[0]=str_set_T[0];
           tmp1[1]=str_set_T[1];
           set_temp_min = atoi(tmp1);
        }
         else
         {
           set_temp_min = atoi(str_set_T);
        }
        
      }
      //Recebe start de processo e tempo
      if(rx_buffer[contagem]== 'S')
      {
         str_set_T[0]= rx_buffer[contagem + 2];
         str_set_T[1]= rx_buffer[contagem + 3];
         str_set_T[2]= rx_buffer[contagem + 4];
         if( str_set_T[2] == '#')
         {
           char tmp1[2];
           tmp1[0]=str_set_T[0];
           tmp1[1]=str_set_T[1];
           set_tempo = atoi(tmp1);
        }
         else
         {
           set_tempo = atoi(str_set_T);
        }
        
      }
       
      }
    
       Serial.println(quantidade);
       delayMicroseconds(1000);

   //==================================
  break;
 // default :
 //    Serial.println("NAO IDENTIFICADO");
//  break;
  }
 // }
 }     
}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  analogicos.onRun(leitura);
  analogicos.setInterval(80);
  supervisorio.onRun(dados);
  supervisorio.setInterval(500);
  controle.onRun(control);
  controle.setInterval(800);
  timer.setInterval(500);
  timer.onRun(relogio);
  pinMode(22, OUTPUT);
  pinMode(24, OUTPUT);
  pinMode(26, OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  analogicos.run();
  supervisorio.run();
  controle.run();
  if(start == true)
  {
    
    timer.run();
  }
  if (processo == 'F'){
    start = false;
  }
  
 
  
}
