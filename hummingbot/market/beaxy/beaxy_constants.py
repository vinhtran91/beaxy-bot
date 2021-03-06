class BeaxyConstants:
    class TradingApi:
        BASE_URL = "https://tradingapi.beaxy.com"
        # BASE_URL = "https://test-tradingapi.tokenexus.com"
        WS_BASE_URL = "wss://tradingapi.beaxy.com/websocket/v1"
        # WS_BASE_URL = "wss://test-tradingapi.tokenexus.com/websocket/v1"
        SECURITIES_ENDPOINT = "/api/v1/securities"
        LOGIN_ATTEMT_ENDPOINT = "/api/v1/login/attempt"
        LOGIN_CONFIRM_ENDPOINT = "/api/v1/login/confirm"
        HEALTH_ENDPOINT = "/api/v1/trader/health"
        ACOUNTS_ENDPOINT = "/api/v1/accounts"
        ORDERS_ENDPOINT = "/api/v1/orders"
        KEEP_ALIVE_ENDPOINT = "/api/v1/login/keepalive"

    class PublicApi:
        BASE_URL = "https://services.beaxy.com"
        # BASE_URL = "https://dev-services.tokenexus.com"
        SYMBOLS_URL = BASE_URL + "/api/v2/symbols"
        RATES_URL = BASE_URL + "/api/v2/symbols/rates"
        ORDER_BOOK_URL = BASE_URL + "/api/v2/symbols/{symbol}/book?depth={depth}"
        WS_BASE_URL = "wss://services.beaxy.com/ws/v2"
