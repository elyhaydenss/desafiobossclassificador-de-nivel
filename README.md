# Verificador de Medalha

Este é um script Python que determina o nível de medalha com base no XP de um herói.

## Funcionamento

O script `verificar_medalha(xp)` recebe o XP do herói e o nome dele como entrada e retorna o nível de medalha correspondente.

- Se o XP for menor que 1000, o herói recebe a medalha de Ferro.
- Se o XP estiver entre 1001 e 2000, o herói recebe a medalha de Bronze.
- Se o XP estiver entre 2001 e 5000, o herói recebe a medalha de Prata.
- Se o XP estiver entre 5001 e 7000, o herói recebe a medalha de Ouro.
- Se o XP estiver entre 7001 e 8000, o herói recebe a medalha de Platina.
- Se o XP estiver entre 8001 e 9000, o herói recebe a medalha de Ascendente.
- Se o XP estiver entre 9001 e 10000, o herói recebe a medalha de Imortal.
- Se o XP for maior ou igual a 10001, o herói recebe a medalha de Radiante.
- Se o XP for inválido, retorna uma mensagem de erro.


