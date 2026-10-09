class RollyPayAdapter:
    async def create_payment(self, *, order_id: int, amount_rub: int, description: str) -> str:
        raise NotImplementedError("Rolly Pay не подключён. Нужна официальная документация API.")
