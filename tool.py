import asyncio
import aiohttp

GREEN = '\033[92m'
RED   = '\033[91m'
RESET = '\033[0m'

URL = 'link đăng kí hp của trường'
COOKIES = {
    'ASC.AUTH' : 'your cookies', 

}
COURSES = {
    'tên môn học': 'mã môn học',
    'tên môn học': 'mã môn học',
    'tên môn học': 'mã môn học',
    'tên môn học': 'mã môn học',
    'tên môn học': 'mã môn học',
    'tên môn học': 'mã môn học'
    
}

MAX_REQUESTS = 1  # Số request tối đa chạy đồng thời

async def post(session, course):
    data = {
        'param[IDDotDangKy]':      45,
        'param[IDLoaiDangKy]':     1,
        'param[GuidIDLopHocPhan]': COURSES[course]
    }

    try:
        async with session.post(URL, data=data) as response:
            result = await response.json()
            code = result.get("Code")

            # Giả sử Code != "01" nghĩa là thành công
            if code != "01":
                print(GREEN, end='')
            else:
                print(RED, end='')

            print(f'{course}: {result}')
            print(RESET, end='')
    except Exception as e:
        print(f"{RED}Lỗi đã xảy ra khi đăng ký {course}: {e}{RESET}")

async def bulk_post():
    async with aiohttp.ClientSession(cookies=COOKIES) as session:
        tasks = [
            post(session, course)
            for course in COURSES
            for _ in range(MAX_REQUESTS)
        ]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(bulk_post())
