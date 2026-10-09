from fastapi import FastAPI
app=FastAPI(title="MYSSOR VPN API")
@app.get("/health")
async def health(): return {"status":"ok","payments":"not_configured","vpn":"not_configured"}
