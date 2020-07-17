# --------------- Declara��o dos Par�metros Iniciais -----------------------

param n;
# N�mero total de clientes

param m;
# N�mero total de clientes

# --------------------- Declara��o dos Conjuntos ---------------------------

set C := 1..n;
# conjunto das cidades a serem visitadas

set N := 0..(n+1);
# conjuntos das cidades + dep�sito (0, n+1)

#set N0 := 0..n;
# conjuntos das cidades + dep�sito (0, n+1)

#set N1 := 1..(n+1);
# conjuntos das cidades + dep�sito (0, n+1)

set K := 1..m;
# conjunto dos ve�culos

# --------------------- Declara��o dos Par�metros ---------------------------

param c {i in N, j in N};
# Matriz com o custos de transporte entre as cidades i e j, com i <> j

param t {i in N, j in N};
# Matriz com o tempo de viagem entre as cidades i e j, com i <> j

param d {j in C};
# Demanda de entrega do cliente j, J=1..n

param p {j in C};
# Demanda de entrega do cliente j, J=1..n

param ts {i in N}; 
#Tempo de servi�o de cada cliente i

param a {i in N};
# inicio da janela de atendimento

param b {i in N};
# fim da janela de tempo

param Q {k in K};
# capacidade dos ve�culos

param M;
# constante de valor elevado

# --------------------- Declara��o das vari�veis ---------------------------

var x {i in N, j in N, k in K}, binary;
# 1 se o ve�culo sai do cliente i e vai pro cliente j, usando o ve�culo k
# 0 caso contr�rio.

var s {i in N, k in K}, >=0; 
# instante de tempo em que o ve�culo k come�a a servir o cliente i.

var y {i in N, j in N}, >=0;
# Demanda coletada dos clientes na rota at� o cliente i (incluindo o cliente i) e transportada at� o cliente j.

var z {i in N, j in N}, >=0;
# Demanda a ser entregue aos clientes da rota ap�s o cliente i e transportada at� o cliente j.

# ------------------------- Fun��o Objetivo --------------------------------

minimize custo: sum {i in N, j in N, k in K: (i != j) && (i != n+1) && (j != 0) } c[i,j] * x[i,j,k];
# minimiza o custo total de transporte

# ---------------------- Restri��es do Problema ----------------------------

s.t. RV2 {i in C} : sum {j in N, k in K} x[i,j,k] = 1;

# s.t. RV3 {k in K} : sum {i in C, j in N} d[i]*x[i,j,k] <= Q[k];

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