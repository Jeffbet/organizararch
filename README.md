# organizararch

<h1>Organizador de Arquivos</h1>
Este script Python foi desenvolvido para organizar arquivos em categorias específicas com base em suas extensões. A organização é feita movendo os arquivos de uma pasta de origem para pastas de destino correspondentes.

Requisitos
Python 3.x instalado
PyInstaller (opcional, apenas se desejar criar um executável)
Como Usar
Opção 1: Executar o Script Python
Certifique-se de ter o Python 3.x instalado no seu sistema.

Abra um terminal.

Navegue até o diretório onde o script organizar.py está localizado.

Execute o seguinte comando:

bash
Copy code
python organizar.py
Siga as instruções no console para selecionar os diretórios de origem e destino.

Opção 2: Executar o Executável (Windows)
Se você não tiver o Python instalado, você pode usar o executável fornecido.
Baixe o executável aqui.
Execute o executável seguindo as instruções.
Personalização
O script organiza os arquivos com base nas seguintes condições padrão:

Documentos PDF: Arquivos com a extensão .pdf
Documentos de Texto: Arquivos com a extensão .txt
Outros: Todos os outros arquivos
Você pode personalizar essas condições diretamente no script organizar.py conforme necessário.

Criação de Executável (Opcional)
Se desejar criar um executável para facilitar a execução, você pode usar o PyInstaller. Execute o seguinte comando no terminal para criar um executável:

bash
Copy code
pyinstaller --onefile organizar.py
O executável será gerado na pasta dist.

Notas Importantes
Certifique-se de fornecer permissões adequadas para acessar e modificar os diretórios especificados.
O executável gerado é específico para o sistema operacional Windows.
Se você encontrar problemas ou erros, consulte a seção de Problemas Conhecidos ou Abra uma Issue.

Direitos Reservados developer: Jefferson Fonseca
