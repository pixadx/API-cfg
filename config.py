# config.py - API configuration file

class APIConfig:
    """
    Configuration class for API settings.
    Modify these values according to your API requirements.
    """
    
    # Base API configuration
    BASE_URL = "https://api.example.com/v1"  # Base API endpoint
    TIMEOUT = 30  # Request timeout in seconds
    MAX_RETRIES = 3  # Maximum number of retry attempts
    RETRY_DELAY = 1  # Delay between retries in seconds
    
    # Authentication settings
    API_KEY = "your_api_key_here"  # API key for authentication
    AUTH_TYPE = "Bearer"  # Authentication type (Bearer, Basic, etc.)
    TOKEN = None  # For OAuth tokens or JWT
    
    # Headers configuration
    DEFAULT_HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "MyPythonAPIClient/1.0"
    }
    
    # Rate limiting settings
    RATE_LIMIT = 100  # Maximum requests per minute
    RATE_LIMIT_WINDOW = 60  # Rate limit window in seconds
    
    # Logging configuration
    LOG_REQUESTS = True  # Enable/disable request logging
    LOG_FILE = "api_requests.log"  # Log file path
    
    # SSL/TLS settings
    VERIFY_SSL = True  # Verify SSL certificates
    SSL_CERT_PATH = None  # Path to custom CA bundle
    
    # Proxy configuration
    PROXY = None  # Example: {"http": "http://proxy.example.com:8080", "https": "https://proxy.example.com:8080"}
    
    # Cache settings
    CACHE_ENABLED = False
    CACHE_TTL = 300  # Cache time-to-live in seconds
    
    # Endpoint-specific configurations (add as needed)
    ENDPOINTS = {
        "users": "/users",
        "products": "/products",
        "orders": "/orders"
    }
    
    @classmethod
    def get_endpoint(cls, endpoint_name):
        """Get full endpoint URL by name"""
        if endpoint_name in cls.ENDPOINTS:
            return f"{cls.BASE_URL}{cls.ENDPOINTS[endpoint_name]}"
        raise ValueError(f"Unknown endpoint: {endpoint_name}")


# Example usage:
# from config import APIConfig
# url = APIConfig.get_endpoint("users")
# headers = {**APIConfig.DEFAULT_HEADERS, "Authorization": f"{APIConfig.AUTH_TYPE} {APIConfig.API_KEY}"}
