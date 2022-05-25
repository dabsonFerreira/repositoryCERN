module treinamento_dabson (
input clk, rst,
input signed [12:0] io_in,
output signed [20:0] io_out,
output [3:0] req_in,
output [3:0] out_en);

wire signed [20:0] in_float;
wire signed [20:0] out_float;

int2float #(.MAN(13),.EXP(7)) i2f (io_in, in_float);

wire proc_req_in, proc_out_en;
wire [1:0] addr_in;
wire [1:0] addr_out;

proc_fl #(.NBMANT(13),
.NBEXPO(7),
.MDATAS(100020),
.MINSTS(1077090),
.SDEPTH(4),
.NUIOIN(4),
.NUIOOU(4),
.CAL(1),
.SRF(1),
.EQU(1),
.LIN(1),
.LES(1),
.ADD(1),
.DIV(1),
.MLT(1),
.NEG(1),
.GRE(1),
.DFILE("C:/Users/ferre/Desktop/IC Luciano/Treniamento 2021/variaveis_06_05_21/treinamentoRedesNeurais/treinamento_dabson/Hardware/treinamento_dabson_H/treinamento_dabson_data.mif"),
.IFILE("C:/Users/ferre/Desktop/IC Luciano/Treniamento 2021/variaveis_06_05_21/treinamentoRedesNeurais/treinamento_dabson/Hardware/treinamento_dabson_H/treinamento_dabson_inst.mif")
) p_treinamento_dabson (clk, rst, in_float, out_float, addr_in, addr_out, proc_req_in, proc_out_en);

float2int #(.EXP(7),.MAN(13)) f2i (out_float, io_out);

addr_dec #(4) dec_in (proc_req_in, addr_in , req_in);
addr_dec #(4) dec_out(proc_out_en, addr_out, out_en);

endmodule
