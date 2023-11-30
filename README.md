# organizararch

<h1>Organizador de Arquivos</h1>
Este script Python foi desenvolvido para organizar arquivos em categorias específicas com base em suas extensões. A organização é feita movendo os arquivos de uma pasta de origem para pastas de destino correspondentes.

<h2>Requisitos</h2>
<ul>
<li>Python 3.x instalado</li>
<li>PyInstaller (opcional, apenas se desejar criar um executável)</li>
</ul>

<h2>Como Usar</h2>
Opção 1: Executar o Script Python
Certifique-se de ter o Python 3.x instalado no seu sistema.

Abra um terminal.

Navegue até o diretório onde o script organizar.py está localizado.

<h2>Execute o seguinte comando:</h2>

'python organizar.py'
Siga as instruções no console para selecionar os diretórios de origem e destino.

<h2>Opção 2: Executar o Executável (Windows)</h2>
Se você não tiver o Python instalado, você pode usar o executável fornecido.
Baixe o executável aqui.
Execute o executável seguindo as instruções.

<h2>Personalização</h2>
O script organiza os arquivos com base nas seguintes condições padrão:
<ul>
<li>Documentos PDF: Arquivos com a extensão .pdf</li>
<li>Documentos de Texto: Arquivos com a extensão .txt</li>
<li>Outros: Todos os outros arquivos</li>
</ul>
Você pode personalizar essas condições diretamente no script organizar.py conforme necessário.

<h2>Criação de Executável (Opcional)</h2>
Se desejar criar um executável para facilitar a execução, você pode usar o PyInstaller. Execute o seguinte comando no terminal para criar um executável:


'pyinstaller --onefile organizar.py'
O executável será gerado na pasta dist.

<h2>Notas Importantes</h2>
<ul>
<li>Certifique-se de fornecer permissões adequadas para acessar e modificar os diretórios especificados.</li>
<li>O executável gerado é específico para o sistema operacional Windows.</li>
<li>Se você encontrar problemas ou erros, consulte a seção de Problemas Conhecidos ou Abra uma Issue.</li>
</ul>
Direitos Reservados developer: Jefferson Fonseca
