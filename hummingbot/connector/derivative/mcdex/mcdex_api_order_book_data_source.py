from typing import List
from typing import Dict


class McdexAPIOrderBookDataSource:
    @staticmethod
    async def fetch_trading_pairs() -> List[str]:
        return []

    @classmethod
    async def get_last_traded_prices(cls, trading_pairs: List[str]) -> Dict[str, float]:
        """
        This function doesn't really need to return a value.
        It is only currently used for performance calculation which will in turn use the last price of the last trades
        if None is returned.
        """
        pass
