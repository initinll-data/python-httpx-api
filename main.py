import asyncio

from httpx_api import (
    delete_notifications,
    get_notifications,
    post_notification,
    update_notifications,
)


async def main():
    try:
        print('Hello world!')

        print('Fetching ...')
        get_response = await get_notifications()
        print(get_response)

        print('Posting ...')
        post_response = await post_notification()
        print(post_response)

        print('Updating ...')
        update_response = await update_notifications()
        print(update_response)

        print('Deleting ...')
        delete_response = await delete_notifications()
        print(update_response)
    except Exception as ex:
        print(f"Exception: {ex}")

asyncio.run(main())
