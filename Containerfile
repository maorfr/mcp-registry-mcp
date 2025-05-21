FROM registry.redhat.io/ubi9/python-311

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY mcp_registry_mcp_server.py ./

CMD ["python", "mcp_registry_mcp_server.py"] 