"""
    JsonPath模块，是一个专门用于处理Json字符串的模块。JsonPath相当于是Xpath
    部署JsonPath，通过pip install jsonpath来进行安装
    通过JsonPath获得的内容，会以list的形式进行返回，也就意味着你的jsonpath是可以有一个值或者多个值同时存在的。
    如果要基于JsonPath来处理json数据，就一定要同步去处理list
    JsonPath定义中，如果表达式出现错误，则会返回False（布尔类型的值）
    JsonPath要么返回False，要么返回list
"""
import jsonpath,json
data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}
# 基于JsonPath获取元素:通过jsonpath函数来进行获取(json数据,定位表达式)
'''
    jsonpath表达式的基本格式规范：
        $ 表示根节点，也是所有jsonpath的表达式的开始
        . 表示获取子节点
        .. 表示获取所有符合条件的内容
        * 表示所有的元素节点
        [] 表示迭代器的标示（可以用于处理下标等情况）
        [,] 表示多个结果的选择
        ?() 表示过滤操作
        @ 表示当前节点
'''
js=jsonpath.jsonpath(data,'$.store..title')
js1=jsonpath.jsonpath(data,'$..book[?(@.price>15)]')
print(js)
print(js1)