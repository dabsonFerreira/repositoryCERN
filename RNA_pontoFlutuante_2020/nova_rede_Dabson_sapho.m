%multiplicar camada de entrada por valores de entrada e os somar    
clear all;
IW = fopen('IW.txt');
w = fscanf(IW,'%f', [10 4] );
fclose(IW);
w = w';

B1 = fopen('B1.txt');
bias = fscanf(B1,'%f');
fclose(B1);

Signal_test = fopen('Signal_test_quant.txt');
y1 = fscanf(Signal_test,'%f' );
fclose(Signal_test);

LUT = fopen('LUT_tansig123.txt');
lut = fscanf(LUT,'%f', [64 1]);
fclose(LUT);
lut = lut';


%se eu ficar num loop com y1 pegando outras partes do sinal, posso cobrir o sinal inteiro
y1 = round(y1(1:10));
for i = 1:4
    for b = 1:10
        produto(i,b) = w(i,b)*y1(b);%eu não sei pq Mateus repetiu isso com as 200 partes do sinal de teste. Era treinando a rede?
    end
end

soma = zeros(1,4);
for i = 1:4
    for b = 1:10        
        soma(i) = soma(i)+produto(i,b);        
    end
    soma(i) = soma(i) + bias(i);
end
%save soma_in soma;
%deve-se fazer uma tangente hiperbólica agora e conferir os valores dentro da tabela LUT?
for i = 1:length(soma(:,1))
    for b = 1:length(soma(1,:))
        lutx(i,b) = abs(fix(soma(i,b)*2^4));
        if soma(i,b) < 0
            a(i,b) = true;
        end
    end
end

for i = 1:length(lutx(:,1))
    for b = 1:length(lutx(1,:))
        if lutx(i,b) <= length(LUT)
            resultado(i,b) = lut(lutx(i,b))/2^6;
            if a(i,b)
                resultado(i,b) = -resultado(i,b);
            end
        else
            resultado(i,b) = lut(length(LUT))/2^6;
            if a(i,b)
                resultado(i,b) = -resultado(i,b);
            end
        end
        
    end
end
%os números não batem com a tabela exatamente. 
%salve qm eh negativo pois o resultado final deve ser negativo