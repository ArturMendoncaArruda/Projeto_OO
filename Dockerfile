FROM python:3.12.5

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependência
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o restante dos arquivos do projeto
COPY . .

# Expõe a porta para o servidor Django
EXPOSE 8000

# Define o comando para iniciar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
