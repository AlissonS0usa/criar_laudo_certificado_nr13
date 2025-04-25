from fastapi import FastAPI
from app.models import base  # isso garante que os modelos sejam importados
from app.routers import auth, item_conformidade, ponto_espessura, cliente, certificado_valvula, laudo_nr13

app = FastAPI()

app.include_router(auth.router)
app.include_router(cliente.router)
app.include_router(certificado_valvula.router)
app.include_router(laudo_nr13.router)
app.include_router(ponto_espessura.router)
app.include_router(item_conformidade.router)


