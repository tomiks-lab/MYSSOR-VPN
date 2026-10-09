class VPNProvisioner:
    async def create_access(self, *, telegram_id: int, plan_code: str) -> str:
        raise NotImplementedError("Автоматическая выдача VPN-доступа пока не подключена.")
