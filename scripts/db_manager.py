import aiomysql
from pymysql import connect
from scripts.config import DB_NAME, DB_USER, DB_HOST, DB_PASSWORD
from scripts.models import SearchRequest


async def create_con(loop):
    con = await aiomysql.connect(host=DB_HOST, user=DB_USER, db=DB_NAME, password=DB_PASSWORD, loop=loop)
    cur = await con.cursor()
    return con, cur


def create_sync_con():
    con = connect(host=DB_HOST, user=DB_USER, db=DB_NAME,
                  password=DB_PASSWORD)
    cur = con.cursor()

    return con, cur


class SearchRequestsDbManager:
    @staticmethod
    async def add(request, channel_id, loop):
        con, cur = await create_con(loop)
        await cur.execute(f'insert into search_requests (request, channel_id) values(%s, %s)', (request, channel_id))
        await con.commit()
        con.close()

    @staticmethod
    async def get_all(loop):
        con, cur = await create_con(loop)
        await cur.execute('select * from search_requests')
        requests = await cur.fetchall()
        con.close()

        result = []
        for r in requests:
            result.append(SearchRequest(r[0], r[1], r[2]))
        return result

    @staticmethod
    async def get_by_id(id, loop):
        con, cur = await create_con(loop)
        await cur.execute('select * from search_requests where id = %s', (id))
        item = await cur.fetchone()
        con.close()

        if item is not '' and item is not None:
            return SearchRequest(item[0], item[1], item[2])
        else:
            return None

    @staticmethod
    async def get_by_name(request, loop):
        con, cur = await create_con(loop)
        await cur.execute('select * from search_requests where request = %s', (request))
        item = await cur.fetchone()
        con.close()

        if item is not '' and item is not None:
            return SearchRequest(item[0], item[1], item[2])
        else:
            return None

    @staticmethod
    async def delete(id, loop):
        con, cur = await create_con(loop)
        await cur.execute(f'delete from search_requests where id = {id}')
        await con.commit()
        con.close()


class ItemsShowedDbManager:
    @staticmethod
    async def add(name, url, request_id, loop):
        con, cur = await create_con(loop)
        await cur.execute(f'insert into items_showed values(%s, %s, %s)', (name, url, request_id))
        await con.commit()
        con.close()

    @staticmethod
    async def clear(loop):
        con, cur = await create_con(loop)
        await cur.execute('delete from items_showed')
        await con.commit()
        con.close()

    @staticmethod
    async def exist(url, request_id, loop):
        con, cur = await create_con(loop)
        await cur.execute('select count(*) from items_showed where url = %s and request_id = %s', (url, request_id))
        r = await cur.fetchone()
        count = r[0]
        return count > 0

    @staticmethod
    async def exist_by_name(name, loop):
        con, cur = await create_con(loop)
        await cur.execute('select count(*) from items_showed where name = %s', (name))
        r = await cur.fetchone()
        count = r[0]
        return count > 0

    @staticmethod
    async def count(loop):
        con, cur = await create_con(loop)
        await cur.execute('select count(*) from items_showed')
        r = await cur.fetchone()
        count = r[0]
        return count

