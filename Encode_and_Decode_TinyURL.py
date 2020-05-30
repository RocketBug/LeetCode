# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    url = {}
    the_http = ""
    def encode(self, longUrl):
        char_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        longUrl = longUrl.split('//')
        url_hash = hash(longUrl[1])
        Codec.the_http = longUrl[0]
        result = ""
        
        if url_hash < 0:
            url_hash *= -1
        
        Codec.url[url_hash] = longUrl[1]
        
        while url_hash > 0:
            result += char_map[int(url_hash%62)]
            url_hash = int(url_hash/62)
            
        result = result[::-1]
        return("http://www.tinyurl.com/"+result)
    
    
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        

    def decode(self, shortUrl):
        code = 0
        url_str = shortUrl.split('/')
        url_str = url_str[3]
        
        for i in url_str:
            
            if ord(i) >= 97 and ord(i) <= 122:
                code = code * 62 + ord(i) - ord('a')

            if ord(i) >= 65 and ord(i) <= 90:
                code = code * 62 + ord(i) - ord('A') + 26
            
            if ord(i) >= 48 and ord(i) <= 57:
                code = code * 62 + ord(i) - ord('0') + 52
            
        return(Codec.the_http+'//'+str(Codec.url[code]))
                                 
        
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))