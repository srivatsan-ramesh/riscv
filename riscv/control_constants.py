SRC_A_SEL_WIDTH = 2
SRC_A_RS1 = 0
SRC_A_PC = 1
SRC_A_ZERO = 2

SRC_B_SEL_WIDTH = 2
SRC_B_RS2 = 0
SRC_B_IMM = 1
SRC_B_FOUR = 2
SRC_B_ZERO = 3

PC_SRC_SEL_WIDTH = 3
PC_PLUS_FOUR = 0
PC_BRANCH_TARGET = 1
PC_JAL_TARGET = 2
PC_JALR_TARGET = 3
PC_REPLAY = 4
PC_HANDLER = 5
PC_EPC = 6

IMM_TYPE_WIDTH = 2
IMM_I = 0
IMM_S = 1
IMM_U = 2
IMM_J = 3

WB_SRC_SEL_WIDTH = 2
WB_SRC_ALU = 0
WB_SRC_MEM = 1
WB_SRC_CSR = 2
WB_SRC_MD = 3

MEM_TYPE_WIDTH = 3
MEM_TYPE_LB = 0
MEM_TYPE_LH = 1
MEM_TYPE_LW = 2
MEM_TYPE_LD = 3
MEM_TYPE_LBU = 4
MEM_TYPE_LHU = 5
MEM_TYPE_LWU = 6

MEM_TYPE_WIDTH = 3
MEM_TYPE_SB = 0
MEM_TYPE_SH = 1
MEM_TYPE_SW = 2
MEM_TYPE_SD = 3

HTIF_PCR_WIDTH = 64