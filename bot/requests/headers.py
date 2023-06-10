import fake_useragent


async def getheaders() -> dict:
    user = fake_useragent.UserAgent().random
    headers = {'user-agent': user}
    return headers

