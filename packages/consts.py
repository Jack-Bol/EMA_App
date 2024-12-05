"""Constants"""

__version__ = "0.1"

API_ENDPOINT = "https://api.tibber.com/v1-beta/gql"
DEFAULT_TIMEOUT = 10
RESPONSE_CODES = {
    0: 'Succeed to request',
    1000: 'Data exception',
    1001: 'No data',
    2000: 'Application account exception',
    2001: 'Invalid application account',
    2002: 'The application account is not authorized',
    2003: 'Application account authorization expires',
    2004: 'The application account has no permission',
    2005: 'The access limit of the application account was exceeded',
    3000: 'Access token exception',
    3001: 'Missing Access token',
    3002: 'Unable to verify Access token',
    3003: 'Access token timeout',
    3004: 'Refresh token timeout',
    4000: 'Request parameter exception',
    4001: 'Invalid request parameter',
    5000: 'Internal server exception',
    6000: 'Communication exception',
    7000: 'Server access restriction exception',
    7001: 'Server access limit exceeded',
    7002: 'Too many requests, please request later',
    7003: 'The system is busy, please request later'
}
