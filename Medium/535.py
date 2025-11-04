class Codec:
    def __init__(self):
        # 使用字典存储短链接到原始URL的映射
        self.url_map = {}
        # 使用计数器生成唯一标识
        self.counter = 0
        # 基础短链接域名
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        # 生成唯一标识符
        self.counter += 1
        short_key = str(self.counter)
        # 存储映射关系
        self.url_map[short_key] = longUrl
        # 返回完整的短链接
        return self.base_url + short_key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        # 从短链接中提取标识符
        short_key = shortUrl.replace(self.base_url, "")
        # 从映射字典中获取原始URL
        return self.url_map.get(short_key, "")
