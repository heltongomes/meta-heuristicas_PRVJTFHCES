/*
MODELO MATEM�TICO DE PROGRAMA��O LINEAR INTEIRA PARA O PRVJTFHCES

@autor: Helton Gomes
*/

# --------------- DECLARA��O DOS PAR�METROS INICIAIS -----------------------

# N�MERO TOTAL DE CLIENTES
param n;

# N�MERO TOTAL DE VE�CULOS
param m;


# --------------------- DECLARA��O DOS CONJUNTOS -------------------------------

# CONJUNTO DE CLIENTES A SEREM ATENDIDOS
set C := 1..n;

# CONJUNTO DE CLIENTES A SEREM ATENDIDOS MAIS O DEP�SITO (0, n+1)
set N := 0..(n+1);

# CONJUNTO DE VE�CULOS
set K := 1..m;

# --------------------- DECLARA��O DOS PAR�METROS -------------------------------

# Matriz com o custos de transporte entre as cidades i e j, com i <> j
param c{i in N, j in N};

# Matriz com o tempo de viagem entre as cidades i e j, com i <> j
param t{i in N, j in N};

# Demanda de entrega do cliente j (j = 1, ..., n)
param d{j in C};

# Demanda de entrega do cliente j (j = 1, ..., n)
param p{j in C};

# Tempo de servi�o de cada cliente i
param ts{i in N}; 

# Inicio da janela de atendimento de cada cliente i
param a{i in N};

# Fim da janela de tempo de cada cliente i
param b{i in N};

# Capacidade de cada ve�culo k
param Q{k in K};

# Constante de valor elevado
param M;

# --------------------- DECLARA��O DAS VARI�VEIS ---------------------------------

# 1 se o ve�culo k sai do cliente i e vai pro cliente j
# 0 caso contr�rio.
var x{i in N, j in N, k in K}, binary;

# Instante de tempo em que o ve�culo k come�a a servir o cliente i
var s {i in N, k in K}, >=0; 

# Demanda coletada dos clientes na rota at� o cliente i (incluindo o cliente i) e transportada at� o cliente j
var y {i in N, j in N}, >=0;

# Demanda a ser entregue aos clientes da rota ap�s o cliente i e transportada at� o cliente j
var z {i in N, j in N}, >=0;

# ------------------------- FUN��O OBJETIVO -----------------------------------------

# Minimiza o custo total de transporte
minimize custo: sum {i in N, j in N, k in K: (i != j) && (i != n+1) && (j != 0) } c[i,j] * x[i,j,k];

# ---------------------- RESTRI��ES DO PROBLEMA ------------------------------------

s.t. RV2 {i in C} : sum {j in N, k in K} x[i,j,k] = 1;

s.t. RV3a{j in C} : sum {i in N: i != j} y[j,i] - sum {i in N: i != j} y[i,j] = p[j];

s.t. RV3b{j in C} : sum {i in N: i != j} z[i,j] - sum {i in N: i != j} z[j,i] = d[j];

s.t. RV3c{i in N, j in N: i != j} :  y[i,j] + z[i,j] -  (sum {k in K} Q[k] * x[i,j,k]) <= 0;

s.t. RV5 {k in K} : sum {j in N} x[0,j,k] = 1;

s.t. RV6 {h in C, k in K}: (sum {i in N} x[i,h,k]) - (sum {j in N} x[h,j,k]) = 0;

s.t. RV7 {k in K} : sum {i in N} x[i,n+1,k] = 1;

s.t. RV11a {i in N, k in K: i != 0}: s[i,k] >= a[i];

s.t. RV11b {i in N, k in K: i != 0}: s[i,k] <= b[i];

s.t. RV12 {i in N, j in N, k in K: (i != j) && (i != n+1) && (j != 0)}: s[i,k] + ts[i] + t[i,j] <= s[j,k] + (1 - x[i,j,k])*M;

s.t. RV13 {i in N, k in K}: x[i,i, k] = 0;

s.t. RV14 {i in N, k in K}: x[i, 0, k] = 0;

s.t. RV15 {k in K}: x[0, n+1, k] = 0;

end;