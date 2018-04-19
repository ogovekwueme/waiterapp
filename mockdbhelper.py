import datetime

MOCK_USERS = {'test@example.com': '123456'}
MOCK_TABLES = [{"_id": "1", "number": "1", "owner":
"test@example.com","url": "mockurl"}]
[ 178 ]

MOCK_REQUESTS = [{"_id": "1", "table_number": "1","table_id": "1",
"time": datetime.datetime.now()}]

class MockDBHelper:
    def get_user(self, email):
        if email in MOCK_USERS:
            return MOCK_USERS[email]
        return None
    def add_table(self, number, owner):
        MOCK_TABLES.append({"_id": number, "number": number, "owner":
          owner})
        return number
    def update_table(self, _id, url):
        for table in MOCK_TABLES:
            if table.get("_id") == _id:
                table["url"] = url
                break
    def get_tables(self, owner_id):
        return MOCK_TABLES
    def delete_table(self, table_id):
        for i, table in enumerate(MOCK_TABLES):
            if table.get("_id") == table_id:
                del MOCK_TABLES[i]
                break

    def add_table(self, number, owner):
        MOCK_TABLES.append({"_id": str(number), "number": number, "owner":owner})
        return number
    def get_requests(self, owner_id):
        return MOCK_REQUESTS
    def delete_request(self, request_id):
        for i, request [...]
            if requests [...]
                del MOCK_REQUESTS[i]
                break

