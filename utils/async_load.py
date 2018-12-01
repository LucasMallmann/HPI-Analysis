# import asyncio


# async def find_divisibles(inrange, div_by):
#     print("finding nums in range {} divisible by {}".format(inrange, div_by))
#     located = []
#     for i in range(inrange):
#         if i % div_by == 0:
#             located.append(i)
#         if i % 50000:
#             await asyncio.sleep(0.00001)
#     print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
#     return located


# async def main():
#     divs1 = loop.create_task(find_divisibles(508000, 34113))
#     divs2 = loop.create_task(find_divisibles(100052, 3210))
#     divs3 = loop.create_task(find_divisibles(500, 3))
#     await asyncio.wait([divs1, divs2, divs3])


# if __name__ == '__main__':
#     try:
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(main())
#     except Exception as e:
#         print(e)
#     finally:
#         loop.close()
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])
