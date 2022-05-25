clear all;
%camada de entrada



%Sinal de entrada
Signal_test = fopen('sinaladc.txt');
yy1 = fscanf(Signal_test,'%f' );
fclose(Signal_test);
yy1 = yy1(1:2000);

%tab
B1 = fopen('LUT_tansig123.txt');
tab = fscanf(B1,'%f');
fclose(B1);

B1 = fopen('LUT_tansig4.txt');
tab4 = fscanf(B1,'%f');
fclose(B1);


%% camda de entrada
%soma = zeros(200,4);
for n = 1:200%length(y1)/10
    
    
    y0=yy1(n);
    y1=yy1(n+1);
    y2=yy1(n+2);
    y3=yy1(n+3);
    y4=yy1(n+4);
    y5=yy1(n+5);
    y6=yy1(n+6);
    y7=yy1(n+7);
    y8=yy1(n+8);
    y9=yy1(n+9);
    
    soma1(n) = ((6*y0 + 34*y2 + 191*y4 + 188*y6 + 47*y8 ) - (1018 + 16*y1 +78*y3 + 321*y5 + 100*y7 + 15*y9))/64;
    soma2(n) = ((25*y1 + 154*y3 + 159*y5 + 46*y7 + 7*y9) - (1086 + 8*y0 + 64*y2 + 255*y4 + 89*y6 + 22*y8 ))/64;
    soma3(n) = ((14*y0 + 143*y2 + 154*y4 + 43*y6 + 10*y8 ) - (1194 + 53*y1 + 255*y3 + 81*y5 + 22*y7 + 3*y9))/64;
    soma4(n) = ((145617 +62*y0 + 489*y2 + 1937*y4 + 667*y6 + 164*y8 ) - (194*y1 + 1174*y3 + 1198*y5 + 351*y7 + 54*y9))/64;

    
   
    


    
   %neuronio1
    if soma1(n)*64 < 3072 && soma1(n)*64 >= 0 && soma1(n) < 64 || soma1(n)*64 > -3072 && soma1(n)*64 < 0 && -soma1(n) < 64            
        if soma1(n) > 0
            lute_out_n_1(n) = tab(fix(abs((soma1(n))))+1)*2816;
        else
            lute_out_n_1(n) = -tab(fix(abs((soma1(n))))+1)*2816;
        end

    else 
        if soma1(n) > 0
            lute_out_n_1(n) = 63*2816;               
        else
            lute_out_n_1(n) = -64*2816;
        end
    end
    
     %neuronio2
    if soma2(n)*64 < 3072 && soma2(n)*64 >= 0 && soma2(n) < 64 || soma2(n)*64 > -3072 && soma2(n)*64 < 0 && -soma2(n) < 64           
        if soma2(n) > 0
            lute_out_n_2(n) = tab(fix(abs((soma2(n))))+1)*5120;
        else
            lute_out_n_2(n) = -tab(fix(abs((soma2(n))))+1)*5120;
        end

    else 
        if soma2(n) > 0
            lute_out_n_2(n) = 63*5120;               
        else
            lute_out_n_2(n) = -64*5120;
        end
    end
    
     %neuronio3
    if ((soma3(n)*64 < 3072 && soma3(n)*64 >= 0 && soma3(n) < 64) || (soma3(n)*64 > -3072 && soma3(n)*64 < 0 && -soma3(n) < 64))           
        if soma3(n) > 0
            lute_out_n_3(n) = tab(fix(abs((soma3(n))))+1)*3840;
        else
            lute_out_n_3(n) = -tab(fix(abs((soma3(n))))+1)*3840;
        end

    else 
        if soma3(n) > 0
            lute_out_n_3(n) = 63*3840;               
        else
            lute_out_n_3(n) = -64*3840;
        end
    end

   %neuronio4
    if soma4(n)*64 < 1048576 && soma4(n)*64 >= 0 && soma4(n) < 32769 || soma4(n)*64 > -1048576 && soma4(n)*64 < 0 && -soma4(n) < 32769            
       if soma4(n) > 0
            lute_out_n_4(n) = tab4(fix(abs((soma4(n))))+1)*2716;
        else
            lute_out_n_4(n) = -tab4(fix(abs((soma4(n))))+1)*2716;
        end

    else 
        if soma4(n) > 0
            lute_out_n_4(n) = 15794*2716;               
        else
            lute_out_n_4(n) = -15795*2716;
        end
    end    
     
    saida_rede = lute_out_n_2 + lute_out_n_4 - (lute_out_n_1 + lute_out_n_3 + 6200193); 
        
end
