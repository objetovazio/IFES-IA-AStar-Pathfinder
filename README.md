# IFES-IA-AStar-Pathfinder
 This is a repository to the first activity of the IA class on IFES.

# How to execute

Para execução do algoritmo foram criados dois arquivos de main() diferentes, são eles:

- main.py – Arquivo que recebe parâmetros através do terminal, sendo eles o nome do arquivo e duas coordenadas no labirinto. Um exemplo de uso: `python .\main.py .\Mapa_B.txt 2,3 14,3`
  
- mainV2.py – Arquivo utilizado para testar vários pontos aleatórios em massa. Todos os parâmetros estão atribuídos dentro do código, não são aceitos parâmetros via linha de comando. Recomendo o uso do operador `>` para recuperar a saída do programa. Um exemplo de uso: `python .\mainV2.py > output.csv`

No arquivo mainV2.py é utilizado a biblioteca NumPy para gerar coordenadas aleatórias. Portanto é necessário a instalação da biblioteca utilizando o comando `pip install numpy`.