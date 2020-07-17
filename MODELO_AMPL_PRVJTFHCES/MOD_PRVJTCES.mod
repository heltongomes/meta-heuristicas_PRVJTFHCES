/*
MODELO MATEMÁTICO DE PROGRAMAÇÃO LINEAR INTEIRA PARA O PRVJTFHCES

@autor: Helton Gomes
*/

# --------------- DECLARAÇÃO DOS PARÂMETROS INICIAIS -----------------------

# NÚMERO TOTAL DE CLIENTES
param n;

# NÚMERO TOTAL DE VEÍCULOS
param m;


# --------------------- DECLARAÇÃO DOS CONJUNTOS -------------------------------

# CONJUNTO DE CLIENTES A SEREM ATENDIDOS
set C := 1..n;

# CONJUNTO DE CLIENTES A SEREM ATENDIDOS MAIS O DEPÓSITO (0, n+1)
set N := 0..(n+1);

# CONJUNTO DE VEÍCULOS
set K := 1..m;

# --------------------- DECLARAÇÃO DOS PARÂMETROS -------------------------------

# Matriz com o custos de transporte entre as cidades i e j, com i <> j
param c{i in N, j in N};

# Matriz com o tempo de viagem entre as cidades i e j, com i <> j
param t{i in N, j in N};

# Demanda de entrega do cliente j (j = 1, ..., n)
param d{j in C};

# Demanda de entrega do cliente j (j = 1, ..., n)
param p{j in C};

# Tempo de serviço de cada cliente i
param ts{i in N}; 

# Inicio da janela de atendimento de cada cliente i
param a{i in N};

# Fim da janela de tempo de cada cliente i
param b{i in N};

# Capacidade de cada veículo k
param Q{k in K};

# Constante de valor elevado
param M;

# --------------------- DECLARAÇÃO DAS VARIÁVEIS ---------------------------------

# 1 se o veículo k sai do cliente i e vai pro cliente j
# 0 caso contrário.
var x{i in N, j in N, k in K}, binary;

# Instante de tempo em que o veículo k começa a servir o cliente i
var s {i in N, k in K}, >=0; 

# Demanda coletada dos clientes na rota até o cliente i (incluindo o cliente i) e transportada até o cliente j
var y {i in N, j in N}, >=0;

# Demanda a ser entregue aos clientes da rota após o cliente i e transportada até o cliente j
var z {i in N, j in N}, >=0;

# ------------------------- FUNÇÃO OBJETIVO -----------------------------------------

# Minimiza o custo total de transporte
minimize custo: sum {i in N, j in N, k in K: (i != j) && (i != n+1) && (j != 0) } c[i,j] * x[i,j,k];

# ---------------------- RESTRIÇÕES DO PROBLEMA ------------------------------------

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