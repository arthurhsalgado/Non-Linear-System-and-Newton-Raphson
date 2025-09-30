# Tanque Agitado - Sistema Não Linear

1) Resolução do Sistema não linear

O sistema foi resolvido usando o código: "TanqueNaoL_1" e aplica as seguintes variavéis:

ca_in = 2000
V = 1
tau = 100
k0 = 10**6
DH = 4*10**4
rho = 10**3
cp = 4.18 * 10**3
UA = 2 * 10**4
E = 8* 10**4
Te = 330
Tc = 300
R = 8.314

Obtendo como resposta as concentrações de 1999.98 e Temperatura de 320.29. 

<p align="center">
  <img src="https://raw.githubusercontent.com/arthurhsalgado/Non-Linear-System-and-Newton-Raphson/1ec39167f191a0f8a886c80eb319512db7da4748/TanqueAgitado_1.png" width="400">
</p>

2) Resolução do sistema linear para o novo cenário:

O sistema foi resolvido para o novo cenário de variavéis, conforme:

ca_in = 2000
V = 1
tau = 50
k0 = 10**8
DH = 2*10**5
rho = 10**3
cp = 4.18 * 10**3
UA = 1.5 * 10**3
E = 7* 10**4
Te = 330
Tc = 280
R = 8.314

Para Ca = 600 e T = 305, obteve-se o par (Ca, T) = (1891, 334)
Para Ca = 1200 e T = 350, obteve-se o par (Ca, T) = (1891, 334)
Para Ca = 2000 e T = 420, obteve-se o par (Ca, T) = (1891, 334)

<p align="center">
  <img src="https://raw.githubusercontent.com/arthurhsalgado/Non-Linear-System-and-Newton-Raphson/f920e35712908663c8cc1b07d961bfc27602635d/TanqueAgitado_2.png" width="400">
</p>

3) Varredura de Condições Iniciais

<p align="center">
  <img src="https://raw.githubusercontent.com/arthurhsalgado/Non-Linear-System-and-Newton-Raphson/d8efae8a523eb3c6716920f3c974567d25a2d6cc/HeatMap_Ca.png" width="400">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/arthurhsalgado/Non-Linear-System-and-Newton-Raphson/d8efae8a523eb3c6716920f3c974567d25a2d6cc/HeatMap_T.png" width="400">
</p>

