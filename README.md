# fastapi-monitoramento-voos

Este projeto fornece uma API simples para monitoramento de voos utilizando FastAPI.

## Como executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicie o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```
3. A API estará disponível em `http://localhost:8000`. A documentação interativa pode ser acessada em `http://localhost:8000/docs`.

## Executando os testes

Execute os testes com:
```bash
pytest
```
